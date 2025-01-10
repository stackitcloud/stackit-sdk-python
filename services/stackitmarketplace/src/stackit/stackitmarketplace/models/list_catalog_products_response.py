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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Annotated, Self

from stackit.stackitmarketplace.models.catalog_product_overview import (
    CatalogProductOverview,
)


class ListCatalogProductsResponse(BaseModel):
    """
    ListCatalogProductsResponse
    """

    cursor: StrictStr = Field(
        description="A pagination cursor that represents a position in the dataset. Use it in subsequent requests to continue retrieving data from this position. If `null`, there are no more results to retrieve."
    )
    items: List[CatalogProductOverview]
    limit: Annotated[int, Field(le=100, strict=True, ge=0)] = Field(
        description="The maximum number of items to return in the response. If not present, an appropriate default will be used. If maximum is exceeded, maximum is used."
    )
    __properties: ClassVar[List[str]] = ["cursor", "items", "limit"]

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
        """Create an instance of ListCatalogProductsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict["items"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListCatalogProductsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cursor": obj.get("cursor"),
                "items": (
                    [CatalogProductOverview.from_dict(_item) for _item in obj["items"]]
                    if obj.get("items") is not None
                    else None
                ),
                "limit": obj.get("limit") if obj.get("limit") is not None else 50,
            }
        )
        return _obj
