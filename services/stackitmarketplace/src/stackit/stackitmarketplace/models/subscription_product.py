# coding: utf-8

"""
    STACKIT Marketplace API

    API to manage STACKIT Marketplace.

    The version of the OpenAPI document: 1
    Contact: marketplace@stackit.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self


class SubscriptionProduct(BaseModel):
    """
    SubscriptionProduct
    """

    delivery_method: StrictStr = Field(description="The product's delivery method.", alias="deliveryMethod")
    lifecycle_state: StrictStr = Field(description="The lifecycle state of the product.", alias="lifecycleState")
    price_type: StrictStr = Field(description="The product's price type.", alias="priceType")
    pricing_plan: StrictStr = Field(description="The product's pricing plan.", alias="pricingPlan")
    product_id: StrictStr = Field(description="The product ID.", alias="productId")
    product_name: StrictStr = Field(description="The name of the product.", alias="productName")
    vendor_name: StrictStr = Field(description="The product's vendor name.", alias="vendorName")
    vendor_website_url: StrictStr = Field(description="The vendor's website.", alias="vendorWebsiteUrl")
    __properties: ClassVar[List[str]] = [
        "deliveryMethod",
        "lifecycleState",
        "priceType",
        "pricingPlan",
        "productId",
        "productName",
        "vendorName",
        "vendorWebsiteUrl",
    ]

    @field_validator("delivery_method")
    def delivery_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["SAAS"]):
            raise ValueError("must be one of enum values ('SAAS')")
        return value

    @field_validator("lifecycle_state")
    def lifecycle_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["PRODUCT_LIVE", "PRODUCT_PREVIEW"]):
            raise ValueError("must be one of enum values ('PRODUCT_LIVE', 'PRODUCT_PREVIEW')")
        return value

    @field_validator("price_type")
    def price_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["CONTRACT", "FREE", "FREE_TRIAL", "BYOL", "PAYG"]):
            raise ValueError("must be one of enum values ('CONTRACT', 'FREE', 'FREE_TRIAL', 'BYOL', 'PAYG')")
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
        """Create an instance of SubscriptionProduct from a JSON string"""
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
        """Create an instance of SubscriptionProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "deliveryMethod": obj.get("deliveryMethod"),
                "lifecycleState": obj.get("lifecycleState"),
                "priceType": obj.get("priceType"),
                "pricingPlan": obj.get("pricingPlan"),
                "productId": obj.get("productId"),
                "productName": obj.get("productName"),
                "vendorName": obj.get("vendorName"),
                "vendorWebsiteUrl": obj.get("vendorWebsiteUrl"),
            }
        )
        return _obj
