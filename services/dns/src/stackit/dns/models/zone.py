# coding: utf-8

"""
    STACKIT DNS API

    This api provides dns

    The version of the OpenAPI document: 1.0
    Contact: dns@stackit.cloud
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

from stackit.dns.models.domain_extensions import DomainExtensions
from stackit.dns.models.label import Label


class Zone(BaseModel):
    """
    Zone.
    """  # noqa: E501

    acl: StrictStr = Field(description="access control list")
    active: Optional[StrictBool] = None
    contact_email: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(
        default=None, description="contact email from soa record", alias="contactEmail"
    )
    creation_finished: StrictStr = Field(description="when zone creation finished", alias="creationFinished")
    creation_started: StrictStr = Field(description="when zone creation started", alias="creationStarted")
    default_ttl: Annotated[int, Field(le=99999999, strict=True, ge=60)] = Field(
        description="default time to live", alias="defaultTTL"
    )
    description: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(
        default=None, description="description of the zone"
    )
    dns_name: Annotated[str, Field(min_length=1, strict=True, max_length=253)] = Field(
        description="zone name", alias="dnsName"
    )
    error: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(
        default=None, description="Error shows error in case create/update/delete failed"
    )
    expire_time: Annotated[int, Field(le=99999999, strict=True, ge=60)] = Field(
        description="expire time", alias="expireTime"
    )
    extensions: Optional[DomainExtensions] = None
    id: StrictStr = Field(description="zone id")
    is_reverse_zone: Optional[StrictBool] = Field(
        default=None, description="if the zone is a reverse zone or not", alias="isReverseZone"
    )
    labels: Optional[List[Label]] = None
    name: Annotated[str, Field(min_length=1, strict=True, max_length=63)] = Field(description="user given name")
    negative_cache: Annotated[int, Field(le=99999999, strict=True, ge=60)] = Field(
        description="negative caching", alias="negativeCache"
    )
    primaries: Optional[Annotated[List[StrictStr], Field(max_length=10)]] = Field(
        default=None, description="primary name server for secondary zone"
    )
    primary_name_server: StrictStr = Field(description="primary name server. FQDN", alias="primaryNameServer")
    record_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, description="record count how many records are in the zone", alias="recordCount"
    )
    refresh_time: Annotated[int, Field(le=99999999, strict=True, ge=60)] = Field(
        description="refresh time", alias="refreshTime"
    )
    retry_time: Annotated[int, Field(le=99999999, strict=True, ge=60)] = Field(
        description="retry time", alias="retryTime"
    )
    serial_number: StrictInt = Field(description="serial number", alias="serialNumber")
    state: StrictStr = Field(description="zone state")
    type: StrictStr = Field(description="zone type")
    update_finished: StrictStr = Field(description="when zone update/deletion finished", alias="updateFinished")
    update_started: StrictStr = Field(description="when zone update/deletion started", alias="updateStarted")
    visibility: StrictStr = Field(description="visibility of the zone")
    __properties: ClassVar[List[str]] = [
        "acl",
        "active",
        "contactEmail",
        "creationFinished",
        "creationStarted",
        "defaultTTL",
        "description",
        "dnsName",
        "error",
        "expireTime",
        "extensions",
        "id",
        "isReverseZone",
        "labels",
        "name",
        "negativeCache",
        "primaries",
        "primaryNameServer",
        "recordCount",
        "refreshTime",
        "retryTime",
        "serialNumber",
        "state",
        "type",
        "updateFinished",
        "updateStarted",
        "visibility",
    ]

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(
            [
                "CREATING",
                "CREATE_SUCCEEDED",
                "CREATE_FAILED",
                "DELETING",
                "DELETE_SUCCEEDED",
                "DELETE_FAILED",
                "UPDATING",
                "UPDATE_SUCCEEDED",
                "UPDATE_FAILED",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('CREATING', 'CREATE_SUCCEEDED', 'CREATE_FAILED', 'DELETING', 'DELETE_SUCCEEDED', 'DELETE_FAILED', 'UPDATING', 'UPDATE_SUCCEEDED', 'UPDATE_FAILED')"
            )
        return value

    @field_validator("type")
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["primary", "secondary"]):
            raise ValueError("must be one of enum values ('primary', 'secondary')")
        return value

    @field_validator("visibility")
    def visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["public"]):
            raise ValueError("must be one of enum values ('public')")
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
        """Create an instance of Zone from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of extensions
        if self.extensions:
            _dict["extensions"] = self.extensions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict["labels"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Zone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "acl": obj.get("acl"),
                "active": obj.get("active"),
                "contactEmail": obj.get("contactEmail"),
                "creationFinished": obj.get("creationFinished"),
                "creationStarted": obj.get("creationStarted"),
                "defaultTTL": obj.get("defaultTTL"),
                "description": obj.get("description"),
                "dnsName": obj.get("dnsName"),
                "error": obj.get("error"),
                "expireTime": obj.get("expireTime"),
                "extensions": (
                    DomainExtensions.from_dict(obj["extensions"]) if obj.get("extensions") is not None else None
                ),
                "id": obj.get("id"),
                "isReverseZone": obj.get("isReverseZone"),
                "labels": (
                    [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None
                ),
                "name": obj.get("name"),
                "negativeCache": obj.get("negativeCache"),
                "primaries": obj.get("primaries"),
                "primaryNameServer": obj.get("primaryNameServer"),
                "recordCount": obj.get("recordCount"),
                "refreshTime": obj.get("refreshTime"),
                "retryTime": obj.get("retryTime"),
                "serialNumber": obj.get("serialNumber"),
                "state": obj.get("state"),
                "type": obj.get("type"),
                "updateFinished": obj.get("updateFinished"),
                "updateStarted": obj.get("updateStarted"),
                "visibility": obj.get("visibility"),
            }
        )
        return _obj
