# coding: utf-8

"""
    STACKIT Opensearch API

    The STACKIT Opensearch API provides endpoints to list service offerings, manage service instances and service credentials within STACKIT portal projects.

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing_extensions import Self


class GetMetricsResponse(BaseModel):
    """
    GetMetricsResponse
    """

    cpu_idle_time: Optional[StrictInt] = Field(default=None, alias="cpuIdleTime")
    cpu_load_percent: Union[StrictFloat, StrictInt] = Field(alias="cpuLoadPercent")
    cpu_system_time: Optional[StrictInt] = Field(default=None, alias="cpuSystemTime")
    cpu_user_time: Optional[StrictInt] = Field(default=None, alias="cpuUserTime")
    disk_ephemeral_total: StrictInt = Field(alias="diskEphemeralTotal")
    disk_ephemeral_used: StrictInt = Field(alias="diskEphemeralUsed")
    disk_persistent_total: StrictInt = Field(alias="diskPersistentTotal")
    disk_persistent_used: StrictInt = Field(alias="diskPersistentUsed")
    load1: Union[StrictFloat, StrictInt]
    load15: Union[StrictFloat, StrictInt]
    load5: Union[StrictFloat, StrictInt]
    memory_total: StrictInt = Field(alias="memoryTotal")
    memory_used: StrictInt = Field(alias="memoryUsed")
    parachute_disk_ephemeral_activated: StrictBool = Field(alias="parachuteDiskEphemeralActivated")
    parachute_disk_ephemeral_total: StrictInt = Field(alias="parachuteDiskEphemeralTotal")
    parachute_disk_ephemeral_used: StrictInt = Field(alias="parachuteDiskEphemeralUsed")
    parachute_disk_ephemeral_used_percent: StrictInt = Field(alias="parachuteDiskEphemeralUsedPercent")
    parachute_disk_ephemeral_used_threshold: StrictInt = Field(alias="parachuteDiskEphemeralUsedThreshold")
    parachute_disk_persistent_activated: StrictBool = Field(alias="parachuteDiskPersistentActivated")
    parachute_disk_persistent_total: StrictInt = Field(alias="parachuteDiskPersistentTotal")
    parachute_disk_persistent_used: StrictInt = Field(alias="parachuteDiskPersistentUsed")
    parachute_disk_persistent_used_percent: StrictInt = Field(alias="parachuteDiskPersistentUsedPercent")
    parachute_disk_persistent_used_threshold: StrictInt = Field(alias="parachuteDiskPersistentUsedThreshold")
    __properties: ClassVar[List[str]] = [
        "cpuIdleTime",
        "cpuLoadPercent",
        "cpuSystemTime",
        "cpuUserTime",
        "diskEphemeralTotal",
        "diskEphemeralUsed",
        "diskPersistentTotal",
        "diskPersistentUsed",
        "load1",
        "load15",
        "load5",
        "memoryTotal",
        "memoryUsed",
        "parachuteDiskEphemeralActivated",
        "parachuteDiskEphemeralTotal",
        "parachuteDiskEphemeralUsed",
        "parachuteDiskEphemeralUsedPercent",
        "parachuteDiskEphemeralUsedThreshold",
        "parachuteDiskPersistentActivated",
        "parachuteDiskPersistentTotal",
        "parachuteDiskPersistentUsed",
        "parachuteDiskPersistentUsedPercent",
        "parachuteDiskPersistentUsedThreshold",
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
        """Create an instance of GetMetricsResponse from a JSON string"""
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
        """Create an instance of GetMetricsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cpuIdleTime": obj.get("cpuIdleTime"),
                "cpuLoadPercent": obj.get("cpuLoadPercent"),
                "cpuSystemTime": obj.get("cpuSystemTime"),
                "cpuUserTime": obj.get("cpuUserTime"),
                "diskEphemeralTotal": obj.get("diskEphemeralTotal"),
                "diskEphemeralUsed": obj.get("diskEphemeralUsed"),
                "diskPersistentTotal": obj.get("diskPersistentTotal"),
                "diskPersistentUsed": obj.get("diskPersistentUsed"),
                "load1": obj.get("load1"),
                "load15": obj.get("load15"),
                "load5": obj.get("load5"),
                "memoryTotal": obj.get("memoryTotal"),
                "memoryUsed": obj.get("memoryUsed"),
                "parachuteDiskEphemeralActivated": obj.get("parachuteDiskEphemeralActivated"),
                "parachuteDiskEphemeralTotal": obj.get("parachuteDiskEphemeralTotal"),
                "parachuteDiskEphemeralUsed": obj.get("parachuteDiskEphemeralUsed"),
                "parachuteDiskEphemeralUsedPercent": obj.get("parachuteDiskEphemeralUsedPercent"),
                "parachuteDiskEphemeralUsedThreshold": obj.get("parachuteDiskEphemeralUsedThreshold"),
                "parachuteDiskPersistentActivated": obj.get("parachuteDiskPersistentActivated"),
                "parachuteDiskPersistentTotal": obj.get("parachuteDiskPersistentTotal"),
                "parachuteDiskPersistentUsed": obj.get("parachuteDiskPersistentUsed"),
                "parachuteDiskPersistentUsedPercent": obj.get("parachuteDiskPersistentUsedPercent"),
                "parachuteDiskPersistentUsedThreshold": obj.get("parachuteDiskPersistentUsedThreshold"),
            }
        )
        return _obj
