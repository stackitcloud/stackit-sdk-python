# coding: utf-8

"""
    STACKIT MSSQL Service API

    This is the documentation for the STACKIT MSSQL service

    The version of the OpenAPI document: 2.0.0
    Contact: support@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Self

from stackit.sqlserverflex.models.acl import ACL
from stackit.sqlserverflex.models.flavor import Flavor
from stackit.sqlserverflex.models.storage import Storage


class Instance(BaseModel):
    """
    Instance
    """  # noqa: E501

    acl: Optional[ACL] = None
    backup_schedule: Optional[StrictStr] = Field(default=None, alias="backupSchedule")
    flavor: Optional[Flavor] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    options: Optional[Dict[str, StrictStr]] = None
    replicas: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    storage: Optional[Storage] = None
    version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "acl",
        "backupSchedule",
        "flavor",
        "id",
        "name",
        "options",
        "replicas",
        "status",
        "storage",
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
        # override the default output from pydantic by calling `to_dict()` of acl
        if self.acl:
            _dict["acl"] = self.acl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flavor
        if self.flavor:
            _dict["flavor"] = self.flavor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict["storage"] = self.storage.to_dict()
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
                "acl": ACL.from_dict(obj["acl"]) if obj.get("acl") is not None else None,
                "backupSchedule": obj.get("backupSchedule"),
                "flavor": Flavor.from_dict(obj["flavor"]) if obj.get("flavor") is not None else None,
                "id": obj.get("id"),
                "name": obj.get("name"),
                "options": obj.get("options"),
                "replicas": obj.get("replicas"),
                "status": obj.get("status"),
                "storage": Storage.from_dict(obj["storage"]) if obj.get("storage") is not None else None,
                "version": obj.get("version"),
            }
        )
        return _obj
