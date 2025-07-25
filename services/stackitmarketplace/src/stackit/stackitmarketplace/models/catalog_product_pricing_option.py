# coding: utf-8

"""
    STACKIT Marketplace API

    API to manage STACKIT Marketplace.

    The version of the OpenAPI document: 1
    Contact: marketplace@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from stackit.stackitmarketplace.models.catalog_pricing_option_highlight import (
    CatalogPricingOptionHighlight,
)
from stackit.stackitmarketplace.models.notice_period import NoticePeriod
from stackit.stackitmarketplace.models.price_type import PriceType
from stackit.stackitmarketplace.models.pricing_option_unit import PricingOptionUnit


class CatalogProductPricingOption(BaseModel):
    """
    CatalogProductPricingOption
    """  # noqa: E501

    description: StrictStr = Field(description="The pricing option description.")
    highlights: List[CatalogPricingOptionHighlight] = Field(description="The list of highlights.")
    name: StrictStr = Field(description="The pricing option name.")
    notice_period: Optional[NoticePeriod] = Field(default=None, alias="noticePeriod")
    price_type: Optional[PriceType] = Field(default=None, alias="priceType")
    pricing_plan: Optional[StrictStr] = Field(
        default=None, description="Additional price type information.", alias="pricingPlan"
    )
    rate: Optional[StrictStr] = Field(default=None, description="The price of the product (per unit).")
    sku: StrictStr = Field(description="The concrete variant of the product.")
    sku_info: StrictStr = Field(description="Short description of this offering.", alias="skuInfo")
    sku_info_details: StrictStr = Field(
        description="More details about what this offering entails.", alias="skuInfoDetails"
    )
    unit: Optional[PricingOptionUnit] = None
    __properties: ClassVar[List[str]] = [
        "description",
        "highlights",
        "name",
        "noticePeriod",
        "priceType",
        "pricingPlan",
        "rate",
        "sku",
        "skuInfo",
        "skuInfoDetails",
        "unit",
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
        """Create an instance of CatalogProductPricingOption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in highlights (list)
        _items = []
        if self.highlights:
            for _item in self.highlights:
                if _item:
                    _items.append(_item.to_dict())
            _dict["highlights"] = _items
        # override the default output from pydantic by calling `to_dict()` of notice_period
        if self.notice_period:
            _dict["noticePeriod"] = self.notice_period.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CatalogProductPricingOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "description": obj.get("description"),
                "highlights": (
                    [CatalogPricingOptionHighlight.from_dict(_item) for _item in obj["highlights"]]
                    if obj.get("highlights") is not None
                    else None
                ),
                "name": obj.get("name"),
                "noticePeriod": (
                    NoticePeriod.from_dict(obj["noticePeriod"]) if obj.get("noticePeriod") is not None else None
                ),
                "priceType": obj.get("priceType"),
                "pricingPlan": obj.get("pricingPlan"),
                "rate": obj.get("rate"),
                "sku": obj.get("sku"),
                "skuInfo": obj.get("skuInfo"),
                "skuInfoDetails": obj.get("skuInfoDetails"),
                "unit": obj.get("unit"),
            }
        )
        return _obj
