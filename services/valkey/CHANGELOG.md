## v0.3.0
- **Chore:** Bump minimum Python version to 3.11
- **Chore:** Update dependencies

## v0.2.2
- **Docs:** `InstanceParameters.min_replicas_to_write` doc comment now notes it should not be greater than the number of nodes (e.g. 1 or 3)

## v0.2.1
- **Fix:** Corrected an invalid `pyproject.toml` build configuration (`wheel-sources` instead of `wheel.sources`) that caused `import stackit.valkey` to fail with `ModuleNotFoundError`

## v0.2.0
- **Breaking Change/Fix:** `create_backup` operation now returns `CreateBackupResponseItem` instead of `List[CreateBackupResponseItem]`
    The return type now correctly models the actual JSON response, this operation was broken beforehand.

## v0.1.0
- **New**: STACKIT valkey module to create key-value stores
