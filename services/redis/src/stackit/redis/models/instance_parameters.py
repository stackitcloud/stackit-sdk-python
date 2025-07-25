# coding: utf-8

"""
    STACKIT Redis API

    The STACKIT Redis API provides endpoints to list service offerings, manage service instances and service credentials within STACKIT portal projects.

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

    down_after_milliseconds: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=10000, description="The unit is milliseconds.", alias="down-after-milliseconds"
    )
    enable_monitoring: Optional[StrictBool] = False
    failover_timeout: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=30000, description="The unit is milliseconds.", alias="failover-timeout"
    )
    graphite: Optional[StrictStr] = Field(
        default=None,
        description="If you want to monitor your service with Graphite, you can set the custom parameter graphite. It expects the host and port where the Graphite metrics should be sent to.",
    )
    lazyfree_lazy_eviction: Optional[StrictStr] = Field(default="no", alias="lazyfree-lazy-eviction")
    lazyfree_lazy_expire: Optional[StrictStr] = Field(default="no", alias="lazyfree-lazy-expire")
    lua_time_limit: Optional[StrictInt] = Field(default=5000, alias="lua-time-limit")
    max_disk_threshold: Optional[StrictInt] = Field(
        default=80,
        description="This component monitors ephemeral and persistent disk usage. If one of these disk usages reaches the default configured threshold of 80%, the a9s Parachute stops all processes on that node.",
    )
    maxclients: Optional[Annotated[int, Field(strict=True, ge=1)]] = 10000
    maxmemory_policy: Optional[StrictStr] = Field(default="volatile-lru", alias="maxmemory-policy")
    maxmemory_samples: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=5, alias="maxmemory-samples")
    metrics_frequency: Optional[StrictInt] = Field(
        default=10, description="Frequency of metrics being emitted in seconds"
    )
    metrics_prefix: Optional[StrictStr] = Field(
        default=None,
        description="Depending on your graphite provider, you might need to prefix the metrics with a certain value, like an API key for example.",
    )
    min_replicas_max_lag: Optional[StrictInt] = Field(default=10, description="The unit is seconds.")
    monitoring_instance_id: Optional[StrictStr] = None
    notify_keyspace_events: Optional[StrictStr] = Field(
        default="",
        description="The allowed value must include the following characters only: [K,E,g,$,l,s,h,z,x,e,A,t]",
        alias="notify-keyspace-events",
    )
    sgw_acl: Optional[StrictStr] = Field(
        default=None,
        description="Comma separated list of IP networks in CIDR notation which are allowed to access this instance.",
    )
    snapshot: Optional[StrictStr] = Field(
        default=None, description="This setting must follow the original Redis configuration for RDB."
    )
    syslog: Optional[List[StrictStr]] = None
    tls_ciphers: Optional[List[StrictStr]] = Field(default=None, alias="tls-ciphers")
    tls_ciphersuites: Optional[StrictStr] = Field(default=None, alias="tls-ciphersuites")
    tls_protocols: Optional[StrictStr] = Field(default=None, alias="tls-protocols")
    __properties: ClassVar[List[str]] = [
        "down-after-milliseconds",
        "enable_monitoring",
        "failover-timeout",
        "graphite",
        "lazyfree-lazy-eviction",
        "lazyfree-lazy-expire",
        "lua-time-limit",
        "max_disk_threshold",
        "maxclients",
        "maxmemory-policy",
        "maxmemory-samples",
        "metrics_frequency",
        "metrics_prefix",
        "min_replicas_max_lag",
        "monitoring_instance_id",
        "notify-keyspace-events",
        "sgw_acl",
        "snapshot",
        "syslog",
        "tls-ciphers",
        "tls-ciphersuites",
        "tls-protocols",
    ]

    @field_validator("lazyfree_lazy_eviction")
    def lazyfree_lazy_eviction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["yes", "no"]):
            raise ValueError("must be one of enum values ('yes', 'no')")
        return value

    @field_validator("lazyfree_lazy_expire")
    def lazyfree_lazy_expire_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["yes", "no"]):
            raise ValueError("must be one of enum values ('yes', 'no')")
        return value

    @field_validator("maxmemory_policy")
    def maxmemory_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            ["volatile-lru", "allkeys-lru", "volatile-random", "allkeys-random", "volatile-ttl", "noeviction"]
        ):
            raise ValueError(
                "must be one of enum values ('volatile-lru', 'allkeys-lru', 'volatile-random', 'allkeys-random', 'volatile-ttl', 'noeviction')"
            )
        return value

    @field_validator("tls_protocols")
    def tls_protocols_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["TLSv1.2", "TLSv1.3"]):
            raise ValueError("must be one of enum values ('TLSv1.2', 'TLSv1.3')")
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
                "down-after-milliseconds": (
                    obj.get("down-after-milliseconds") if obj.get("down-after-milliseconds") is not None else 10000
                ),
                "enable_monitoring": (
                    obj.get("enable_monitoring") if obj.get("enable_monitoring") is not None else False
                ),
                "failover-timeout": obj.get("failover-timeout") if obj.get("failover-timeout") is not None else 30000,
                "graphite": obj.get("graphite"),
                "lazyfree-lazy-eviction": (
                    obj.get("lazyfree-lazy-eviction") if obj.get("lazyfree-lazy-eviction") is not None else "no"
                ),
                "lazyfree-lazy-expire": (
                    obj.get("lazyfree-lazy-expire") if obj.get("lazyfree-lazy-expire") is not None else "no"
                ),
                "lua-time-limit": obj.get("lua-time-limit") if obj.get("lua-time-limit") is not None else 5000,
                "max_disk_threshold": (
                    obj.get("max_disk_threshold") if obj.get("max_disk_threshold") is not None else 80
                ),
                "maxclients": obj.get("maxclients") if obj.get("maxclients") is not None else 10000,
                "maxmemory-policy": (
                    obj.get("maxmemory-policy") if obj.get("maxmemory-policy") is not None else "volatile-lru"
                ),
                "maxmemory-samples": obj.get("maxmemory-samples") if obj.get("maxmemory-samples") is not None else 5,
                "metrics_frequency": obj.get("metrics_frequency") if obj.get("metrics_frequency") is not None else 10,
                "metrics_prefix": obj.get("metrics_prefix"),
                "min_replicas_max_lag": (
                    obj.get("min_replicas_max_lag") if obj.get("min_replicas_max_lag") is not None else 10
                ),
                "monitoring_instance_id": obj.get("monitoring_instance_id"),
                "notify-keyspace-events": (
                    obj.get("notify-keyspace-events") if obj.get("notify-keyspace-events") is not None else ""
                ),
                "sgw_acl": obj.get("sgw_acl"),
                "snapshot": obj.get("snapshot"),
                "syslog": obj.get("syslog"),
                "tls-ciphers": obj.get("tls-ciphers"),
                "tls-ciphersuites": obj.get("tls-ciphersuites"),
                "tls-protocols": obj.get("tls-protocols"),
            }
        )
        return _obj
