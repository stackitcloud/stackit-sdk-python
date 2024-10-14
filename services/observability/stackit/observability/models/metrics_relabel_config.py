# coding: utf-8

"""
    STACKIT Observability API

    API endpoints for Observability on STACKIT

    The version of the OpenAPI document: 1.1.1
    Contact: stackit-argus@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self


class MetricsRelabelConfig(BaseModel):
    """
    MetricsRelabelConfig
    """

    action: Optional[StrictStr] = "replace"
    modulus: Optional[Annotated[int, Field(le=200, strict=True)]] = None
    regex: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=400)]] = ".*"
    replacement: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = "$1"
    separator: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=20)]] = ";"
    source_labels: Annotated[
        List[Annotated[str, Field(min_length=1, strict=True, max_length=200)]], Field(max_length=5)
    ] = Field(alias="sourceLabels")
    target_label: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(
        default=None, alias="targetLabel"
    )
    __properties: ClassVar[List[str]] = [
        "action",
        "modulus",
        "regex",
        "replacement",
        "separator",
        "sourceLabels",
        "targetLabel",
    ]

    @field_validator("action")
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["replace", "keep", "drop", "hashmod", "labelmap", "labeldrop", "labelkeep"]):
            raise ValueError(
                "must be one of enum values ('replace', 'keep', 'drop', 'hashmod', 'labelmap', 'labeldrop', 'labelkeep')"
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
        """Create an instance of MetricsRelabelConfig from a JSON string"""
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
        """Create an instance of MetricsRelabelConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "action": obj.get("action") if obj.get("action") is not None else "replace",
                "modulus": obj.get("modulus"),
                "regex": obj.get("regex") if obj.get("regex") is not None else ".*",
                "replacement": obj.get("replacement") if obj.get("replacement") is not None else "$1",
                "separator": obj.get("separator") if obj.get("separator") is not None else ";",
                "sourceLabels": obj.get("sourceLabels"),
                "targetLabel": obj.get("targetLabel"),
            }
        )
        return _obj
