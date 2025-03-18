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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from stackit.runcommand.models.model_field import ModelField


class Properties(BaseModel):
    """
    Properties
    """

    confirm_password: Optional[ModelField] = Field(default=None, alias="ConfirmPassword")
    password: Optional[ModelField] = Field(default=None, alias="Password")
    script: Optional[ModelField] = Field(default=None, alias="Script")
    username: Optional[ModelField] = Field(default=None, alias="Username")
    required: Optional[List[StrictStr]] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["ConfirmPassword", "Password", "Script", "Username", "required", "type"]

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
        """Create an instance of Properties from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of confirm_password
        if self.confirm_password:
            _dict["ConfirmPassword"] = self.confirm_password.to_dict()
        # override the default output from pydantic by calling `to_dict()` of password
        if self.password:
            _dict["Password"] = self.password.to_dict()
        # override the default output from pydantic by calling `to_dict()` of script
        if self.script:
            _dict["Script"] = self.script.to_dict()
        # override the default output from pydantic by calling `to_dict()` of username
        if self.username:
            _dict["Username"] = self.username.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Properties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "ConfirmPassword": (
                    ModelField.from_dict(obj["ConfirmPassword"]) if obj.get("ConfirmPassword") is not None else None
                ),
                "Password": ModelField.from_dict(obj["Password"]) if obj.get("Password") is not None else None,
                "Script": ModelField.from_dict(obj["Script"]) if obj.get("Script") is not None else None,
                "Username": ModelField.from_dict(obj["Username"]) if obj.get("Username") is not None else None,
                "required": obj.get("required"),
                "type": obj.get("type"),
            }
        )
        return _obj
