# coding: utf-8

"""
    STACKIT DNS API

    This api provides dns

    The version of the OpenAPI document: 1.0
    Contact: stackit-dns@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated, Self

from stackit.dns.models.record_payload import RecordPayload


class PartialUpdateRecordSetPayload(BaseModel):
    """
    RRSetPatch for rr patch set info.
    """

    comment: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None, description="user comment"
    )
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=253)]] = Field(
        default=None, description="rfc1035 Section 2.3.4"
    )
    records: Optional[List[RecordPayload]] = Field(default=None, description="records")
    ttl: Optional[Annotated[int, Field(le=99999999, strict=True, ge=30)]] = Field(
        default=None, description="time to live"
    )
    __properties: ClassVar[List[str]] = ["comment", "name", "records", "ttl"]

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
        """Create an instance of PartialUpdateRecordSetPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in records (list)
        _items = []
        if self.records:
            for _item in self.records:
                if _item:
                    _items.append(_item.to_dict())
            _dict["records"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PartialUpdateRecordSetPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "comment": obj.get("comment"),
                "name": obj.get("name"),
                "records": (
                    [RecordPayload.from_dict(_item) for _item in obj["records"]]
                    if obj.get("records") is not None
                    else None
                ),
                "ttl": obj.get("ttl"),
            }
        )
        return _obj
