# coding: utf-8

"""
    STACKIT Redis API

    The STACKIT Redis API provides endpoints to list service offerings, manage service instances and service credentials within STACKIT portal projects.

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Self

from stackit.redis.models.instance_schema import InstanceSchema
from stackit.redis.models.plan import Plan


class Offering(BaseModel):
    """
    Offering
    """

    description: StrictStr
    documentation_url: StrictStr = Field(alias="documentationUrl")
    image_url: StrictStr = Field(alias="imageUrl")
    latest: StrictBool
    lifecycle: Optional[StrictStr] = None
    name: StrictStr
    plans: List[Plan]
    quota_count: StrictInt = Field(alias="quotaCount")
    var_schema: Optional[InstanceSchema] = Field(default=None, alias="schema")
    version: StrictStr
    __properties: ClassVar[List[str]] = [
        "description",
        "documentationUrl",
        "imageUrl",
        "latest",
        "lifecycle",
        "name",
        "plans",
        "quotaCount",
        "schema",
        "version",
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
        """Create an instance of Offering from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in plans (list)
        _items = []
        if self.plans:
            for _item in self.plans:
                if _item:
                    _items.append(_item.to_dict())
            _dict["plans"] = _items
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict["schema"] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Offering from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "description": obj.get("description"),
                "documentationUrl": obj.get("documentationUrl"),
                "imageUrl": obj.get("imageUrl"),
                "latest": obj.get("latest"),
                "lifecycle": obj.get("lifecycle"),
                "name": obj.get("name"),
                "plans": [Plan.from_dict(_item) for _item in obj["plans"]] if obj.get("plans") is not None else None,
                "quotaCount": obj.get("quotaCount"),
                "schema": InstanceSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
                "version": obj.get("version"),
            }
        )
        return _obj
