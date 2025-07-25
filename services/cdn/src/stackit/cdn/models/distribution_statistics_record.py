# coding: utf-8

"""
    CDN API

    API used to create and manage your CDN distributions.

    The version of the OpenAPI document: 1beta.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing_extensions import Self

from stackit.cdn.models.distribution_statistics_record_regions import (
    DistributionStatisticsRecordRegions,
)


class DistributionStatisticsRecord(BaseModel):
    """
    Aggregated statistics of a distribution during a time interval
    """  # noqa: E501

    cached_requests: StrictInt = Field(description="Number of cached requests that were served", alias="cachedRequests")
    total_requests: StrictInt = Field(description="Total number of requests that were served", alias="totalRequests")
    total_traffic_bytes: StrictInt = Field(
        description="Total traffic in bytes that occurred during the time interval", alias="totalTrafficBytes"
    )
    end: datetime = Field(description="Exclusive end of the time interval the statistics refer to")
    regions: DistributionStatisticsRecordRegions
    start: datetime = Field(description="Start of the time interval the statistics refer to")
    __properties: ClassVar[List[str]] = [
        "cachedRequests",
        "totalRequests",
        "totalTrafficBytes",
        "end",
        "regions",
        "start",
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
        """Create an instance of DistributionStatisticsRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of regions
        if self.regions:
            _dict["regions"] = self.regions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DistributionStatisticsRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cachedRequests": obj.get("cachedRequests"),
                "totalRequests": obj.get("totalRequests"),
                "totalTrafficBytes": obj.get("totalTrafficBytes"),
                "end": obj.get("end"),
                "regions": (
                    DistributionStatisticsRecordRegions.from_dict(obj["regions"])
                    if obj.get("regions") is not None
                    else None
                ),
                "start": obj.get("start"),
            }
        )
        return _obj
