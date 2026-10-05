## v0.7.0
- **Feature:** Add support for managing AppRoles and their secret IDs: new `Approle`, `ApproleList`, `ApproleSecret`, `ApproleSecretList`, `CreateApprolePayload`, `CreateApproleSecretIdPayload`, `UpdateApprolePayload` and `UpdateApproleSecretIdPayload` models, plus new `create_approle`, `get_approle`, `get_approles`, `update_approle`, `delete_approle`, `create_approle_secret_id`, `get_approle_secret_id`, `list_approle_secret_ids`, `update_approle_secret_id` and `delete_approle_secret_id` operations

## v0.6.0
- **Chore:** Bump minimum Python version to 3.10
- **Chore:** Update dependencies

## v0.5.0
- **Feature:** regenerate with openapi-generator v7.22.0

## v0.4.1
- **Feature:** client now supports UUID and decimal types
- **Bugfix:** timeouts now passed to requests library

## v0.4.0
- **Feature:** added KmsKey model
- **Feature:** added KmsKey to Instance, CreateInstancePayload and UpdateInstancePayload

## v0.3.0
- **Version**: Minimal version is now python 3.9

## v0.2.3
- **Internal:** Improve deserializing and error types

## v0.2.2 (2025-05-09)
- **Feature:** Update user-agent header

## v0.2.1 (2025-03-20)
- **Improvement:** Error handling
- **Feature:** Add description to `UpdateUserPayload`

## v0.2.0 (2025-01-13)

- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.0 (2024-12-04)

- Manage your STACKIT Secrets manager resources
- [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/secretsmanager)
