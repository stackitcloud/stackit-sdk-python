## v0.5.0
- **Feature:** Add regex field validator for `display_name` attribute in model classes `CreateKeyPayload`, `CreateKeyRingPayload`, `CreateWrappingKeyPayload`

## v0.4.1
- **Bugfix:** Prevent year 0 timestamp issue

## v0.4.0
- Switch to API version `v1` of STACKIT KMS service (previously `v1beta`)
- **Breaking Change:** Removal of deprecated `Backend` model
- **Breaking Change:** Mark `protection` attribute as required in `Key`, `CreateKeyPayload`, `CreateWrappingKeyPayload` and `WrappingKey` model

## v0.3.0
- **Breaking Change:** Updated `create_key()` and `create_wrapping_key()` method signatures to require new `access_scope` parameter
- **Breaking Change:** Added new required `access_scope` field to `Key` and `WrappingKey` models
- **Feature:** Add new `AccessScope` enum with values `PUBLIC` and `SNA` for managing key access permissions
- **Feature:** Add new `Protection` enum with value `SOFTWARE` as a replacement for the deprecated `backend` field
- **Feature:** Add new `access_scope` field to `CreateKeyPayload` and `CreateWrappingKeyPayload` models
- **Feature:** Add new `protection` field to `CreateKeyPayload`, `CreateWrappingKeyPayload`, `Key`, and `WrappingKey` models
- **Deprecation:** The `backend` field is now deprecated in all relevant models. Use the new `protection` field instead

## v0.2.0
- **Breaking Change:** Change return type from `Key` to `Version` for `import_key()` and `rotate_key()` methods
- **Internal:** Add HTTP 409 (Conflict) error handling to API methods

## v0.1.0
- **Version**: Minimal version is now python 3.9

## v0.0.6
- **Internal:** Improve deserializing and error types

## v0.0.5
- **Improvement:** Updated validators

## v0.0.4 (2025-05-19)
- **Feature:** Added new method `delete_wrapping_key`

## v0.0.3 (2025-05-09)
- **Feature:** Update user-agent header

## v0.0.2 (2025-05-05)
- **Minor change:** Use stderr by default.
- **Minor change:** Service update.

## v0.0.1 (2025-04-28)
- **New module:** Initial publication of Key Management Service API
