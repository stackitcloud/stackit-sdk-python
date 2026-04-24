## v0.4.0
- **Feature:** model `CreateResourcePoolPayload` now has an additional field `snapshotPolicyId`
- **Feature:** model `CreateResourcePoolSnapshotPayload` now has an additional field `snaplockRetentionHours`
- **Feature:** model `ResourcePool` now has an additional field `snapshotPolicy`
- **Feature:** model `ResourcePoolSnapshot` now has an additional field `snaplockExpiryTime`
- **Feature:** model `ResourcePoolSpace` now has an additional field `usedBySnapshotsGigabytes`
- **Feature:** model `UpdateResourcePoolPayload` now has an additional field `snapshotPolicyId`
- **Feature:** new models: `DisableLockResponse`, `EnableLockResponse`, `GetLockResponse`, `GetScheduleResponse`, `GetSnapshotPolicyResponse`, `ListSchedulesResponse`, `ListSnapshotPoliciesResponse`, `ResourcePoolSnapshotPolicy`, `Schedule`, `SnapshotPolicy`, `SnapshotPolicySchedule`, `UpdateResourcePoolSnapshotPayload`, `UpdateResourcePoolSnapshotResponse`
- **Feature:** new operations: `UpdateResourcePoolSnapshot`, `ListSchedules`, `GetSchedule`, `ListSnapshotPolicies`, `GetSnapshotPolicy`, `DisableLock`, `GetLock`, `EnableLock`, 

## v0.3.1
- **Feature:** client now supports UUID and decimal types
- **Bugfix:** timeouts now passed to requests library

## v0.3.0
- **Breaking change:** The `name` and `spaceHardLimitGigabytes` fields are now marked as required for `ShareExportPayload`, `SharePayload`.

## v0.2.0
- **Feature:** Switch from `v1beta` API version to `v1` version.
- **Breaking change:** Remove `ListSnapshotSchedules` method
- **Breaking change:** Remove field `SnapshotScheduleName` from `CreateResourcePoolPayload` and `UpdateResourcePoolPayload` model
- **Breaking change:** Remove field `SnapshotSchedule` from `CreateResourcePoolResponseResourcePool`, `GetResourcePoolResponseResourcePool`, `UpdateResourcePoolResponseResourcePoolGetStateRetType` and `ResourcePool` model

## v0.1.0
- **New**: STACKIT File Storage (SFS) service