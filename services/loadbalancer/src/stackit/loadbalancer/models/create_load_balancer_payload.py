# coding: utf-8

"""
    Load Balancer API

    This API offers an interface to provision and manage load balancing servers in your STACKIT project. It also has the possibility of pooling target servers for load balancing purposes.  For each load balancer provided, two VMs are deployed in your OpenStack project subject to a fee.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing_extensions import Annotated, Self

from stackit.loadbalancer.models.listener import Listener
from stackit.loadbalancer.models.load_balancer_error import LoadBalancerError
from stackit.loadbalancer.models.load_balancer_options import LoadBalancerOptions
from stackit.loadbalancer.models.network import Network
from stackit.loadbalancer.models.security_group import SecurityGroup
from stackit.loadbalancer.models.target_pool import TargetPool


class CreateLoadBalancerPayload(BaseModel):
    """
    CreateLoadBalancerPayload
    """  # noqa: E501

    disable_target_security_group_assignment: Optional[StrictBool] = Field(
        default=None,
        description="Disable target security group assignemt to allow targets outside of the given network. Connectivity to targets need to be ensured by the customer, including routing and Security Groups (targetSecurityGroup can be assigned). Not changeable after creation.",
        alias="disableTargetSecurityGroupAssignment",
    )
    errors: Optional[List[LoadBalancerError]] = Field(
        default=None, description="Reports all errors a load balancer has."
    )
    external_address: Optional[StrictStr] = Field(
        default=None,
        description="External load balancer IP address where this load balancer is exposed. Not changeable after creation.",
        alias="externalAddress",
    )
    listeners: Optional[List[Listener]] = Field(
        default=None,
        description="There is a maximum listener count of 20.  Port and protocol limitations:  - UDP listeners cannot have the same port. - TCP-derived listeners cannot have the same port. A TCP-derived listener is any listener that listens on a TCP port. As of now those are: TCP, TCP_PROXY, and PROTOCOL_TLS_PASSTHROUGH. The only exception is, if all listeners for the same port are PROTOCOL_TLS_PASSTHROUGH. - PROTOCOL_TLS_PASSTHROUGH listeners cannot have the same port and at least one common domain name. - PROTOCOL_TLS_PASSTHROUGH listeners can have the same domain name and different ports though (e.g. ports 443 and 8443 for domain example.com). - PROTOCOL_TLS_PASSTHROUGH listeners without a domain name serve as a default listener and you can have only one default listener. ",
    )
    load_balancer_security_group: Optional[SecurityGroup] = Field(
        default=None,
        description="Security Group permitting network traffic from the LoadBalancer to the targets. Useful when disableTargetSecurityGroupAssignment=true to manually assign target security groups to targets.",
        alias="loadBalancerSecurityGroup",
    )
    name: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Load balancer name. Not changeable after creation."
    )
    networks: Optional[List[Network]] = Field(
        default=None,
        description="List of networks that listeners and targets reside in. Currently limited to one. Not changeable after creation.",
    )
    options: Optional[LoadBalancerOptions] = None
    plan_id: Optional[StrictStr] = Field(
        default=None,
        description="Service Plan configures the size of the Load Balancer. Currently supported plans are p10, p50, p250 and p750. This list can change in the future where plan ids will be removed and new plans by added. That is the reason this is not an enum.",
        alias="planId",
    )
    private_address: Optional[StrictStr] = Field(
        default=None,
        description="Transient private load balancer IP address that can change any time.",
        alias="privateAddress",
    )
    region: Optional[StrictStr] = Field(default=None, description="Region of the LoadBalancer")
    status: Optional[StrictStr] = None
    target_pools: Optional[List[TargetPool]] = Field(
        default=None,
        description="List of all target pools which will be used in the load balancer. Limited to 20.",
        alias="targetPools",
    )
    target_security_group: Optional[SecurityGroup] = Field(
        default=None,
        description="Security Group that allows the targets to receive traffic from the LoadBalancer. Useful when disableTargetSecurityGroupAssignment=true to manually assign target security groups to targets.",
        alias="targetSecurityGroup",
    )
    version: Optional[StrictStr] = Field(
        default=None,
        description="Load balancer resource version. Must be empty or unset for creating load balancers, non-empty for updating load balancers. Semantics: While retrieving load balancers, this is the current version of this load balancer resource that changes during updates of the load balancers. On updates this field specified the load balancer version you calculated your update for instead of the future version to enable concurrency safe updates. Update calls will then report the new version in their result as you would see with a load balancer retrieval call later. There exist no total order of the version, so you can only compare it for equality, but not for less/greater than another version. Since the creation of load balancer is always intended to create the first version of it, there should be no existing version. That's why this field must by empty of not present in that case.",
    )
    __properties: ClassVar[List[str]] = [
        "disableTargetSecurityGroupAssignment",
        "errors",
        "externalAddress",
        "listeners",
        "loadBalancerSecurityGroup",
        "name",
        "networks",
        "options",
        "planId",
        "privateAddress",
        "region",
        "status",
        "targetPools",
        "targetSecurityGroup",
        "version",
    ]

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-z](?:(?:[0-9a-z]|-){0,61}[0-9a-z])?$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-z](?:(?:[0-9a-z]|-){0,61}[0-9a-z])?$/")
        return value

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            ["STATUS_UNSPECIFIED", "STATUS_PENDING", "STATUS_READY", "STATUS_ERROR", "STATUS_TERMINATING"]
        ):
            raise ValueError(
                "must be one of enum values ('STATUS_UNSPECIFIED', 'STATUS_PENDING', 'STATUS_READY', 'STATUS_ERROR', 'STATUS_TERMINATING')"
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
        """Create an instance of CreateLoadBalancerPayload from a JSON string"""
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
                "errors",
                "load_balancer_security_group",
                "private_address",
                "region",
                "status",
                "target_security_group",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict["errors"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in listeners (list)
        _items = []
        if self.listeners:
            for _item in self.listeners:
                if _item:
                    _items.append(_item.to_dict())
            _dict["listeners"] = _items
        # override the default output from pydantic by calling `to_dict()` of load_balancer_security_group
        if self.load_balancer_security_group:
            _dict["loadBalancerSecurityGroup"] = self.load_balancer_security_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in networks (list)
        _items = []
        if self.networks:
            for _item in self.networks:
                if _item:
                    _items.append(_item.to_dict())
            _dict["networks"] = _items
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in target_pools (list)
        _items = []
        if self.target_pools:
            for _item in self.target_pools:
                if _item:
                    _items.append(_item.to_dict())
            _dict["targetPools"] = _items
        # override the default output from pydantic by calling `to_dict()` of target_security_group
        if self.target_security_group:
            _dict["targetSecurityGroup"] = self.target_security_group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateLoadBalancerPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "disableTargetSecurityGroupAssignment": obj.get("disableTargetSecurityGroupAssignment"),
                "errors": (
                    [LoadBalancerError.from_dict(_item) for _item in obj["errors"]]
                    if obj.get("errors") is not None
                    else None
                ),
                "externalAddress": obj.get("externalAddress"),
                "listeners": (
                    [Listener.from_dict(_item) for _item in obj["listeners"]]
                    if obj.get("listeners") is not None
                    else None
                ),
                "loadBalancerSecurityGroup": (
                    SecurityGroup.from_dict(obj["loadBalancerSecurityGroup"])
                    if obj.get("loadBalancerSecurityGroup") is not None
                    else None
                ),
                "name": obj.get("name"),
                "networks": (
                    [Network.from_dict(_item) for _item in obj["networks"]] if obj.get("networks") is not None else None
                ),
                "options": LoadBalancerOptions.from_dict(obj["options"]) if obj.get("options") is not None else None,
                "planId": obj.get("planId"),
                "privateAddress": obj.get("privateAddress"),
                "region": obj.get("region"),
                "status": obj.get("status"),
                "targetPools": (
                    [TargetPool.from_dict(_item) for _item in obj["targetPools"]]
                    if obj.get("targetPools") is not None
                    else None
                ),
                "targetSecurityGroup": (
                    SecurityGroup.from_dict(obj["targetSecurityGroup"])
                    if obj.get("targetSecurityGroup") is not None
                    else None
                ),
                "version": obj.get("version"),
            }
        )
        return _obj
