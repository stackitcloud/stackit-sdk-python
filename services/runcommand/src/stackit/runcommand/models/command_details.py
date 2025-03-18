# coding: utf-8

"""
    STACKIT Run Commands Service API

    API endpoints for the STACKIT Run Commands Service API

    The version of the OpenAPI document: 2.0
    Contact: support@stackit.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing_extensions import Self


class CommandDetails(BaseModel):
    """
    CommandDetails
    """

    command_template_name: Optional[StrictStr] = Field(default=None, alias="commandTemplateName")
    command_template_title: Optional[StrictStr] = Field(default=None, alias="commandTemplateTitle")
    exit_code: Optional[StrictInt] = Field(default=None, alias="exitCode")
    finished_at: Optional[StrictStr] = Field(default=None, alias="finishedAt")
    id: Optional[StrictInt] = None
    output: Optional[StrictStr] = None
    script: Optional[StrictStr] = None
    started_at: Optional[StrictStr] = Field(default=None, alias="startedAt")
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "commandTemplateName",
        "commandTemplateTitle",
        "exitCode",
        "finishedAt",
        "id",
        "output",
        "script",
        "startedAt",
        "status",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["pending", "running", "completed", "failed"]):
            raise ValueError("must be one of enum values ('pending', 'running', 'completed', 'failed')")
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
        """Create an instance of CommandDetails from a JSON string"""
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
        """Create an instance of CommandDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "commandTemplateName": obj.get("commandTemplateName"),
                "commandTemplateTitle": obj.get("commandTemplateTitle"),
                "exitCode": obj.get("exitCode"),
                "finishedAt": obj.get("finishedAt"),
                "id": obj.get("id"),
                "output": obj.get("output"),
                "script": obj.get("script"),
                "startedAt": obj.get("startedAt"),
                "status": obj.get("status"),
            }
        )
        return _obj
