# coding: utf-8

"""
    STACKIT Marketplace API

    API to manage STACKIT Marketplace.

    The version of the OpenAPI document: 1
    Contact: marketplace@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self

from stackit.stackitmarketplace.models.subscription_product import SubscriptionProduct


class VendorSubscription(BaseModel):
    """
    VendorSubscription
    """

    lifecycle_state: StrictStr = Field(description="Lifecycle state of the subscription.", alias="lifecycleState")
    product: SubscriptionProduct
    project_id: StrictStr = Field(description="The associated consumer project ID.", alias="projectId")
    subscription_id: StrictStr = Field(description="The subscription ID.", alias="subscriptionId")
    __properties: ClassVar[List[str]] = ["lifecycleState", "product", "projectId", "subscriptionId"]

    @field_validator("lifecycle_state")
    def lifecycle_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(
            [
                "SUBSCRIPTION_PENDING",
                "SUBSCRIPTION_ACTIVE",
                "SUBSCRIPTION_INACTIVE",
                "SUBSCRIPTION_CANCELLING",
                "SUBSCRIPTION_CANCELLED",
                "SUBSCRIPTION_REJECTED",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('SUBSCRIPTION_PENDING', 'SUBSCRIPTION_ACTIVE', 'SUBSCRIPTION_INACTIVE', 'SUBSCRIPTION_CANCELLING', 'SUBSCRIPTION_CANCELLED', 'SUBSCRIPTION_REJECTED')"
            )
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
        """Create an instance of VendorSubscription from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict["product"] = self.product.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VendorSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "lifecycleState": obj.get("lifecycleState"),
                "product": SubscriptionProduct.from_dict(obj["product"]) if obj.get("product") is not None else None,
                "projectId": obj.get("projectId"),
                "subscriptionId": obj.get("subscriptionId"),
            }
        )
        return _obj
