## v2.0.0 (2025-XX-YY)
- **Breaking Change:** The region is no longer specified within the client configuration. Instead, the region must be passed as a parameter to any region-specific request.

## v1.0.1 (2025-02-26)

- New value `eu02` in region enum

## v1.0.0 (2025-02-06)

- **Breaking Change:** The region is no longer specified within the client configuration. Instead, the region must be passed as a parameter to any region-specific request.

## v0.2.1 (2025-01-14)

- **Bugfix**: `configuration.py` region adjustment was missing

## v0.2.0 (2025-01-13)

- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.0 (2024-12-04)

- Manage your STACKIT Object Storage resources
- [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/objectstorage)
