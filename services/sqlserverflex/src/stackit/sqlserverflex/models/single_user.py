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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing_extensions import Self


class SingleUser(BaseModel):
    """
    SingleUser
    """

    default_database: Optional[StrictStr] = None
    host: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    port: Optional[StrictInt] = None
    roles: Optional[List[StrictStr]] = None
    uri: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "default_database",
        "host",
        "id",
        "password",
        "port",
        "roles",
        "uri",
        "username",
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
        """Create an instance of SingleUser from a JSON string"""
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
        """Create an instance of SingleUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "default_database": obj.get("default_database"),
                "host": obj.get("host"),
                "id": obj.get("id"),
                "password": obj.get("password"),
                "port": obj.get("port"),
                "roles": obj.get("roles"),
                "uri": obj.get("uri"),
                "username": obj.get("username"),
            }
        )
        return _obj
