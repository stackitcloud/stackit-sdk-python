# coding: utf-8

"""
    STACKIT Observability API

    API endpoints for Observability on STACKIT

    The version of the OpenAPI document: 1.1.1
    Contact: stackit-argus@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated, Self


class UpdateAlertgroupsRequestInnerRulesInner(BaseModel):
    """
    Alert rule. `Additional Validators:` * total config (all alert groups/rules) should not be bigger than 500000 characters as string since this the limitation of prometheus.
    """

    alert: Annotated[str, Field(min_length=1, strict=True, max_length=200)] = Field(
        description="The name of the alert. `Additional Validators:` * is the identifier and so unique in the group * should only include the characters: a-zA-Z0-9-"
    )
    annotations: Optional[Dict[str, Any]] = Field(
        default=None,
        description="map of key:value. Annotations to add to each alert. `Additional Validators:` * should not contain more than 5 keys * each key and value should not be longer than 200 characters",
    )
    expr: Annotated[str, Field(min_length=1, strict=True, max_length=600)] = Field(
        description="The PromQL expression to evaluate. Every evaluation cycle this is evaluated at the current time, and all resultant time series become pending/firing alerts."
    )
    var_for: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=8)]] = Field(
        default="0s",
        description="Alerts are considered firing once they have been returned for this long. Alerts which have not yet fired for long enough are considered pending. `Additional Validators:` * must be a valid time string",
        alias="for",
    )
    labels: Optional[Dict[str, Any]] = Field(
        default=None,
        description="map of key:value. Labels to add or overwrite for each alert. `Additional Validators:` * should not contain more than 10 keys * each key and value should not be longer than 200 characters",
    )
    __properties: ClassVar[List[str]] = ["alert", "annotations", "expr", "for", "labels"]

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
        """Create an instance of UpdateAlertgroupsRequestInnerRulesInner from a JSON string"""
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
        """Create an instance of UpdateAlertgroupsRequestInnerRulesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "alert": obj.get("alert"),
                "annotations": obj.get("annotations"),
                "expr": obj.get("expr"),
                "for": obj.get("for") if obj.get("for") is not None else "0s",
                "labels": obj.get("labels"),
            }
        )
        return _obj
