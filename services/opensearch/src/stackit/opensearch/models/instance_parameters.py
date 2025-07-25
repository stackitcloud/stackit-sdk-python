# coding: utf-8

"""
    STACKIT Opensearch API

    The STACKIT Opensearch API provides endpoints to list service offerings, manage service instances and service credentials within STACKIT portal projects.

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing_extensions import Annotated, Self


class InstanceParameters(BaseModel):
    """
    InstanceParameters
    """  # noqa: E501

    enable_monitoring: Optional[StrictBool] = False
    graphite: Optional[StrictStr] = Field(
        default=None,
        description="If you want to monitor your service with Graphite, you can set the custom parameter graphite. It expects the host and port where the Graphite metrics should be sent to.",
    )
    java_garbage_collector: Optional[StrictStr] = "UseG1GC"
    java_heapspace: Optional[Annotated[int, Field(strict=True, ge=256)]] = Field(
        default=None,
        description="Default: not set, 46% of available memory will be used. The amount of memory (in MB) allocated as heap by the JVM for OpenSearch.",
    )
    java_maxmetaspace: Optional[Annotated[int, Field(le=1024, strict=True, ge=256)]] = Field(
        default=512, description="The amount of memory (in MB) used by the JVM to store metadata for OpenSearch."
    )
    max_disk_threshold: Optional[StrictInt] = Field(
        default=80,
        description="This component monitors ephemeral and persistent disk usage. If one of these disk usages reaches the default configured threshold of 80%, the a9s Parachute stops all processes on that node.",
    )
    metrics_frequency: Optional[StrictInt] = Field(
        default=10, description="Frequency of metrics being emitted in seconds"
    )
    metrics_prefix: Optional[StrictStr] = Field(
        default=None,
        description="Depending on your graphite provider, you might need to prefix the metrics with a certain value, like an API key for example.",
    )
    monitoring_instance_id: Optional[StrictStr] = None
    plugins: Optional[List[StrictStr]] = Field(
        default=None,
        description="The plugins repository-s3 and repository-azure are enabled by default and cannot be disabled.",
    )
    sgw_acl: Optional[StrictStr] = Field(
        default=None,
        description="Comma separated list of IP networks in CIDR notation which are allowed to access this instance.",
    )
    syslog: Optional[List[StrictStr]] = None
    tls_ciphers: Optional[List[StrictStr]] = Field(
        default=None, description="Only Java format is supported.", alias="tls-ciphers"
    )
    tls_protocols: Optional[List[StrictStr]] = Field(default=None, alias="tls-protocols")
    __properties: ClassVar[List[str]] = [
        "enable_monitoring",
        "graphite",
        "java_garbage_collector",
        "java_heapspace",
        "java_maxmetaspace",
        "max_disk_threshold",
        "metrics_frequency",
        "metrics_prefix",
        "monitoring_instance_id",
        "plugins",
        "sgw_acl",
        "syslog",
        "tls-ciphers",
        "tls-protocols",
    ]

    @field_validator("java_garbage_collector")
    def java_garbage_collector_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["UseSerialGC", "UseParallelGC", "UseParallelOldGC", "UseG1GC"]):
            raise ValueError(
                "must be one of enum values ('UseSerialGC', 'UseParallelGC', 'UseParallelOldGC', 'UseG1GC')"
            )
        return value

    @field_validator("plugins")
    def plugins_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(["repository-s3", "repository-azure", "analysis-phonetic"]):
                raise ValueError(
                    "each list item must be one of ('repository-s3', 'repository-azure', 'analysis-phonetic')"
                )
        return value

    @field_validator("tls_protocols")
    def tls_protocols_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(["TLSv1.2", "TLSv1.3"]):
                raise ValueError("each list item must be one of ('TLSv1.2', 'TLSv1.3')")
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
        """Create an instance of InstanceParameters from a JSON string"""
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
        """Create an instance of InstanceParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "enable_monitoring": (
                    obj.get("enable_monitoring") if obj.get("enable_monitoring") is not None else False
                ),
                "graphite": obj.get("graphite"),
                "java_garbage_collector": (
                    obj.get("java_garbage_collector") if obj.get("java_garbage_collector") is not None else "UseG1GC"
                ),
                "java_heapspace": obj.get("java_heapspace"),
                "java_maxmetaspace": obj.get("java_maxmetaspace") if obj.get("java_maxmetaspace") is not None else 512,
                "max_disk_threshold": (
                    obj.get("max_disk_threshold") if obj.get("max_disk_threshold") is not None else 80
                ),
                "metrics_frequency": obj.get("metrics_frequency") if obj.get("metrics_frequency") is not None else 10,
                "metrics_prefix": obj.get("metrics_prefix"),
                "monitoring_instance_id": obj.get("monitoring_instance_id"),
                "plugins": obj.get("plugins"),
                "sgw_acl": obj.get("sgw_acl"),
                "syslog": obj.get("syslog"),
                "tls-ciphers": obj.get("tls-ciphers"),
                "tls-protocols": obj.get("tls-protocols"),
            }
        )
        return _obj
