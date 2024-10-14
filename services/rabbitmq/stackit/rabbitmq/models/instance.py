# coding: utf-8

"""
    STACKIT RabbitMQ API

    The STACKIT RabbitMQ API provides endpoints to list service offerings, manage service instances and service credentials within STACKIT portal projects.

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self

from stackit.rabbitmq.models.instance_last_operation import InstanceLastOperation


class Instance(BaseModel):
    """
    Instance
    """

    cf_guid: StrictStr = Field(alias="cfGuid")
    cf_organization_guid: StrictStr = Field(alias="cfOrganizationGuid")
    cf_space_guid: StrictStr = Field(alias="cfSpaceGuid")
    dashboard_url: StrictStr = Field(alias="dashboardUrl")
    image_url: StrictStr = Field(alias="imageUrl")
    instance_id: Optional[StrictStr] = Field(default=None, alias="instanceId")
    last_operation: InstanceLastOperation = Field(alias="lastOperation")
    name: StrictStr
    offering_name: StrictStr = Field(alias="offeringName")
    offering_version: StrictStr = Field(alias="offeringVersion")
    parameters: Dict[str, Any]
    plan_id: StrictStr = Field(alias="planId")
    plan_name: StrictStr = Field(alias="planName")
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "cfGuid",
        "cfOrganizationGuid",
        "cfSpaceGuid",
        "dashboardUrl",
        "imageUrl",
        "instanceId",
        "lastOperation",
        "name",
        "offeringName",
        "offeringVersion",
        "parameters",
        "planId",
        "planName",
        "status",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["active", "failed", "stopped", "creating", "deleting", "updating"]):
            raise ValueError(
                "must be one of enum values ('active', 'failed', 'stopped', 'creating', 'deleting', 'updating')"
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
        """Create an instance of Instance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of last_operation
        if self.last_operation:
            _dict["lastOperation"] = self.last_operation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Instance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cfGuid": obj.get("cfGuid"),
                "cfOrganizationGuid": obj.get("cfOrganizationGuid"),
                "cfSpaceGuid": obj.get("cfSpaceGuid"),
                "dashboardUrl": obj.get("dashboardUrl"),
                "imageUrl": obj.get("imageUrl"),
                "instanceId": obj.get("instanceId"),
                "lastOperation": (
                    InstanceLastOperation.from_dict(obj["lastOperation"])
                    if obj.get("lastOperation") is not None
                    else None
                ),
                "name": obj.get("name"),
                "offeringName": obj.get("offeringName"),
                "offeringVersion": obj.get("offeringVersion"),
                "parameters": obj.get("parameters"),
                "planId": obj.get("planId"),
                "planName": obj.get("planName"),
                "status": obj.get("status"),
            }
        )
        return _obj
