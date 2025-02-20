# coding: utf-8

"""
    STACKIT MSSQL Service API

    This is the documentation for the STACKIT MSSQL service

    The version of the OpenAPI document: 2.0.0
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

from stackit.sqlserverflex.models.instance_documentation_acl import (
    InstanceDocumentationACL,
)
from stackit.sqlserverflex.models.instance_documentation_options import (
    InstanceDocumentationOptions,
)
from stackit.sqlserverflex.models.instance_documentation_storage import (
    InstanceDocumentationStorage,
)


class CreateInstancePayload(BaseModel):
    """
    CreateInstancePayload
    """

    acl: Optional[InstanceDocumentationACL] = Field(
        default=None,
        description="ACL is the Access Control List defining the IP ranges allowed to connect to the database",
    )
    backup_schedule: Optional[StrictStr] = Field(
        default=None,
        description="Cronjob for the daily full backup if not provided a job will generated between 00:00 and 04:59",
        alias="backupSchedule",
    )
    flavor_id: StrictStr = Field(description="Id of the selected flavor", alias="flavorId")
    labels: Optional[Dict[str, Any]] = Field(default=None, description="Labels for the instance")
    name: StrictStr = Field(description="Name of the instance")
    options: Optional[InstanceDocumentationOptions] = Field(
        default=None, description="Database instance specific options are requested via this field"
    )
    storage: Optional[InstanceDocumentationStorage] = Field(default=None, description="Storage for the instance")
    version: Optional[StrictStr] = Field(default="2022", description="Version of the MSSQL Server")
    __properties: ClassVar[List[str]] = [
        "acl",
        "backupSchedule",
        "flavorId",
        "labels",
        "name",
        "options",
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
        """Create an instance of CreateInstancePayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict["storage"] = self.storage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateInstancePayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "acl": InstanceDocumentationACL.from_dict(obj["acl"]) if obj.get("acl") is not None else None,
                "backupSchedule": obj.get("backupSchedule"),
                "flavorId": obj.get("flavorId"),
                "labels": obj.get("labels"),
                "name": obj.get("name"),
                "options": (
                    InstanceDocumentationOptions.from_dict(obj["options"]) if obj.get("options") is not None else None
                ),
                "storage": (
                    InstanceDocumentationStorage.from_dict(obj["storage"]) if obj.get("storage") is not None else None
                ),
                "version": obj.get("version") if obj.get("version") is not None else "2022",
            }
        )
        return _obj
