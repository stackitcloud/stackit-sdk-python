# coding: utf-8

"""
    STACKIT RabbitMQ API

    The STACKIT RabbitMQ API provides endpoints to list service offerings, manage service instances and service credentials within STACKIT portal projects.

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

    consumer_timeout: Optional[Annotated[int, Field(strict=True, ge=1800000)]] = Field(
        default=1800000, description="The unit is milliseconds."
    )
    enable_monitoring: Optional[StrictBool] = False
    graphite: Optional[StrictStr] = Field(
        default=None,
        description="If you want to monitor your service with Graphite, you can set the custom parameter graphite. It expects the host and port where the Graphite metrics should be sent to.",
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
    plugins: Optional[List[StrictStr]] = None
    roles: Optional[List[StrictStr]] = None
    sgw_acl: Optional[StrictStr] = Field(
        default=None,
        description="Comma separated list of IP networks in CIDR notation which are allowed to access this instance.",
    )
    syslog: Optional[List[StrictStr]] = None
    tls_ciphers: Optional[List[StrictStr]] = Field(default=None, alias="tls-ciphers")
    tls_protocols: Optional[StrictStr] = Field(default=None, alias="tls-protocols")
    __properties: ClassVar[List[str]] = [
        "consumer_timeout",
        "enable_monitoring",
        "graphite",
        "max_disk_threshold",
        "metrics_frequency",
        "metrics_prefix",
        "monitoring_instance_id",
        "plugins",
        "roles",
        "sgw_acl",
        "syslog",
        "tls-ciphers",
        "tls-protocols",
    ]

    @field_validator("plugins")
    def plugins_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(
                [
                    "rabbitmq_consistent_hash_exchange",
                    "rabbitmq_federation",
                    "rabbitmq_federation_management",
                    "rabbitmq_mqtt",
                    "rabbitmq_sharding",
                    "rabbitmq_shovel",
                    "rabbitmq_shovel_management",
                    "rabbitmq_stomp",
                    "rabbitmq_tracing",
                    "rabbitmq_event_exchange",
                ]
            ):
                raise ValueError(
                    "each list item must be one of ('rabbitmq_consistent_hash_exchange', 'rabbitmq_federation', 'rabbitmq_federation_management', 'rabbitmq_mqtt', 'rabbitmq_sharding', 'rabbitmq_shovel', 'rabbitmq_shovel_management', 'rabbitmq_stomp', 'rabbitmq_tracing', 'rabbitmq_event_exchange')"
                )
        return value

    @field_validator("tls_protocols")
    def tls_protocols_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["tlsv1.2", "tlsv1.3"]):
            raise ValueError("must be one of enum values ('tlsv1.2', 'tlsv1.3')")
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
                "consumer_timeout": obj.get("consumer_timeout") if obj.get("consumer_timeout") is not None else 1800000,
                "enable_monitoring": (
                    obj.get("enable_monitoring") if obj.get("enable_monitoring") is not None else False
                ),
                "graphite": obj.get("graphite"),
                "max_disk_threshold": (
                    obj.get("max_disk_threshold") if obj.get("max_disk_threshold") is not None else 80
                ),
                "metrics_frequency": obj.get("metrics_frequency") if obj.get("metrics_frequency") is not None else 10,
                "metrics_prefix": obj.get("metrics_prefix"),
                "monitoring_instance_id": obj.get("monitoring_instance_id"),
                "plugins": obj.get("plugins"),
                "roles": obj.get("roles"),
                "sgw_acl": obj.get("sgw_acl"),
                "syslog": obj.get("syslog"),
                "tls-ciphers": obj.get("tls-ciphers"),
                "tls-protocols": obj.get("tls-protocols"),
            }
        )
        return _obj
