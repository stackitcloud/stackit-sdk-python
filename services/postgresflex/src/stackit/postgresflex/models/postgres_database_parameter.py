# coding: utf-8

"""
    STACKIT PostgreSQL Flex API

    This is the documentation for the STACKIT postgres service

    The version of the OpenAPI document: 2.0.0
    Contact: support@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing_extensions import Self


class PostgresDatabaseParameter(BaseModel):
    """
    PostgresDatabaseParameter
    """

    context: Optional[StrictStr] = Field(default=None, description="Context of the parameter.")
    data_type: Optional[StrictStr] = Field(
        default=None,
        description="Datatype describes the type of data that is used in the Value field.",
        alias="dataType",
    )
    default_value: Optional[StrictStr] = Field(
        default=None, description="DefaultValue for the value field.", alias="defaultValue"
    )
    description: Optional[StrictStr] = Field(default=None, description="Description of the parameter.")
    edit: Optional[StrictBool] = Field(default=None, description="Edit shows if the user can change this value.")
    max_value: Optional[StrictStr] = Field(
        default=None, description="MaxValue describes the highest possible value that can be set.", alias="maxValue"
    )
    min_value: Optional[StrictStr] = Field(
        default=None, description="MinValue describes the lowest possible value that can be set.", alias="minValue"
    )
    name: Optional[StrictStr] = Field(default=None, description="Name of the parameter.")
    pending_restart: Optional[StrictBool] = Field(
        default=None,
        description="PendingRestart describes if a parameter change requires a restart of the server.",
        alias="pendingRestart",
    )
    reset_value: Optional[StrictStr] = Field(
        default=None, description="ResetValue for the value field af.ter a reset.", alias="resetValue"
    )
    unit: Optional[StrictStr] = Field(default=None, description="Unit if the parameter has a unit if not empty.")
    value: Optional[StrictStr] = Field(default=None, description="Value of this parameter.")
    __properties: ClassVar[List[str]] = [
        "context",
        "dataType",
        "defaultValue",
        "description",
        "edit",
        "maxValue",
        "minValue",
        "name",
        "pendingRestart",
        "resetValue",
        "unit",
        "value",
    ]

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
        """Create an instance of PostgresDatabaseParameter from a JSON string"""
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
        """Create an instance of PostgresDatabaseParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "context": obj.get("context"),
                "dataType": obj.get("dataType"),
                "defaultValue": obj.get("defaultValue"),
                "description": obj.get("description"),
                "edit": obj.get("edit"),
                "maxValue": obj.get("maxValue"),
                "minValue": obj.get("minValue"),
                "name": obj.get("name"),
                "pendingRestart": obj.get("pendingRestart"),
                "resetValue": obj.get("resetValue"),
                "unit": obj.get("unit"),
                "value": obj.get("value"),
            }
        )
        return _obj
