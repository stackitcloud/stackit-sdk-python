# coding: utf-8

"""
    Resource Manager API

    API v2 to manage resource containers - organizations, folders, projects incl. labels  ### Resource Management STACKIT resource management handles the terms _Organization_, _Folder_, _Project_, _Label_, and the hierarchical structure between them. Technically, organizations,  folders, and projects are _Resource Containers_ to which a _Label_ can be attached to. The STACKIT _Resource Manager_ provides CRUD endpoints to query and to modify the state.  ### Organizations STACKIT organizations are the base element to create and to use cloud-resources. An organization is bound to one customer account. Organizations have a lifecycle. - Organizations are always the root node in resource hierarchy and do not have a parent  ### Projects STACKIT projects are needed to use cloud-resources. Projects serve as wrapper for underlying technical structures and processes. Projects have a lifecycle. Projects compared to folders may have different policies. - Projects are optional, but mandatory for cloud-resource usage - A project can be created having either an organization, or a folder as parent - A project must not have a project as parent - Project names under the same parent must not be unique - Root organization cannot be changed  ### Label STACKIT labels are key-value pairs including a resource container reference. Labels can be defined and attached freely to resource containers by which resources can be organized and queried. - Policy-based, immutable labels may exists

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Annotated, Self


class ListOrganizationContainersResponse(BaseModel):
    """
    ListOrganizationContainersResponse
    """

    cursor: StrictStr = Field(
        description="A pagination cursor is returned on the first call of the pagination process. If given, it will start from the end of the previous position. If not given, a new pagination is started."
    )
    items: List[Optional[Dict[str, Any]]]
    limit: Union[
        Annotated[float, Field(le=100, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]
    ] = Field(
        description="The maximum number of projects to return in the response. If not present, an appropriate default will be used."
    )
    __properties: ClassVar[List[str]] = ["cursor", "items", "limit"]

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
        """Create an instance of ListOrganizationContainersResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict["items"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListOrganizationContainersResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cursor": obj.get("cursor"),
                "items": [AnyOf.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
                "limit": obj.get("limit") if obj.get("limit") is not None else 50,
            }
        )
        return _obj
