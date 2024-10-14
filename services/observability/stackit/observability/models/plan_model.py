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
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Annotated, Self


class PlanModel(BaseModel):
    """
    PlanModel
    """

    alert_matchers: StrictInt = Field(alias="alertMatchers")
    alert_receivers: StrictInt = Field(alias="alertReceivers")
    alert_rules: StrictInt = Field(alias="alertRules")
    amount: Optional[
        Union[
            Annotated[float, Field(le=10000000, strict=True, ge=0)],
            Annotated[int, Field(le=10000000, strict=True, ge=0)],
        ]
    ] = None
    bucket_size: Annotated[int, Field(strict=True, ge=0)] = Field(alias="bucketSize")
    description: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1000)]] = None
    grafana_global_dashboards: StrictInt = Field(alias="grafanaGlobalDashboards")
    grafana_global_orgs: StrictInt = Field(alias="grafanaGlobalOrgs")
    grafana_global_sessions: StrictInt = Field(alias="grafanaGlobalSessions")
    grafana_global_users: StrictInt = Field(alias="grafanaGlobalUsers")
    id: StrictStr
    logs_alert: StrictInt = Field(alias="logsAlert")
    logs_storage: StrictInt = Field(alias="logsStorage")
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=500)]] = None
    plan_id: StrictStr = Field(alias="planId")
    samples_per_scrape: StrictInt = Field(alias="samplesPerScrape")
    target_number: StrictInt = Field(alias="targetNumber")
    total_metric_samples: StrictInt = Field(alias="totalMetricSamples")
    traces_storage: StrictInt = Field(alias="tracesStorage")
    __properties: ClassVar[List[str]] = [
        "alertMatchers",
        "alertReceivers",
        "alertRules",
        "amount",
        "bucketSize",
        "description",
        "grafanaGlobalDashboards",
        "grafanaGlobalOrgs",
        "grafanaGlobalSessions",
        "grafanaGlobalUsers",
        "id",
        "logsAlert",
        "logsStorage",
        "name",
        "planId",
        "samplesPerScrape",
        "targetNumber",
        "totalMetricSamples",
        "tracesStorage",
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
        """Create an instance of PlanModel from a JSON string"""
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
        """Create an instance of PlanModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "alertMatchers": obj.get("alertMatchers"),
                "alertReceivers": obj.get("alertReceivers"),
                "alertRules": obj.get("alertRules"),
                "amount": obj.get("amount"),
                "bucketSize": obj.get("bucketSize"),
                "description": obj.get("description"),
                "grafanaGlobalDashboards": obj.get("grafanaGlobalDashboards"),
                "grafanaGlobalOrgs": obj.get("grafanaGlobalOrgs"),
                "grafanaGlobalSessions": obj.get("grafanaGlobalSessions"),
                "grafanaGlobalUsers": obj.get("grafanaGlobalUsers"),
                "id": obj.get("id"),
                "logsAlert": obj.get("logsAlert"),
                "logsStorage": obj.get("logsStorage"),
                "name": obj.get("name"),
                "planId": obj.get("planId"),
                "samplesPerScrape": obj.get("samplesPerScrape"),
                "targetNumber": obj.get("targetNumber"),
                "totalMetricSamples": obj.get("totalMetricSamples"),
                "tracesStorage": obj.get("tracesStorage"),
            }
        )
        return _obj
