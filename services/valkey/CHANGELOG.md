## v0.2.0
- **Breaking Change/Fix:** `create_backup` operation now returns `CreateBackupResponseItem` instead of `List[CreateBackupResponseItem]`
    The return type now correctly models the actual JSON response, this operation was broken beforehand.

## v0.1.0
- **New**: STACKIT valkey module to create key-value stores
