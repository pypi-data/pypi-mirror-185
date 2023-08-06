# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, Optional, Sequence

from google.ads.googleads.client import GoogleAdsClient  # type: ignore
from importlib import import_module
from pathlib import Path
from proto.primitives import ProtoType


class BaseClient:

    def get_response(self, entity_id: str, query_text: str):
        pass


class GoogleAdsApiClient(BaseClient):
    default_google_ads_yaml = str(Path.home() / "google-ads.yaml")

    def __init__(self,
                 path_to_config: str = default_google_ads_yaml,
                 config_dict: Dict[str, Any] = None,
                 yaml_str: str = None,
                 version: str = "v12"):
        self.client = self._init_client(path=path_to_config,
                                        config_dict=config_dict,
                                        yaml_str=yaml_str,
                                        version=version)
        self.ads_service = self.client.get_service("GoogleAdsService")
        self.api_version = version
        self.google_ads_row = self._get_google_ads_row(version)


    def _get_google_ads_row(self, api_version: str) -> "GoogleAdsRow":
        base_module = f"google.ads.googleads.{api_version}"
        google_ads_service = import_module(f"{base_module}.services.types.google_ads_service")
        return google_ads_service.GoogleAdsRow()

    def get_response(self, entity_id, query_text):
        response = self.ads_service.search_stream(customer_id=entity_id,
                                                  query=query_text)
        return response

    def _init_client(self, path, config_dict, yaml_str,
                     version) -> Optional[GoogleAdsClient]:
        if path:
            return GoogleAdsClient.load_from_storage(path, version)
        if config_dict:
            return GoogleAdsClient.load_from_dict(config_dict, version)
        if yaml_str:
            return GoogleAdsClient.load_from_string(yaml_str, version)
        try:
            return GoogleAdsClient.load_from_env(version)
        except Exception as e:
            raise ValueError("Cannot instantiate GoogleAdsClient")


def clean_resource(resource: str) -> str:
    return resource.title().replace('_', '')
