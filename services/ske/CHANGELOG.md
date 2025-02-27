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
