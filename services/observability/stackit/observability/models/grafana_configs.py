# coding: utf-8

"""
    STACKIT Observability API

    API endpoints for Observability on STACKIT

    The version of the OpenAPI document: 1.1.1
    Contact: stackit-argus@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing_extensions import Annotated, Self

from stackit.observability.models.grafana_oauth import GrafanaOauth


class GrafanaConfigs(BaseModel):
    """
    GrafanaConfigs
    """

    generic_oauth: Optional[GrafanaOauth] = Field(default=None, alias="genericOauth")
    message: Annotated[str, Field(min_length=1, strict=True)]
    public_read_access: Optional[StrictBool] = Field(default=None, alias="publicReadAccess")
    use_stackit_sso: Optional[StrictBool] = Field(default=None, alias="useStackitSso")
    __properties: ClassVar[List[str]] = ["genericOauth", "message", "publicReadAccess", "useStackitSso"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GrafanaConfigs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of generic_oauth
        if self.generic_oauth:
            _dict["genericOauth"] = self.generic_oauth.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GrafanaConfigs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "genericOauth": (
                    GrafanaOauth.from_dict(obj["genericOauth"]) if obj.get("genericOauth") is not None else None
                ),
                "message": obj.get("message"),
                "publicReadAccess": obj.get("publicReadAccess"),
                "useStackitSso": obj.get("useStackitSso"),
            }
        )
        return _obj
