## v1.14.0
- **Feature:** Add `has_private_plan_option` attribute to `CatalogProductDetail` model class

## v1.13.0
- **Feature:** Add `has_demo` attribute to `CatalogProductDetail` model class

## v1.12.0
- **Breaking Change:** Change `logo` field type from `Union[StrictBytes, StrictStr]` to `StrictStr` in `CatalogProductDetail`, `CatalogProductDetailsVendor`, and `CatalogProductOverview` models

## v1.11.0
- **Feature:** Add new field `DemoUrl` to `CatalogProductDetail` model

## v1.10.0
- **Feature:** Added `PlanId` to `CatalogProductPricingOption` and `SubscriptionProduct`

## v1.9.0
- **Feature:** Added `RequestPrivatePlan` to `InquiriesCreateInquiryPayload`

## v1.8.0
- **Feature:** Add new field `free_trial` in `CatalogProductOverview` model

## v1.7.0
- **Breaking Change:** Update `InquiryFormType` enums

## v1.6.0
- **Version**: Minimal version is now python 3.9

## v1.5.1
- **Internal:** Improve deserializing and error types

## v1.5.0
- **Feature:** Add new `Assets` model for managing service certificate assets
- **Feature:** Add new `LocalizedVersion` model for localized content management
- **Feature:** Add new `NoticePeriod` model with types: `SAME_DAY`, `DAYS`, `MONTHS`
- **Feature:** Add new `ServiceCertificate` model for service certification

## v1.4.0
- **Feature:** Add support for offer types
    - new model `OfferType`
    - new attribute `CatalogProductDetail` for `CatalogProductDetail` model
- Attribute `is_product_listing` in `CatalogProductDetail` is now of type `Optional[StrictBool]` (previously `StrictBool`)

## v1.3.0 (2025-06-10)
- **Feature:** Add new field `facets` in `ListCatalogProductsResponse`

## v1.2.0 (2025-06-06)
- **Fix:** Fixed types for `VendorId`, `ProjectId`, `OrganizationId` and `SubscriptionId`

## v1.1.3 (2025-06-02)
- **Feature:** Added `industries` to `CatalogProductDetail`

## v1.1.2 (2025-05-19)
- **Improvement:** Update descriptions

## v1.1.1 (2025-05-14)
- **Feature**: Added new method `vendors_subscriptions_reject`

## v1.1.0 (2025-05-13)
- **Breaking Change:** Added organization id to `VendorSubscription`

## v1.0.1 (2025-05-09)
- **Feature:** Update user-agent header

## v1.0.0 (2025-05-05)
- **Breaking Change:**
    - Introduced dedicated type for product id with appropriate validations
- **Feature:** 
    - subscription products contain the plan id

## v0.4.0 (2025-04-16)
- **Feature:** Add new `InquiryContactSales`, `InquirySuggestProduct`, `PriceType`, `PricingOption` and `DeliveryMethod`

## v0.3.0 (2025-04-04)
- **Feature:** Add new `VendorProductId` attribute for subscription products

## v0.2.0 (2025-03-05)

- **Feature:** Add method to create inquiries: `InquiriesCreateInquiry`
- **Feature:** Add `sort` property to `ApiListCatalogProductsRequest`
- **Feature:** Add payload `ApproveSubscriptionPayload` for `ApiApproveSubscriptionRequest`

## v0.1.0 (2025-01-13)

- **New**: STACKIT Marketplace module can be used to manage the STACKIT Marketplace.
