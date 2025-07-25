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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from stackit.kms.models.backend import Backend
from stackit.kms.models.wrapping_algorithm import WrappingAlgorithm
from stackit.kms.models.wrapping_purpose import WrappingPurpose


class WrappingKey(BaseModel):
    """
    WrappingKey
    """  # noqa: E501

    algorithm: WrappingAlgorithm
    backend: Backend
    created_at: datetime = Field(
        description="The date and time the creation of the wrapping key was triggered.", alias="createdAt"
    )
    description: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(
        default=None, description="A user chosen description to distinguish multiple wrapping keys."
    )
    display_name: Annotated[str, Field(strict=True, max_length=64)] = Field(
        description="The display name to distinguish multiple wrapping keys.", alias="displayName"
    )
    expires_at: datetime = Field(description="The date and time the wrapping key will expire.", alias="expiresAt")
    id: StrictStr = Field(description="A auto generated unique id which identifies the wrapping keys.")
    key_ring_id: StrictStr = Field(
        description="The unique id of the key ring this wrapping key is assigned to.", alias="keyRingId"
    )
    public_key: Optional[StrictStr] = Field(
        default=None, description="The public key of the wrapping key.", alias="publicKey"
    )
    purpose: WrappingPurpose
    state: StrictStr = Field(description="The current state of the wrapping key.")
    __properties: ClassVar[List[str]] = [
        "algorithm",
        "backend",
        "createdAt",
        "description",
        "displayName",
        "expiresAt",
        "id",
        "keyRingId",
        "publicKey",
        "purpose",
        "state",
    ]

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["active", "creating", "expired", "deleted", "key_material_unavailable"]):
            raise ValueError(
                "must be one of enum values ('active', 'creating', 'expired', 'deleted', 'key_material_unavailable')"
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
        """Create an instance of WrappingKey from a JSON string"""
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
        """Create an instance of WrappingKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "algorithm": obj.get("algorithm"),
                "backend": obj.get("backend"),
                "createdAt": obj.get("createdAt"),
                "description": obj.get("description"),
                "displayName": obj.get("displayName"),
                "expiresAt": obj.get("expiresAt"),
                "id": obj.get("id"),
                "keyRingId": obj.get("keyRingId"),
                "publicKey": obj.get("publicKey"),
                "purpose": obj.get("purpose"),
                "state": obj.get("state"),
            }
        )
        return _obj
