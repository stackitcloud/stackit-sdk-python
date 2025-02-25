# coding: utf-8

"""
    IaaS-API

    This API allows you to create and modify IaaS resources.

    The version of the OpenAPI document: 1beta1
    Contact: stackit-iaas@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing_extensions import Annotated, Self

from stackit.iaas.models.image_config import ImageConfig


class UpdateVolumePayload(BaseModel):
    """
    Object that represents an update request body of a  volume.
    """

    bootable: Optional[StrictBool] = Field(default=None, description="Indicates if a volume is bootable.")
    description: Optional[Annotated[str, Field(strict=True, max_length=127)]] = Field(
        default=None, description="Description Object. Allows string up to 127 Characters."
    )
    image_config: Optional[ImageConfig] = Field(default=None, alias="imageConfig")
    labels: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Object that represents the labels of an object. Regex for keys: `^[a-z]((-|_|[a-z0-9])){0,62}$`. Regex for values: `^(-|_|[a-z0-9]){0,63}$`.",
    )
    name: Optional[Annotated[str, Field(strict=True, max_length=63)]] = Field(
        default=None, description="The name for a General Object. Matches Names and also UUIDs."
    )
    __properties: ClassVar[List[str]] = ["bootable", "description", "imageConfig", "labels", "name"]

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of UpdateVolumePayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of image_config
        if self.image_config:
            _dict["imageConfig"] = self.image_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateVolumePayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "bootable": obj.get("bootable"),
                "description": obj.get("description"),
                "imageConfig": (
                    ImageConfig.from_dict(obj["imageConfig"]) if obj.get("imageConfig") is not None else None
                ),
                "labels": obj.get("labels"),
                "name": obj.get("name"),
            }
        )
        return _obj
