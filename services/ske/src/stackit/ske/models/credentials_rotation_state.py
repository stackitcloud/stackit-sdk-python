# coding: utf-8

"""
    SKE-API

    The SKE API provides endpoints to create, update, delete clusters within STACKIT portal projects and to trigger further cluster management tasks.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self


class CredentialsRotationState(BaseModel):
    """
    CredentialsRotationState
    """  # noqa: E501

    last_completion_time: Optional[datetime] = Field(
        default=None, description="Format: `2024-02-15T11:06:29Z`", alias="lastCompletionTime"
    )
    last_initiation_time: Optional[datetime] = Field(
        default=None, description="Format: `2024-02-15T11:06:29Z`", alias="lastInitiationTime"
    )
    phase: Optional[StrictStr] = Field(
        default=None,
        description="Phase of the credentials rotation. `NEVER` indicates that no credentials rotation has been performed using the new credentials rotation endpoints yet. Using the deprecated [rotate-credentials](#tag/Credentials/operation/SkeService_GetClusterCredentials) endpoint will not update this status field.",
    )
    __properties: ClassVar[List[str]] = ["lastCompletionTime", "lastInitiationTime", "phase"]

    @field_validator("phase")
    def phase_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["NEVER", "PREPARING", "PREPARED", "COMPLETING", "COMPLETED"]):
            raise ValueError("must be one of enum values ('NEVER', 'PREPARING', 'PREPARED', 'COMPLETING', 'COMPLETED')")
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
        """Create an instance of CredentialsRotationState from a JSON string"""
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
        """Create an instance of CredentialsRotationState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "lastCompletionTime": obj.get("lastCompletionTime"),
                "lastInitiationTime": obj.get("lastInitiationTime"),
                "phase": obj.get("phase"),
            }
        )
        return _obj
