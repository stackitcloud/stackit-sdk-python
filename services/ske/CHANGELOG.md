## v1.6.0
- **Feature:** new model `AccessScope`
- **Feature:** new model `V2ControlPlaneNetwork`
- **Feature:** added field `control_plane` of type `V2ControlPlaneNetwork` to model `Network`

## v1.5.0
- **Feature:** Add field `identity` to model `ClusterStatus`

## v1.4.0
- **Feature:** Add new optional `version_state` param to `DefaultApi.list_provider_options` method
- **Feature:** Add new enum `GetProviderOptionsRequestVersionState`

## v1.3.1
- **Bugfix:** Prevent year 0 timestamp issue

## v1.3.0
- **Feature:** Add new field `kubernetes` to `Nodepool` model

## v1.2.0
- **Version**: Minimal version is now python 3.9

## v1.1.0
- **Feature:** Add new methods to trigger the wake up of a cluster.

## v1.0.0
- **Breaking Change:** The region is no longer specified within the client configuration. Instead, the region must be passed as a parameter to any region-specific request.
- **Breaking Change:** Renamed `Argus` model to `Observability`
- **Breaking Change:** Renamed `argus` field to `observability` in `Extension` model
- **Breaking Change:** Removed enum validation in `code` field in `ClusterError` model
- **Deprecated:** Remove deprecated `allow_privileged_containers` field in `Kubernetes` model
- **Internal:** Improve deserializing and error types

## v0.6.0
- **Feature:** Add new `ClusterErrorCode` types: `CLUSTERERRORCODE_INFRA_SNA_NETWORK_NOT_FOUND`, `CLUSTERERRORCODE_FETCHING_ERRORS_NOT_POSSIBLE`

## v0.5.0 (2025-06-10)
- **Feature:** Add new field `pod_address_ranges` to `ClusterStatus`

## v0.4.3 (2025-05-14)
- **Feature:** Added enum `SKE_NODE_MACHINE_TYPE_NOT_FOUND` to `ClusterError`

## v0.4.2 (2025-05-13)
- **Feature:** Added `ClusterError`

## v0.4.1 (2025-05-09)
- **Feature:** Update user-agent header

## v0.4.0 (2025-02-27)
- `Nodepool`: `maximum` and `minimum` must be <= 1000

## v0.3.0 (2025-02-06)
- **Removal:** The following methods were removed after deprecation (2024-04-16) and [`serviceenablement` SDK](https://github.com/stackitcloud/stackit-sdk-python/tree/main/services/serviceenablement) must be used instead.
  - `DisableService`
  - `EnableService`
  - `GetServiceStatus`

## v0.2.0 (2025-01-13)
- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.0 (2024-12-04)
- Manage your STACKIT Kubernetes Engine resources
- [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/ske)
