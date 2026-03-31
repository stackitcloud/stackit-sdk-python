## v1.3.0
- **Feature:** New models: `SetDefaultRetentionPayload`, `GetCredentialsGroupResponse`, `DeleteDefaultRetentionResponse`, `DefaultRetentionResponse`, `CredentialsGroupExtended`, `ComplianceLockResponse`
- **Feature:** New enum type `RetentionMode`
- **Feature:** New field `object_lock_enabled` in `Bucket` model struct
- **Feature:** New API client methods: `create_compliance_lock`, `delete_compliance_lock`, `delete_default_retention`, `get_compliance_lock`, `get_credentials_group`, `get_default_retention`, `set_default_retention`

## v1.2.2
- **Feature:** client now supports UUID and decimal types
- **Bugfix:** timeouts now passed to requests library

## v1.2.1
- **Bugfix:** Prevent year 0 timestamp issue

## v1.2.0
- **Breaking change:** Set `expires` field in `CreateAccessKeyResponse` model to optional

## v1.1.0
- **Version**: Minimal version is now python 3.9

## v1.0.4
- **Internal:** Improve deserializing and error types

## v1.0.3 (2025-05-09)
- **Feature:** Update user-agent header

## v1.0.2 (2025-03-18)
- Adapted to minor API changes

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
