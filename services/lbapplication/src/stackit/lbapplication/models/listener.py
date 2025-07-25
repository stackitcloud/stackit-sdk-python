# coding: utf-8

"""
    Application Load Balancer API

    ### DEPRECATED! This service, lb-application, is no longer maintained. Please use the alb service, version v2beta2 instead  This API offers an interface to provision and manage load balancing servers in your STACKIT project. It also has the possibility of pooling target servers for load balancing purposes.  For each application load balancer provided, two VMs are deployed in your OpenStack project subject to a fee.

    The version of the OpenAPI document: 1beta.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from stackit.lbapplication.models.protocol_options_https import ProtocolOptionsHTTPS
from stackit.lbapplication.models.rule import Rule


class Listener(BaseModel):
    """
    Listener
    """  # noqa: E501

    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    http: Optional[Dict[str, Any]] = None
    https: Optional[ProtocolOptionsHTTPS] = None
    name: Optional[StrictStr] = Field(
        default=None,
        description="Will be used to reference a listener and will replace display name in the future. Currently uses <protocol>-<port> as the name if no display name is given.",
    )
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(
        default=None, description="Port number where we listen for traffic"
    )
    protocol: Optional[StrictStr] = Field(
        default=None,
        description="Protocol is the highest network protocol we understand to load balance. Currently PROTOCOL_HTTP and PROTOCOL_HTTPS are supported.",
    )
    rules: Optional[List[Rule]] = Field(
        default=None, description="Rules define the routing parameters for the HTTP and HTTPS listeners."
    )
    __properties: ClassVar[List[str]] = ["displayName", "http", "https", "name", "port", "protocol", "rules"]

    @field_validator("protocol")
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["PROTOCOL_UNSPECIFIED", "PROTOCOL_HTTP", "PROTOCOL_HTTPS"]):
            raise ValueError("must be one of enum values ('PROTOCOL_UNSPECIFIED', 'PROTOCOL_HTTP', 'PROTOCOL_HTTPS')")
        return value

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
        """Create an instance of Listener from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "name",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of https
        if self.https:
            _dict["https"] = self.https.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict["rules"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Listener from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "displayName": obj.get("displayName"),
                "http": obj.get("http"),
                "https": ProtocolOptionsHTTPS.from_dict(obj["https"]) if obj.get("https") is not None else None,
                "name": obj.get("name"),
                "port": obj.get("port"),
                "protocol": obj.get("protocol"),
                "rules": [Rule.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            }
        )
        return _obj
