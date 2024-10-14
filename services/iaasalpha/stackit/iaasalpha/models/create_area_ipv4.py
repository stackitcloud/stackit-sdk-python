# coding: utf-8

"""
    IaaS-API

    This API allows you to create and modify IaaS resources.

    The version of the OpenAPI document: 1alpha1
    Contact: stackit-iaas@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing_extensions import Annotated, Self

from stackit.iaasalpha.models.network_range import NetworkRange
from stackit.iaasalpha.models.route import Route


class CreateAreaIPv4(BaseModel):
    """
    The config object for a IPv4 network area.
    """

    default_nameservers: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(max_length=3)]] = Field(
        default=None, alias="defaultNameservers"
    )
    network_ranges: Annotated[List[NetworkRange], Field(min_length=1, max_length=64)] = Field(
        description="A list of network ranges.", alias="networkRanges"
    )
    routes: Optional[List[Route]] = Field(default=None, description="A list of routes.")
    transfer_network: Annotated[str, Field(strict=True)] = Field(
        description="Classless Inter-Domain Routing (CIDR).", alias="transferNetwork"
    )
    default_prefix_len: Optional[Annotated[int, Field(le=29, strict=True, ge=24)]] = Field(
        default=None,
        description="The default prefix length for networks in the network area.",
        alias="defaultPrefixLen",
    )
    max_prefix_len: Optional[Annotated[int, Field(le=29, strict=True, ge=24)]] = Field(
        default=None, description="The maximal prefix length for networks in the network area.", alias="maxPrefixLen"
    )
    min_prefix_len: Optional[Annotated[int, Field(le=29, strict=True, ge=22)]] = Field(
        default=None, description="The minimal prefix length for networks in the network area.", alias="minPrefixLen"
    )
    __properties: ClassVar[List[str]] = [
        "defaultNameservers",
        "networkRanges",
        "routes",
        "transferNetwork",
        "defaultPrefixLen",
        "maxPrefixLen",
        "minPrefixLen",
    ]

    @field_validator("transfer_network")
    def transfer_network_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\/(3[0-2]|2[0-9]|1[0-9]|[0-9]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(\/((1(1[0-9]|2[0-8]))|([0-9][0-9])|([0-9])))?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\/(3[0-2]|2[0-9]|1[0-9]|[0-9]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(\/((1(1[0-9]|2[0-8]))|([0-9][0-9])|([0-9])))?$/"
            )
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
        """Create an instance of CreateAreaIPv4 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in network_ranges (list)
        _items = []
        if self.network_ranges:
            for _item in self.network_ranges:
                if _item:
                    _items.append(_item.to_dict())
            _dict["networkRanges"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in routes (list)
        _items = []
        if self.routes:
            for _item in self.routes:
                if _item:
                    _items.append(_item.to_dict())
            _dict["routes"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateAreaIPv4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "defaultNameservers": obj.get("defaultNameservers"),
                "networkRanges": (
                    [NetworkRange.from_dict(_item) for _item in obj["networkRanges"]]
                    if obj.get("networkRanges") is not None
                    else None
                ),
                "routes": (
                    [Route.from_dict(_item) for _item in obj["routes"]] if obj.get("routes") is not None else None
                ),
                "transferNetwork": obj.get("transferNetwork"),
                "defaultPrefixLen": obj.get("defaultPrefixLen"),
                "maxPrefixLen": obj.get("maxPrefixLen"),
                "minPrefixLen": obj.get("minPrefixLen"),
            }
        )
        return _obj
