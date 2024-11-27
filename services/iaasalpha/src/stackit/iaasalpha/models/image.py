# coding: utf-8

"""
    IaaS-API

    This API allows you to create and modify IaaS resources.

    The version of the OpenAPI document: 1alpha1
    Contact: stackit-iaas@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
import re
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing_extensions import Annotated, Self

from stackit.iaasalpha.models.image_checksum import ImageChecksum
from stackit.iaasalpha.models.image_config import ImageConfig


class Image(BaseModel):
    """
    Object that represents an Image and its parameters. Used for Creating and returning (get/list).
    """

    checksum: Optional[ImageChecksum] = None
    config: Optional[ImageConfig] = None
    created_at: Optional[datetime] = Field(
        default=None, description="Date-time when resource was created.", alias="createdAt"
    )
    disk_format: StrictStr = Field(description="Object that represents a disk format.", alias="diskFormat")
    id: Optional[Annotated[str, Field(min_length=36, strict=True, max_length=36)]] = Field(
        default=None, description="Universally Unique Identifier (UUID)."
    )
    labels: Optional[Dict[str, Any]] = Field(
        default=None, description="Object that represents the labels of an object."
    )
    min_disk_size: Optional[StrictInt] = Field(default=None, description="Size in Gigabyte.", alias="minDiskSize")
    min_ram: Optional[StrictInt] = Field(default=None, description="Size in Megabyte.", alias="minRam")
    name: Annotated[str, Field(strict=True, max_length=63)] = Field(
        description="The name for a General Object. Matches Names and also UUIDs."
    )
    protected: Optional[StrictBool] = None
    scope: Optional[StrictStr] = Field(default=None, description="Scope of an Image.")
    status: Optional[StrictStr] = Field(default=None, description="The status of an image object.")
    updated_at: Optional[datetime] = Field(
        default=None, description="Date-time when resource was last updated.", alias="updatedAt"
    )
    __properties: ClassVar[List[str]] = [
        "checksum",
        "config",
        "createdAt",
        "diskFormat",
        "id",
        "labels",
        "minDiskSize",
        "minRam",
        "name",
        "protected",
        "scope",
        "status",
        "updatedAt",
    ]

    @field_validator("id")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(
                r"must validate the regular expression /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/"
            )
        return value

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[A-Za-z0-9]+((-|_|\s|\.)[A-Za-z0-9]+)*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9]+((-|_|\s|\.)[A-Za-z0-9]+)*$/")
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
        """Create an instance of Image from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "checksum",
                "created_at",
                "id",
                "scope",
                "status",
                "updated_at",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of checksum
        if self.checksum:
            _dict["checksum"] = self.checksum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict["config"] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Image from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "checksum": ImageChecksum.from_dict(obj["checksum"]) if obj.get("checksum") is not None else None,
                "config": ImageConfig.from_dict(obj["config"]) if obj.get("config") is not None else None,
                "createdAt": obj.get("createdAt"),
                "diskFormat": obj.get("diskFormat"),
                "id": obj.get("id"),
                "labels": obj.get("labels"),
                "minDiskSize": obj.get("minDiskSize"),
                "minRam": obj.get("minRam"),
                "name": obj.get("name"),
                "protected": obj.get("protected"),
                "scope": obj.get("scope"),
                "status": obj.get("status"),
                "updatedAt": obj.get("updatedAt"),
            }
        )
        return _obj
