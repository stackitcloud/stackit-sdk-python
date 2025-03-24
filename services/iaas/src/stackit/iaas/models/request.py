# coding: utf-8

"""
    IaaS-API

    This API allows you to create and modify IaaS resources.

    The version of the OpenAPI document: 1
    Contact: stackit-iaas@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from stackit.iaas.models.request_resource import RequestResource


class Request(BaseModel):
    """
    Object that represents a request.
    """

    details: Optional[StrictStr] = None
    request_action: StrictStr = Field(
        description="Object that represents a resource action. Possible values: `CREATE`, `DELETE`, `UPDATE`.",
        alias="requestAction",
    )
    request_id: Annotated[str, Field(min_length=36, strict=True, max_length=36)] = Field(
        description="Identifier (ID) representing a single API request.", alias="requestId"
    )
    request_type: StrictStr = Field(
        description="Object that represents a resource type. Possible values: `BACKUP`, `IMAGE`, `NETWORK`, `NETWORKAREA`, `NIC`, `PROJECT`, `ROUTE`, `SERVER`, `SERVICEACCOUNT`, `SNAPSHOT`, `VIRTUALIP`, `VOLUME`.",
        alias="requestType",
    )
    resources: List[RequestResource]
    status: StrictStr = Field(
        description="The state of a resource object. Possible values: `CREATING`, `CREATED`, `DELETING`, `DELETED`, `FAILED`, `UPDATED`, `UPDATING`."
    )
    __properties: ClassVar[List[str]] = ["details", "requestAction", "requestId", "requestType", "resources", "status"]

    @field_validator("request_id")
    def request_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^req-[0-9a-f]{32}$", value):
            raise ValueError(r"must validate the regular expression /^req-[0-9a-f]{32}$/")
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
        """Create an instance of Request from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict["resources"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "details": obj.get("details"),
                "requestAction": obj.get("requestAction"),
                "requestId": obj.get("requestId"),
                "requestType": obj.get("requestType"),
                "resources": (
                    [RequestResource.from_dict(_item) for _item in obj["resources"]]
                    if obj.get("resources") is not None
                    else None
                ),
                "status": obj.get("status"),
            }
        )
        return _obj
