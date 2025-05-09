## v1.0.2 (2025-05-09)
- **Feature:** Update user-agent header

## v1.0.1 (2025-05-05)
- **Minor change:** Use stderr by default.

## v1.0.0 (2025-03-18)
- **Breaking Change:** The region is no longer specified within the client configuration. Instead, the region must be passed as a parameter to any region-specific request.

## v0.3.0 (2025-02-06)

- **Breaking Change:**: Remove field `BackupProperties` from `CreateUpdatePayload` model
- **Fix**: Remove field `Id` from `CreateUpdateSchedulePayload` model

## v0.2.0 (2025-01-13)

- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.1 (2024-12-23)

- **Bugfix:** `Id` field of `Update` model is now of type `int64` (was `string`)

## v0.1.0 (2024-12-04)

- Manage your STACKIT Server Updates
