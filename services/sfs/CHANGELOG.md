## v0.3.0
- **Breaking change:** The `name` and `spaceHardLimitGigabytes` fields are now marked as required for `ShareExportPayload`, `SharePayload`.

## v0.2.0
- **Feature:** Switch from `v1beta` API version to `v1` version.
- **Breaking change:** Remove `ListSnapshotSchedules` method
- **Breaking change:** Remove field `SnapshotScheduleName` from `CreateResourcePoolPayload` and `UpdateResourcePoolPayload` model
- **Breaking change:** Remove field `SnapshotSchedule` from `CreateResourcePoolResponseResourcePool`, `GetResourcePoolResponseResourcePool`, `UpdateResourcePoolResponseResourcePoolGetStateRetType` and `ResourcePool` model

## v0.1.0
- **New**: STACKIT File Storage (SFS) service