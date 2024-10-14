# coding: utf-8

"""
    STACKIT Service Enablement API

    STACKIT Service Enablement API

    The version of the OpenAPI document: 1.1
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

from stackit.serviceenablement.models.action_error import ActionError
from stackit.serviceenablement.models.dependencies import Dependencies
from stackit.serviceenablement.models.parameters import Parameters


class ServiceStatus(BaseModel):
    """
    ServiceStatus
    """

    dependencies: Optional[Dependencies] = None
    enablement: Optional[StrictStr] = "REQUEST"
    error: Optional[ActionError] = None
    labels: Optional[Dict[str, StrictStr]] = None
    lifecycle: Optional[StrictStr] = "FLEX"
    parameters: Optional[Parameters] = None
    scope: Optional[StrictStr] = "PUBLIC"
    service_id: Optional[Annotated[str, Field(min_length=10, strict=True, max_length=255)]] = Field(
        default=None, description="the id of the service", alias="serviceId"
    )
    state: Optional[StrictStr] = Field(default="ENABLED", description="the state of a service within a project")
    __properties: ClassVar[List[str]] = [
        "dependencies",
        "enablement",
        "error",
        "labels",
        "lifecycle",
        "parameters",
        "scope",
        "serviceId",
        "state",
    ]

    @field_validator("enablement")
    def enablement_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["REQUEST", "AUTO"]):
            raise ValueError("must be one of enum values ('REQUEST', 'AUTO')")
        return value

    @field_validator("lifecycle")
    def lifecycle_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["FLEX", "PROJECT"]):
            raise ValueError("must be one of enum values ('FLEX', 'PROJECT')")
        return value

    @field_validator("scope")
    def scope_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["PRIVATE", "PUBLIC"]):
            raise ValueError("must be one of enum values ('PRIVATE', 'PUBLIC')")
        return value

    @field_validator("service_id")
    def service_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{1,254}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9][a-zA-Z0-9._-]{1,254}$/")
        return value

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["ENABLED", "ENABLING", "DISABLED", "DISABLING"]):
            raise ValueError("must be one of enum values ('ENABLED', 'ENABLING', 'DISABLED', 'DISABLING')")
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
        """Create an instance of ServiceStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dependencies
        if self.dependencies:
            _dict["dependencies"] = self.dependencies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict["parameters"] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "dependencies": (
                    Dependencies.from_dict(obj["dependencies"]) if obj.get("dependencies") is not None else None
                ),
                "enablement": obj.get("enablement") if obj.get("enablement") is not None else "REQUEST",
                "error": ActionError.from_dict(obj["error"]) if obj.get("error") is not None else None,
                "labels": obj.get("labels"),
                "lifecycle": obj.get("lifecycle") if obj.get("lifecycle") is not None else "FLEX",
                "parameters": Parameters.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None,
                "scope": obj.get("scope") if obj.get("scope") is not None else "PUBLIC",
                "serviceId": obj.get("serviceId"),
                "state": obj.get("state") if obj.get("state") is not None else "ENABLED",
            }
        )
        return _obj
