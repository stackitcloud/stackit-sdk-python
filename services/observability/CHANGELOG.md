# v0.10.1
- **Feature:** Add attributes `jaeger_http_traces_url`, `otlp_grpc_traces_url` and `otlp_http_traces_url` to `InstanceSensitiveData` model

## v0.10.0
- **Feature:** Add support for HTTP checks and cert checks

## v0.9.2
- **Feature:** Add `metrics_endpoint_url` attribute to `InstanceSensitiveData` model

## v0.9.1
- Introduce new model `UpdateAlertConfigsPayloadRouteRoutesInner` 

## v0.9.0
- **Feature:** Add new `GoogleChat` webhook

## v0.8.0
- **Feature:** Add new model `CreateCredentialsPayload`
- **Feature:** Enhance `create_credentials()` method to accept optional payload parameter 
- **Internal:** Add HTTP 400 error handling

## v0.7.0
- **Version**: Minimal version is now python 3.9

## v0.6.0
- **Feature:** Add new methods `get_logs_configs()`, `update_logs_configs()`, `get_traces_configs()`, `update_traces_configs()`, `get_metrics_storage_retention()`, `update_metrics_storage_retention()`, `get_scrape_config()`, `update_scrape_config()`, `list_acl()`, `update_acl()`, `list_alert_config_receivers()`, `list_alert_config_routes()`, `update_alert_config_receiver()`, `update_alert_config_route()`, `list_alertgroups()`, `list_alertrules()`, `list_credentials()`, `list_instances()`
- **Feature:** Add new models `LogsConfig`, `LogsConfigResponse`, `TraceConfig`, `TracesConfigResponse`, `UpdateLogsConfigsPayload`, `UpdateTracesConfigsPayload`

## v0.5.1
- **Internal:** Improve deserializing and error types

## v0.5.0 (2025-05-27)
- **Feature:** Add support for `matchers` to route
- **Feature:** Add support for `priority levels`, `sendResolved`, `continue` to alert config models

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
