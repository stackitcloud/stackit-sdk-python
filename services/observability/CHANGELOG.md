## v0.4.1 (2025-05-09)
- **Feature:** Update user-agent header

## v0.4.0 (2025-04-17)
- **Feature:** Add new methods `create_logs_alertgroups`, `delete_logs_alertgroup`, `get_logs_alertgroup`, `list_logs_alertgroups`, `update_logs_alertgroup`

## v0.3.0 (2025-03-27)
- **Feature:** Added support for alert groups and alert rules.

## v0.2.0 (2025-01-13)
- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.0 (2024-12-04)
- Manage your STACKIT Observability resources
- [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/observability)
