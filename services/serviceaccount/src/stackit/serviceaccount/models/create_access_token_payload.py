# coding: utf-8

"""
    Service Account API

    API to manage Service Accounts and their Access Tokens.  ### System for Cross-domain Identity Management (SCIM) Service Account Service offers SCIM APIs to query state. The SCIM protocol was created as standard for  automating the exchange of user identity information between identity domains, or IT systems. Service accounts  are be handled as indentites similar to SCIM users. A custom SCIM schema has been created: `/ServiceAccounts`  #### Syntax ##### Attribute operators | OPERATOR | DESCRIPTION              | |----------|--------------------------| | eq       | equal                    | | ne       | not equal                | | co       | contains                 | | sw       | starts with              | | ew       | ends with                |  ##### Logical operators | OPERATOR | DESCRIPTION              | |----------|--------------------------| | and      | logical \"and\"            | | or       | logical \"or\"             |  ##### Grouping operators | OPERATOR | DESCRIPTION              | |----------|--------------------------| | ()       | precending grouping      |  ##### Example ``` filter=email eq \"my-service-account-aBc2defg@sa.stackit.cloud\" filter=email ne \"my-service-account-aBc2defg@sa.stackit.cloud\" filter=email co \"my-service-account\" filter=name sw \"my\" filter=name ew \"account\" filter=email co \"my-service-account\" and name sw \"my\" filter=email co \"my-service-account\" and (name sw \"my\" or name ew \"account\") ```  #### Sorting  > Sorting is optional  | PARAMETER | DESCRIPTION                          | |-----------|--------------------------------------| | sortBy    | attribute response is ordered by     | | sortOrder | 'ASCENDING' (default) or 'DESCENDING'|  #### Pagination  | PARAMETER    | DESCRIPTION                                  | |--------------|----------------------------------------------| | startIndex   | index of first query result, default: 1      | | count        | maximum number of query results, default: 100|

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated, Self


class CreateAccessTokenPayload(BaseModel):
    """
    CreateAccessTokenPayload
    """  # noqa: E501

    ttl_days: Annotated[int, Field(le=180, strict=True, ge=1)] = Field(
        description="The duration in days for how long the new Access Token should be valid.", alias="ttlDays"
    )
    __properties: ClassVar[List[str]] = ["ttlDays"]

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
        """Create an instance of CreateAccessTokenPayload from a JSON string"""
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
        """Create an instance of CreateAccessTokenPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({"ttlDays": obj.get("ttlDays")})
        return _obj
