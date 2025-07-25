# coding: utf-8

"""
    STACKIT Observability API

    API endpoints for Observability on STACKIT

    The version of the OpenAPI document: 1.1.1
    Contact: stackit-argus@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing_extensions import Annotated, Self

from stackit.observability.models.create_alert_config_route_payload_routes_inner import (
    CreateAlertConfigRoutePayloadRoutesInner,
)


class UpdateAlertConfigRoutePayload(BaseModel):
    """
    The root node of the routing tree.
    """  # noqa: E501

    var_continue: Optional[StrictBool] = Field(
        default=False,
        description="Whether an alert should continue matching subsequent sibling nodes.",
        alias="continue",
    )
    group_by: Optional[List[Annotated[str, Field(min_length=1, strict=True, max_length=200)]]] = Field(
        default=None,
        description="The labels by which incoming alerts are grouped together. For example, multiple alerts coming in for cluster=A and alertname=LatencyHigh would be batched into a single group. To aggregate by all possible labels use the special value '...' as the sole label name, for example: group_by: ['...']. This effectively disables aggregation entirely, passing through all alerts as-is. This is unlikely to be what you want, unless you have a very low alert volume or your upstream notification system performs its own grouping.",
        alias="groupBy",
    )
    group_interval: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=8)]] = Field(
        default="5m",
        description="How long to wait before sending a notification about new alerts that are added to a group of alerts for which an initial notification has already been sent. (Usually ~5m or more.) `Additional Validators:` * must be a valid time format",
        alias="groupInterval",
    )
    group_wait: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=8)]] = Field(
        default="30s",
        description="How long to initially wait to send a notification for a group of alerts. Allows to wait for an inhibiting alert to arrive or collect more initial alerts for the same group. (Usually ~0s to few minutes.) `Additional Validators:` * must be a valid time format",
        alias="groupWait",
    )
    match: Optional[Dict[str, Any]] = Field(
        default=None,
        description="map of key:value. A set of equality matchers an alert has to fulfill to match the node.  `Additional Validators:` * should not contain more than 5 keys * each key and value should not be longer than 200 characters * key and values should only include the characters: a-zA-Z0-9_./@&?:-",
    )
    match_re: Optional[Dict[str, Any]] = Field(
        default=None,
        description="map of key:value. A set of regex-matchers an alert has to fulfill to match the node.  `Additional Validators:` * should not contain more than 5 keys * each key and value should not be longer than 200 characters",
        alias="matchRe",
    )
    matchers: Optional[List[Annotated[str, Field(min_length=1, strict=True, max_length=200)]]] = Field(
        default=None,
        description="A list of matchers that an alert has to fulfill to match the node. A matcher is a string with a syntax inspired by PromQL and OpenMetrics. The syntax of a matcher consists of three tokens: * A valid Prometheus label name. * One of =, !=, =~, or !~. = means equals, != means that the strings are not equal, =~ is used for equality of regex expressions and !~ is used for un-equality of regex expressions. They have the same meaning as known from PromQL selectors. * A UTF-8 string, which may be enclosed in double quotes. Before or after each token, there may be any amount of whitespace. `Additional Validators:` * should not contain more than 5 keys * each key and value should not be longer than 200 characters",
    )
    receiver: Annotated[str, Field(min_length=1, strict=True, max_length=200)] = Field(
        description="Receiver that should be one item of receivers `Additional Validators:` * must be a in name of receivers"
    )
    repeat_interval: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=8)]] = Field(
        default="4h",
        description="How long to wait before sending a notification again if it has already been sent successfully for an alert. (Usually ~3h or more). `Additional Validators:` * must be a valid time format",
        alias="repeatInterval",
    )
    routes: Optional[List[CreateAlertConfigRoutePayloadRoutesInner]] = Field(
        default=None, description="Zero or more child routes."
    )
    __properties: ClassVar[List[str]] = [
        "continue",
        "groupBy",
        "groupInterval",
        "groupWait",
        "match",
        "matchRe",
        "matchers",
        "receiver",
        "repeatInterval",
        "routes",
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
        """Create an instance of UpdateAlertConfigRoutePayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in routes (list)
        _items = []
        if self.routes:
            for _item in self.routes:
                if _item:
                    _items.append(_item.to_dict())
            _dict["routes"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateAlertConfigRoutePayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "continue": obj.get("continue") if obj.get("continue") is not None else False,
                "groupBy": obj.get("groupBy"),
                "groupInterval": obj.get("groupInterval") if obj.get("groupInterval") is not None else "5m",
                "groupWait": obj.get("groupWait") if obj.get("groupWait") is not None else "30s",
                "match": obj.get("match"),
                "matchRe": obj.get("matchRe"),
                "matchers": obj.get("matchers"),
                "receiver": obj.get("receiver"),
                "repeatInterval": obj.get("repeatInterval") if obj.get("repeatInterval") is not None else "4h",
                "routes": (
                    [CreateAlertConfigRoutePayloadRoutesInner.from_dict(_item) for _item in obj["routes"]]
                    if obj.get("routes") is not None
                    else None
                ),
            }
        )
        return _obj
