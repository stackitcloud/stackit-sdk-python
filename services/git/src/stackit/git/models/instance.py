# coding: utf-8

"""
    STACKIT Git API

    Manage STACKIT Git instances.

    The version of the OpenAPI document: 1beta.0.3
    Contact: git@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing_extensions import Annotated, Self


class Instance(BaseModel):
    """
    Describes a STACKIT Git instance.
    """

    created: datetime = Field(description="The date and time the creation of the STACKIT GIT instance was triggered.")
    id: Annotated[str, Field(strict=True, max_length=36)] = Field(
        description="A auto generated unique id which identifies the STACKIT GIT instances."
    )
    name: Annotated[str, Field(strict=True, max_length=32)] = Field(
        description="A user chosen name to distinguish multiple STACKIT GIT instances."
    )
    state: Annotated[str, Field(strict=True, max_length=32)] = Field(
        description="The current state of the STACKIT GIT instance."
    )
    url: Annotated[str, Field(strict=True, max_length=2048)] = Field(
        description="The URL for reaching the STACKIT GIT instance."
    )
    version: Annotated[str, Field(strict=True, max_length=20)] = Field(
        description="The current version of STACKIT GIT deployed to the instance."
    )
    __properties: ClassVar[List[str]] = ["created", "id", "name", "state", "url", "version"]

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["Creating", "WaitingForResources", "Updating", "Deleting", "Ready", "Error"]):
            raise ValueError(
                "must be one of enum values ('Creating', 'WaitingForResources', 'Updating', 'Deleting', 'Ready', 'Error')"
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
        """Create an instance of Instance from a JSON string"""
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
        """Create an instance of Instance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "created": obj.get("created"),
                "id": obj.get("id"),
                "name": obj.get("name"),
                "state": obj.get("state"),
                "url": obj.get("url"),
                "version": obj.get("version"),
            }
        )
        return _obj
