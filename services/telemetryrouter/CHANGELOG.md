## v0.8.0
- **Feature:** New API client methods `partial_update_telemetry_router`, `partial_update_destination` and `partial_update_access_token` with corresponding model classes `PartialUpdate*Payload`, `ConfigFilterPatch` and `DestinationConfigPatch*`
- **Feature:** Add `destination_count` field to `TelemetryRouterResponse` model
- **Feature:** Add `resource_labels` field to `CreateTelemetryRouterPayload`, `UpdateTelemetryRouterPayload`, `PartialUpdateTelemetryRouterPayload` and `TelemetryRouterResponse` models
- **Improvement:** `description` fields now also allow `.` characters
- **Breaking Change:** Add regex validation (non-empty, no control characters) to `ConfigFilterAttributes.key`, `DestinationConfigOpenTelemetry.bearer_token`/`uri`, `DestinationConfigOpenTelemetryBasicAuth.username`/`password`, `DestinationConfigS3.endpoint` and `DestinationConfigS3AccessKey.id`/`secret`
- **Breaking Change:** `DestinationConfigS3.bucket` may now only contain lowercase letters, digits and hyphens

## v0.7.0
- **Chore:** Bump minimum Python version to 3.11
- **Chore:** Support Python version 3.15
- **Chore:** Update dependencies

## v0.6.0
- **Feature:** Add `disabled` field to `ConfigFilter` to allow disabling a filter without removing it

## v0.5.2
- **Fix:** Corrected an invalid `pyproject.toml` build configuration (`wheel-sources` instead of `wheel.sources`) that caused `import stackit.telemetryrouter` to fail with `ModuleNotFoundError`

## v0.5.1
- **Improvement:** Add validation for `description` field in `AccessTokenBaseRequest`, `AccessTokenBaseResponse`, `CreateAccessTokenPayload`, `CreateAccessTokenResponse`, `DestinationResponse`, `GetAccessTokenResponse`, `TelemetryRouterResponse`, `UpdateAccessTokenPayload` and `UpdateAccessTokenResponse` models

## v0.5.0
- **Improvement:** Add validation for `Description` field

## v0.4.0
- **Chore:** Bump minimum Python version to 3.10
- **Chore:** Update dependencies

## v0.3.0
- **New:** v1 API version for STACKIT Telemetry Router

## v0.2.0
- **Feature:** regenerate with openapi-generator v7.22.0

## v0.1.0
- **New**: API for STACKIT Telemetry Router
