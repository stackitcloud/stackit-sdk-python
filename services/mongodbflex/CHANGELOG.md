## v1.2.0
- **Version**: Minimal version is now python 3.9

## v1.1.0
- **Breaking Change:** Add required `region` parameter to all API methods.
- **Feature:** Add new methods `clone_instance()` and `restore_instance()`.
- **Feature:** Add new models `InstanceFlavor` and `InstanceResponse`.

## v1.0.1 (2025-05-09)
    - **Feature:** Update user-agent header

## v1.0.0 (2025-05-05)
    - **Breaking Change:** Introduce typed enum constants for status attributes

## v0.3.0 (2025-01-21)

- **Breaking change**: Delete endpoint made private.

## v0.2.1 (2025-01-14)

- **Bugfix**: `configuration.py` region adjustment was missing

## v0.2.0 (2025-01-13)

- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.0 (2024-12-04)

- Manage your STACKIT MongoDB Flex resources
- [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/mongodbflex)
