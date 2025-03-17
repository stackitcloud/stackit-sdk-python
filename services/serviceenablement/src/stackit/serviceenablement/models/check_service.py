# coding: utf-8

"""
    STACKIT Service Enablement API

    STACKIT Service Enablement API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self


class CheckService(BaseModel):
    """
    CheckService
    """

    resource: Optional[StrictStr] = Field(default=None, description="the identifier of the resource e.g. projectID")
    resource_type: Optional[StrictStr] = Field(default="project", alias="resourceType")
    service_id: Optional[Annotated[str, Field(min_length=10, strict=True, max_length=255)]] = Field(
        default=None, description="the id of the service", alias="serviceId"
    )
    __properties: ClassVar[List[str]] = ["resource", "resourceType", "serviceId"]

    @field_validator("resource_type")
    def resource_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["project"]):
            raise ValueError("must be one of enum values ('project')")
        return value

    @field_validator("service_id")
    def service_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{1,254}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9][a-zA-Z0-9._-]{1,254}$/")
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
        """Create an instance of CheckService from a JSON string"""
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
        """Create an instance of CheckService from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "resource": obj.get("resource"),
                "resourceType": obj.get("resourceType") if obj.get("resourceType") is not None else "project",
                "serviceId": obj.get("serviceId"),
            }
        )
        return _obj
