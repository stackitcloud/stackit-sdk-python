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
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing_extensions import Annotated, Self


class MachineType(BaseModel):
    """
    Machine Type. Filterable Fields: name, ram, vcpus, disk, extraSpecs.
    """

    description: Optional[Annotated[str, Field(strict=True, max_length=127)]] = Field(
        default=None, description="Description Object. Allows string up to 127 Characters."
    )
    disk: StrictInt = Field(description="Size in Gigabyte.")
    extra_specs: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Properties to control certain aspects or scheduling behavior for an object.",
        alias="extraSpecs",
    )
    name: Annotated[str, Field(strict=True, max_length=63)] = Field(
        description="The name for a General Object. Matches Names and also UUIDs."
    )
    ram: StrictInt = Field(description="Size in Megabyte.")
    vcpus: Annotated[int, Field(strict=True, ge=1)] = Field(description="The number of virtual CPUs of a server.")
    __properties: ClassVar[List[str]] = ["description", "disk", "extraSpecs", "name", "ram", "vcpus"]

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
        """Create an instance of MachineType from a JSON string"""
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
        """Create an instance of MachineType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "description": obj.get("description"),
                "disk": obj.get("disk"),
                "extraSpecs": obj.get("extraSpecs"),
                "name": obj.get("name"),
                "ram": obj.get("ram"),
                "vcpus": obj.get("vcpus"),
            }
        )
        return _obj
