# coding: utf-8

"""
    STACKIT MongoDB Service API

    This is the documentation for the STACKIT MongoDB Flex Service API

    The version of the OpenAPI document: 1.0.0
    Contact: support@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from stackit.mongodbflex.models.mongodbatlas_stats import MongodbatlasStats


class MongodbatlasOperation(BaseModel):
    """
    MongodbatlasOperation
    """

    predicates: Optional[List[Dict[str, Any]]] = Field(
        default=None, description="Documents containing the search criteria used by the query."
    )
    raw: Optional[StrictStr] = Field(default=None, description="Raw log line produced by the query.")
    stats: Optional[MongodbatlasStats] = Field(default=None, description="Query statistics.")
    __properties: ClassVar[List[str]] = ["predicates", "raw", "stats"]

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
        """Create an instance of MongodbatlasOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict["stats"] = self.stats.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MongodbatlasOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "predicates": obj.get("predicates"),
                "raw": obj.get("raw"),
                "stats": MongodbatlasStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            }
        )
        return _obj
