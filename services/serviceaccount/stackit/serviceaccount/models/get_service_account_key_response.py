# coding: utf-8

"""
    Service Account API

    API to manage Service Accounts and their Access Tokens.  ### System for Cross-domain Identity Management (SCIM) Service Account Service offers SCIM APIs to query state. The SCIM protocol was created as standard for  automating the exchange of user identity information between identity domains, or IT systems. Service accounts  are be handled as indentites similar to SCIM users. A custom SCIM schema has been created: `/ServiceAccounts`  #### Syntax ##### Attribute operators | OPERATOR | DESCRIPTION              | |----------|--------------------------| | eq       | equal                    | | ne       | not equal                | | co       | contains                 | | sw       | starts with              | | ew       | ends with                |  ##### Logical operators | OPERATOR | DESCRIPTION              | |----------|--------------------------| | and      | logical \"and\"            | | or       | logical \"or\"             |  ##### Grouping operators | OPERATOR | DESCRIPTION              | |----------|--------------------------| | ()       | precending grouping      |  ##### Example ``` filter=email eq \"my-service-account-aBc2defg@sa.stackit.cloud\" filter=email ne \"my-service-account-aBc2defg@sa.stackit.cloud\" filter=email co \"my-service-account\" filter=name sw \"my\" filter=name ew \"account\" filter=email co \"my-service-account\" and name sw \"my\" filter=email co \"my-service-account\" and (name sw \"my\" or name ew \"account\") ```  #### Sorting  > Sorting is optional  | PARAMETER | DESCRIPTION                          | |-----------|--------------------------------------| | sortBy    | attribute response is ordered by     | | sortOrder | 'ASCENDING' (default) or 'DESCENDING'|  #### Pagination  | PARAMETER    | DESCRIPTION                                  | |--------------|----------------------------------------------| | startIndex   | index of first query result, default: 1      | | count        | maximum number of query results, default: 100|

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing_extensions import Self

from stackit.serviceaccount.models.get_service_account_key_response_credentials import (
    GetServiceAccountKeyResponseCredentials,
)


class GetServiceAccountKeyResponse(BaseModel):
    """
    GetServiceAccountKeyResponse
    """

    active: StrictBool
    created_at: datetime = Field(description="Creation time of the key", alias="createdAt")
    credentials: GetServiceAccountKeyResponseCredentials
    id: StrictStr = Field(description="Unique ID of the key.")
    key_algorithm: StrictStr = Field(alias="keyAlgorithm")
    key_origin: StrictStr = Field(alias="keyOrigin")
    key_type: StrictStr = Field(alias="keyType")
    public_key: Optional[StrictStr] = Field(
        default=None, description="Public key, in the requested format", alias="publicKey"
    )
    valid_until: Optional[datetime] = Field(
        default=None, description="If specified, the timestamp until the key is active. May be null", alias="validUntil"
    )
    __properties: ClassVar[List[str]] = [
        "active",
        "createdAt",
        "credentials",
        "id",
        "keyAlgorithm",
        "keyOrigin",
        "keyType",
        "publicKey",
        "validUntil",
    ]

    @field_validator("key_algorithm")
    def key_algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["RSA_2048"]):
            raise ValueError("must be one of enum values ('RSA_2048')")
        return value

    @field_validator("key_origin")
    def key_origin_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["USER_PROVIDED", "GENERATED"]):
            raise ValueError("must be one of enum values ('USER_PROVIDED', 'GENERATED')")
        return value

    @field_validator("key_type")
    def key_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["USER_MANAGED", "SYSTEM_MANAGED"]):
            raise ValueError("must be one of enum values ('USER_MANAGED', 'SYSTEM_MANAGED')")
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
        """Create an instance of GetServiceAccountKeyResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict["credentials"] = self.credentials.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetServiceAccountKeyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "active": obj.get("active"),
                "createdAt": obj.get("createdAt"),
                "credentials": (
                    GetServiceAccountKeyResponseCredentials.from_dict(obj["credentials"])
                    if obj.get("credentials") is not None
                    else None
                ),
                "id": obj.get("id"),
                "keyAlgorithm": obj.get("keyAlgorithm"),
                "keyOrigin": obj.get("keyOrigin"),
                "keyType": obj.get("keyType"),
                "publicKey": obj.get("publicKey"),
                "validUntil": obj.get("validUntil"),
            }
        )
        return _obj
