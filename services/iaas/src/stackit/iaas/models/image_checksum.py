# coding: utf-8

"""
    IaaS-API

    This API allows you to create and modify IaaS resources.

    The version of the OpenAPI document: 1
    Contact: stackit-iaas@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self


class ImageChecksum(BaseModel):
    """
    Representation of an image checksum.
    """  # noqa: E501

    algorithm: StrictStr = Field(description="Algorithm for the checksum of the image data.")
    digest: Annotated[str, Field(strict=True)] = Field(description="Hexdigest of the checksum of the image data.")
    __properties: ClassVar[List[str]] = ["algorithm", "digest"]

    @field_validator("digest")
    def digest_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9a-f]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]+$/")
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
        """Create an instance of ImageChecksum from a JSON string"""
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
        """Create an instance of ImageChecksum from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({"algorithm": obj.get("algorithm"), "digest": obj.get("digest")})
        return _obj
