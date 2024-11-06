# coding: utf-8

"""
    STACKIT Membership API

    The Membership API is used to manage memberships, roles and permissions of STACKIT resources, like projects, folders, organizations and other resources.

    The version of the OpenAPI document: 2.0
    Contact: SIT-STACKIT-Core-Platform-Security@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing_extensions import Annotated, Self

from stackit.membership.models.remove_role_request import RemoveRoleRequest


class RemoveRolesPayload(BaseModel):
    """
    RemoveRolesPayload
    """

    resource_type: Annotated[str, Field(strict=True)] = Field(alias="resourceType")
    roles: List[RemoveRoleRequest]
    __properties: ClassVar[List[str]] = ["resourceType", "roles"]

    @field_validator("resource_type")
    def resource_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z](?:-?[a-z]){1,63}$", value):
            raise ValueError(r"must validate the regular expression /^[a-z](?:-?[a-z]){1,63}$/")
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
        """Create an instance of RemoveRolesPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict["roles"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RemoveRolesPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "resourceType": obj.get("resourceType"),
                "roles": (
                    [RemoveRoleRequest.from_dict(_item) for _item in obj["roles"]]
                    if obj.get("roles") is not None
                    else None
                ),
            }
        )
        return _obj
