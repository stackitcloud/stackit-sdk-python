# coding: utf-8

# flake8: noqa

"""
    STACKIT Marketplace API

    API to manage STACKIT Marketplace.

    The version of the OpenAPI document: 1
    Contact: marketplace@stackit.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long


__version__ = "1.0.0"

# import apis into sdk package
from stackit.stackitmarketplace.api.default_api import DefaultApi
from stackit.stackitmarketplace.api_client import ApiClient

# import ApiClient
from stackit.stackitmarketplace.api_response import ApiResponse
from stackit.stackitmarketplace.configuration import HostConfiguration
from stackit.stackitmarketplace.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from stackit.stackitmarketplace.models.catalog_pricing_option_highlight import (
    CatalogPricingOptionHighlight,
)
from stackit.stackitmarketplace.models.catalog_product_detail import (
    CatalogProductDetail,
)
from stackit.stackitmarketplace.models.catalog_product_details_vendor import (
    CatalogProductDetailsVendor,
)
from stackit.stackitmarketplace.models.catalog_product_highlight import (
    CatalogProductHighlight,
)
from stackit.stackitmarketplace.models.catalog_product_overview import (
    CatalogProductOverview,
)
from stackit.stackitmarketplace.models.catalog_product_overview_vendor import (
    CatalogProductOverviewVendor,
)
from stackit.stackitmarketplace.models.catalog_product_pricing_option import (
    CatalogProductPricingOption,
)
from stackit.stackitmarketplace.models.catalog_product_support_resource import (
    CatalogProductSupportResource,
)
from stackit.stackitmarketplace.models.catalog_product_vendor_terms import (
    CatalogProductVendorTerms,
)
from stackit.stackitmarketplace.models.current_subscription_state_response import (
    CurrentSubscriptionStateResponse,
)
from stackit.stackitmarketplace.models.error_response import ErrorResponse
from stackit.stackitmarketplace.models.list_catalog_products_response import (
    ListCatalogProductsResponse,
)
from stackit.stackitmarketplace.models.list_vendor_subscriptions_response import (
    ListVendorSubscriptionsResponse,
)
from stackit.stackitmarketplace.models.requested_subscription_state_response import (
    RequestedSubscriptionStateResponse,
)
from stackit.stackitmarketplace.models.resolve_customer_payload import (
    ResolveCustomerPayload,
)
from stackit.stackitmarketplace.models.subscription_cancel_response import (
    SubscriptionCancelResponse,
)
from stackit.stackitmarketplace.models.subscription_product import SubscriptionProduct
from stackit.stackitmarketplace.models.vendor_subscription import VendorSubscription
