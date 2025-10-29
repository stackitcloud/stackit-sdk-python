## v2.0.0
- **Feature:** Switch from `v1beta` CDN API version to `v1beta2` version.
- **Breaking change:** Changed spelling from `WAF` to `Waf` in model class names
  - `WAFStatusRuleBlock` -> `WafStatusRuleBlock`
  - `WAFRuleGroup` -> `WafRuleGroup`
  - `WAFRuleCollection` -> `WafRuleCollection`
  - `WAFRule` -> `WafRule`
  - `ListWAFCollectionsResponse` -> `ListWafCollectionsResponse`
- **Breaking change:** Changed spelling from model class named `GenericJSONResponse` to `GenericJsonResponse`
- **Breaking change:** Removal of attributes from model classes
  - Remove `description` attribute from `ErrorDetails` model class
  - Remove `domain` attribute from `PutCustomDomainResponse` and `GetCustomDomainResponse` model classes
  - Remove `occured_at` attribute from `GetCacheInfoResponseHistoryEntry` model class
- **Breaking change:** Removal of API client method `get_logs_search_filters`
- **Feature:** Add attributes to model classes
  - Add `backend` attribute to `CreateDistributionPayload` model class
- **Feature:** New model classes
  - New Loki model classes: `LokiLogSinkCredentials`, `LokiLogSinkCreate`, `LokiLogSinkPatch`
  - New Backend model classes: `HttpBackendCreate`,  `BucketBackendCreate`, `BucketBackend`, `BucketBackendPatch`, `CreateDistributionPayloadBackend`, `ConfigPatchBackend`, `ConfigBackend`
  - Other new model classes: `BucketCredentials`

## v1.7.1
- **Bugfix:** Prevent year 0 timestamp issue

## v1.7.0
- **Feature:** Add models: `DistributionWaf`, `WafConfig`, `WAFConfigPatch`, `WAFMode`, `WAFRule`, `WAFRuleCollection`, `WAFRuleGroup` and `WAFStatusRuleBlock`
- **Feature:** Add `Waf` attribute to `Config` and `Distribution`
- **Feature:** Add `WafStatus` to `DistributionRequest` and `ListWafCollections`

## v1.6.0
- **Feature:** Added Attribute `LogSink` to `ConfigPatch`
- **Feature:** Added Attribute `Geofencing` to `DistributionPayload`, `HttpBackend` and `HttpBackendPatch`
- **Feature:** Added new function `GetLogsSearchFilters`

## v1.5.0
- **Feature:** Added new filter functions `DataCenterRegion`, `RequestCountryCode`, `StatusCode` and `CacheHit`
- **Feature:** Added Attribute `LogSink` and `Certificate`
- **Feature:** Added `ConfigLogSink` and `PatchLokiLogSink` functionality

## v1.4.0
- **Version**: Minimal version is now python 3.9

## v1.3.0
- **Breaking change:** Replace oneOf `ConfigBackend` with `HttpBackend`
- **Internal:** Improve deserializing and error types

## v1.2.0
- **Feature:** Add `default_cache_duration` attribute to `Config`, `ConfigPatch` and `CreateDistributionPayload` model
- Add `originUrlRelated` to available options given in `sort_by` description

## v1.1.0 (2025-05-27)
- **Feature:** Add support for CDN Optimizer feature

## v1.0.1 (2025-05-09)
- **Feature:** Update user-agent header

## v1.0.0 (2025-05-05)
- **Feature:** Support for log management
- **Feature:** Create distribution payload has additional optional attributes for blocked countries, IPs and volume limitation
- **Feature:** Config Patch payload has additional optional attributes for blocked countries, IPs and volume limitation
- **Breaking Change:** Config has additional required attributes for blocked countries, IPs and volume limitation

## v0.1.0 (2025-03-18)
- **New**: Client for managing the CDN service
