# coding: utf-8

"""
    STACKIT Key Management Service API

    This API provides endpoints for managing keys and key rings. 

    The version of the OpenAPI document: 1beta.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing_extensions import Annotated, Self

from stackit.kms.models.algorithm import Algorithm
from stackit.kms.models.backend import Backend
from stackit.kms.models.purpose import Purpose


class Key(BaseModel):
    """
    Key
    """  # noqa: E501

    algorithm: Algorithm
    backend: Backend
    created_at: datetime = Field(
        description="The date and time the creation of the key was triggered.", alias="createdAt"
    )
    deletion_date: Optional[datetime] = Field(
        default=None,
        description="This date is set when a key is pending deletion and refers to the scheduled date of deletion",
        alias="deletionDate",
    )
    description: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(
        default=None, description="A user chosen description to distinguish multiple keys."
    )
    display_name: Annotated[str, Field(strict=True, max_length=64)] = Field(
        description="The display name to distinguish multiple keys.", alias="displayName"
    )
    id: StrictStr = Field(description="A auto generated unique id which identifies the keys.")
    import_only: Optional[StrictBool] = Field(
        default=False, description="States whether versions can be created or only imported.", alias="importOnly"
    )
    key_ring_id: StrictStr = Field(
        description="The unique id of the key ring this key is assigned to.", alias="keyRingId"
    )
    purpose: Purpose
    state: StrictStr = Field(description="The current state of the key.")
    __properties: ClassVar[List[str]] = [
        "algorithm",
        "backend",
        "createdAt",
        "deletionDate",
        "description",
        "displayName",
        "id",
        "importOnly",
        "keyRingId",
        "purpose",
        "state",
    ]

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["active", "deleted", "not_available", "errors_exist", "creating", "no_version"]):
            raise ValueError(
                "must be one of enum values ('active', 'deleted', 'not_available', 'errors_exist', 'creating', 'no_version')"
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
        """Create an instance of Key from a JSON string"""
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
        """Create an instance of Key from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "algorithm": obj.get("algorithm"),
                "backend": obj.get("backend"),
                "createdAt": obj.get("createdAt"),
                "deletionDate": obj.get("deletionDate"),
                "description": obj.get("description"),
                "displayName": obj.get("displayName"),
                "id": obj.get("id"),
                "importOnly": obj.get("importOnly") if obj.get("importOnly") is not None else False,
                "keyRingId": obj.get("keyRingId"),
                "purpose": obj.get("purpose"),
                "state": obj.get("state"),
            }
        )
        return _obj
