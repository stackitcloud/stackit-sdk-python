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
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing_extensions import Annotated, Self


class ImageShareConsumer(BaseModel):
    """
    The details of an Image share consumer.
    """

    consumer_project_id: Optional[Annotated[str, Field(min_length=36, strict=True, max_length=36)]] = Field(
        default=None, description="Universally Unique Identifier (UUID).", alias="consumerProjectId"
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Date-time when resource was created.", alias="createdAt"
    )
    image_id: Optional[Annotated[str, Field(min_length=36, strict=True, max_length=36)]] = Field(
        default=None, description="Universally Unique Identifier (UUID).", alias="imageId"
    )
    updated_at: Optional[datetime] = Field(
        default=None, description="Date-time when resource was last updated.", alias="updatedAt"
    )
    __properties: ClassVar[List[str]] = ["consumerProjectId", "createdAt", "imageId", "updatedAt"]

    @field_validator("consumer_project_id")
    def consumer_project_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(
                r"must validate the regular expression /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/"
            )
        return value

    @field_validator("image_id")
    def image_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(
                r"must validate the regular expression /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/"
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
        """Create an instance of ImageShareConsumer from a JSON string"""
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
        """
        excluded_fields: Set[str] = set(
            [
                "consumer_project_id",
                "created_at",
                "image_id",
                "updated_at",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImageShareConsumer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "consumerProjectId": obj.get("consumerProjectId"),
                "createdAt": obj.get("createdAt"),
                "imageId": obj.get("imageId"),
                "updatedAt": obj.get("updatedAt"),
            }
        )
        return _obj
