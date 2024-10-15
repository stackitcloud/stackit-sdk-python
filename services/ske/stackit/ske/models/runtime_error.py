# coding: utf-8

"""
    SKE-API

    The SKE API provides endpoints to create, update, delete clusters within STACKIT portal projects and to trigger further cluster management tasks.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self


class RuntimeError(BaseModel):
    """
    RuntimeError
    """

    code: Optional[StrictStr] = Field(
        default=None,
        description='- Code:    `SKE_UNSPECIFIED`   Message: "An error occurred. Please open a support ticket if this error persists." - Code:    `SKE_TMP_AUTH_ERROR`   Message: "Authentication failed. This is a temporary error. Please wait while the system recovers." - Code:    `SKE_QUOTA_EXCEEDED`   Message: "Your project\'s resource quotas are exhausted. Please make sure your quota is sufficient for the ordered cluster." - Code:    `SKE_ARGUS_INSTANCE_NOT_FOUND`   Message: "The provided Argus instance could not be found." - Code:    `SKE_RATE_LIMITS`   Message: "While provisioning your cluster, request rate limits where incurred. Please wait while the system recovers." - Code:    `SKE_INFRA_ERROR`   Message: "An error occurred with the underlying infrastructure. Please open a support ticket if this error persists." - Code:    `SKE_REMAINING_RESOURCES`   Message: "There are remaining Kubernetes resources in your cluster that prevent deletion. Please make sure to remove them." - Code:    `SKE_CONFIGURATION_PROBLEM`   Message: "A configuration error occurred. Please open a support ticket if this error persists." - Code:    `SKE_UNREADY_NODES`   Message: "Not all worker nodes are ready. Please open a support ticket if this error persists." - Code:    `SKE_API_SERVER_ERROR`   Message: "The Kubernetes API server is not reporting readiness. Please open a support ticket if this error persists." - Code:    `SKE_DNS_ZONE_NOT_FOUND`   Message: "The provided DNS zone for the STACKIT DNS extension could not be found. Please ensure you defined a valid domain that belongs to a STACKIT DNS zone." ',
    )
    details: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["code", "details", "message"]

    @field_validator("code")
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            [
                "SKE_UNSPECIFIED",
                "SKE_TMP_AUTH_ERROR",
                "SKE_QUOTA_EXCEEDED",
                "SKE_ARGUS_INSTANCE_NOT_FOUND",
                "SKE_RATE_LIMITS",
                "SKE_INFRA_ERROR",
                "SKE_REMAINING_RESOURCES",
                "SKE_CONFIGURATION_PROBLEM",
                "SKE_UNREADY_NODES",
                "SKE_API_SERVER_ERROR",
                "SKE_DNS_ZONE_NOT_FOUND",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('SKE_UNSPECIFIED', 'SKE_TMP_AUTH_ERROR', 'SKE_QUOTA_EXCEEDED', 'SKE_ARGUS_INSTANCE_NOT_FOUND', 'SKE_RATE_LIMITS', 'SKE_INFRA_ERROR', 'SKE_REMAINING_RESOURCES', 'SKE_CONFIGURATION_PROBLEM', 'SKE_UNREADY_NODES', 'SKE_API_SERVER_ERROR', 'SKE_DNS_ZONE_NOT_FOUND')"
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
        """Create an instance of RuntimeError from a JSON string"""
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
        """Create an instance of RuntimeError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {"code": obj.get("code"), "details": obj.get("details"), "message": obj.get("message")}
        )
        return _obj
