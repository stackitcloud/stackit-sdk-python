# coding: utf-8

"""
    Load Balancer API

    This API offers an interface to provision and manage load balancing servers in your STACKIT project. It also has the possibility of pooling target servers for load balancing purposes.  For each load balancer provided, two VMs are deployed in your OpenStack project subject to a fee.

    The version of the OpenAPI document: 1.7.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self


class LoadbalancerOptionMetrics(BaseModel):
    """
    LoadbalancerOptionMetrics
    """

    credentials_ref: Optional[StrictStr] = Field(
        default=None,
        description="Credentials reference for metrics. This reference is created via the observability create endpoint and the credential needs to contain the basic auth username and password for the metrics solution the push URL points to. Then this enables monitoring via remote write for the Load Balancer.",
        alias="credentialsRef",
    )
    push_url: Optional[StrictStr] = Field(
        default=None,
        description="The ARGUS/Prometheus remote write Push URL you want the metrics to be shipped to.",
        alias="pushUrl",
    )
    __properties: ClassVar[List[str]] = ["credentialsRef", "pushUrl"]

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
        """Create an instance of LoadbalancerOptionMetrics from a JSON string"""
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
        """Create an instance of LoadbalancerOptionMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({"credentialsRef": obj.get("credentialsRef"), "pushUrl": obj.get("pushUrl")})
        return _obj
