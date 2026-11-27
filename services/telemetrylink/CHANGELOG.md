## v0.6.0
- **Feature:** New API client methods `create_*_backflush_job`, `get_*_backflush_job` and `list_*_backflush_jobs` (each for organization, folder and project) with model classes `BackflushJobResponse`, `Create*BackflushJobPayload` and `ListBackflushJobsResponse`
- **Feature:** Add `resource_labels` field to `CreateOrUpdate*TelemetryLinkPayload`, `PartialUpdate*TelemetryLinkPayload` and `TelemetryLinkResponse` models
- **Improvement:** `enabled` field of `CreateOrUpdate*TelemetryLinkPayload` models is no longer required and defaults to `True`

## v0.5.0
- **Chore:** Bump minimum Python version to 3.11
- **Chore:** Support Python version 3.15
- **Chore:** Update dependencies

## v0.4.2
- **Fix:** Corrected an invalid `pyproject.toml` build configuration (`wheel-sources` instead of `wheel.sources`) that caused `import stackit.telemetrylink` to fail with `ModuleNotFoundError`

## v0.4.1
- **Improvement:** Add validation for `description` field in `TelemetryLinkResponse` model

## v0.4.0
- **Improvement:** Add validation for `Description` field
- **Feature:** Add support for `if_none_match` header in `create_or_update_folder_telemetry_link`, `create_or_update_organization_telemetry_link` and `create_or_update_project_telemetry_link`

## v0.3.0
- **Chore:** Bump minimum Python version to 3.10
- **Chore:** Update dependencies

## v0.2.0
- **New:** v1 API version for STACKIT Telemetry Link

## v0.1.0
- **New**: API for STACKIT Telemetry Link
