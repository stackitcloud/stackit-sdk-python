# coding: utf-8

"""
    STACKIT Marketplace API

    API to manage STACKIT Marketplace.

    The version of the OpenAPI document: 1
    Contact: marketplace@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing_extensions import Annotated, Self


class CatalogProductOverviewVendor(BaseModel):
    """
    CatalogProductOverviewVendor
    """  # noqa: E501

    name: Annotated[str, Field(strict=True, max_length=512)] = Field(description="The product's vendor name.")
    vendor_id: Annotated[str, Field(min_length=36, strict=True, max_length=36)] = Field(
        description="Universally Unique Identifier (UUID).", alias="vendorId"
    )
    website_url: Annotated[str, Field(strict=True, max_length=512)] = Field(
        description="Uniform Resource Locator.", alias="websiteUrl"
    )
    __properties: ClassVar[List[str]] = ["name", "vendorId", "websiteUrl"]

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-ZäüöÄÜÖ0-9,.!?()@\/:=\n\t -]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-ZäüöÄÜÖ0-9,.!?()@\/:=\n\t -]+$/")
        return value

    @field_validator("vendor_id")
    def vendor_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(
                r"must validate the regular expression /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/"
            )
        return value

    @field_validator("website_url")
    def website_url_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$", value):
            raise ValueError(
                r"must validate the regular expression /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/"
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
        """Create an instance of CatalogProductOverviewVendor from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CatalogProductOverviewVendor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {"name": obj.get("name"), "vendorId": obj.get("vendorId"), "websiteUrl": obj.get("websiteUrl")}
        )
        return _obj
