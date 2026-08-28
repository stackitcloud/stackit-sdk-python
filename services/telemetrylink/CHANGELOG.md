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
