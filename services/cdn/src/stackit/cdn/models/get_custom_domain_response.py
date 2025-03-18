# coding: utf-8

"""
    CDN API

    API used to create and manage your CDN distributions.

    The version of the OpenAPI document: 1beta.0.0
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

from stackit.cdn.models.custom_domain import CustomDomain


class GetCustomDomainResponse(BaseModel):
    """
    GetCustomDomainResponse
    """

    custom_domain: CustomDomain = Field(alias="customDomain")
    domain: Annotated[str, Field(strict=True, max_length=72)]
    __properties: ClassVar[List[str]] = ["customDomain", "domain"]

    @field_validator("domain")
    def domain_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[.\-A-Za-z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[.\-A-Za-z0-9]*$/")
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
        """Create an instance of GetCustomDomainResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_domain
        if self.custom_domain:
            _dict["customDomain"] = self.custom_domain.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetCustomDomainResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "customDomain": (
                    CustomDomain.from_dict(obj["customDomain"]) if obj.get("customDomain") is not None else None
                ),
                "domain": obj.get("domain"),
            }
        )
        return _obj
