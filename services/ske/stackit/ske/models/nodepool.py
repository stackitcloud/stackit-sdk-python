# coding: utf-8

"""
    SKE-API

    The SKE API provides endpoints to create, update, delete clusters within STACKIT portal projects and to trigger further cluster management tasks.

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing_extensions import Annotated, Self

from stackit.ske.models.cri import CRI
from stackit.ske.models.machine import Machine
from stackit.ske.models.taint import Taint
from stackit.ske.models.volume import Volume


class Nodepool(BaseModel):
    """
    Nodepool
    """

    allow_system_components: Optional[StrictBool] = Field(
        default=None, description="This needs to be true for at least one node pool.", alias="allowSystemComponents"
    )
    availability_zones: List[StrictStr] = Field(alias="availabilityZones")
    cri: Optional[CRI] = None
    labels: Optional[Dict[str, StrictStr]] = None
    machine: Machine
    max_surge: Optional[StrictInt] = Field(default=None, alias="maxSurge")
    max_unavailable: Optional[StrictInt] = Field(default=None, alias="maxUnavailable")
    maximum: Annotated[int, Field(strict=True, ge=1)]
    minimum: StrictInt
    name: StrictStr = Field(description="Maximum 15 chars")
    taints: Optional[List[Taint]] = None
    volume: Volume
    __properties: ClassVar[List[str]] = [
        "allowSystemComponents",
        "availabilityZones",
        "cri",
        "labels",
        "machine",
        "maxSurge",
        "maxUnavailable",
        "maximum",
        "minimum",
        "name",
        "taints",
        "volume",
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
        """Create an instance of Nodepool from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cri
        if self.cri:
            _dict["cri"] = self.cri.to_dict()
        # override the default output from pydantic by calling `to_dict()` of machine
        if self.machine:
            _dict["machine"] = self.machine.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in taints (list)
        _items = []
        if self.taints:
            for _item in self.taints:
                if _item:
                    _items.append(_item.to_dict())
            _dict["taints"] = _items
        # override the default output from pydantic by calling `to_dict()` of volume
        if self.volume:
            _dict["volume"] = self.volume.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Nodepool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "allowSystemComponents": obj.get("allowSystemComponents"),
                "availabilityZones": obj.get("availabilityZones"),
                "cri": CRI.from_dict(obj["cri"]) if obj.get("cri") is not None else None,
                "labels": obj.get("labels"),
                "machine": Machine.from_dict(obj["machine"]) if obj.get("machine") is not None else None,
                "maxSurge": obj.get("maxSurge"),
                "maxUnavailable": obj.get("maxUnavailable"),
                "maximum": obj.get("maximum"),
                "minimum": obj.get("minimum"),
                "name": obj.get("name"),
                "taints": (
                    [Taint.from_dict(_item) for _item in obj["taints"]] if obj.get("taints") is not None else None
                ),
                "volume": Volume.from_dict(obj["volume"]) if obj.get("volume") is not None else None,
            }
        )
        return _obj
