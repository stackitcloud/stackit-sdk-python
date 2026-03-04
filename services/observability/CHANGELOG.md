## v0.13.0
- **Feature:** manage alert records
    - New API client methods: `create_alert_record`, `delete_alert_record`, `delete_alert_records`, `get_alert_record`, `list_alert_records`, `update_alert_record`, `partial_update_alert_records`
    - New model classes: `AlertRecord`, `AlertRecordResponse`, `AlertRecordsResponse`, `CreateAlertRecordPayload`, `UpdateAlertRecordPayload`, `PartialUpdateAlertRecordsRequestInner`
- **Feature:** manage alert rules
    - New API client methods: `get_alertrule`, `update_alertrule`, `delete_alertrule`
    - New model classes: `AlertRuleResponse`, `UpdateAlertrulePayload`
- **Feature:** manage backups
    - New API client methods: `create_backup`,`create_backup_schedule`, `list_backup_retentions`, `list_backup_schedules`, `list_backups`, `restore_backup`
    - New model classes: `BackupResponse`, `BackupRetentionResponse`, `BackupSchedule`, `BackupSchedulePostResponse`, `BackupScheduleResponse`, `CreateBackupSchedulePayload`
- **Feature:** to manage checks
    - MongoDB
        - New API client methods: `create_mongodb_check`, `delete_mongodb_check`, `list_mongodb_checks`
        - New model classes: `CreateMongodbCheckPayload`, `MongodbCheckChildResponse`, `MongodbCheckResponse`
    - RabbitMQ
        - New API client methods: `create_rabbitmq_check`, `delete_rabbitmq_check`, `list_rabbitmq_checks`
        - New model classes: `CreateRabbitmqCheckPayload`, `RabbitMQCheckChildResponse`, `RabbitmqCheckResponse`
    - Network
        - New API client methods: `list_network_checks`, `delete_network_check`, `create_network_check`
        - New model classes: `CreateNetworkCheckPayload`, `NetworkCheckChildResponse`, `NetworkCheckResponse`
    - Redis
        - New API client methods: `create_redis_check`, `list_redis_checks`, `delete_redis_check`
        - New model classes: `CreateRedisCheckPayload`, `RedisCheckChildResponse`, `RedisCheckResponse`
    - MySQL
        - New API client methods: `create_mysql_check`, `delete_mysql_check`, `list_mysql_checks`
        - New model classes: `CreateMysqlCheckPayload`, `MysqlCheckChildResponse`, `MysqlCheckResponse`
    - Ping
        - New API client methods: `create_ping_check`, `delete_ping_check`, `list_ping_checks`
        - New model classes: `CreatePingCheckPayload`, `PingCheckChildResponse`, `PingCheckResponse`
    - Elasticsearch
        - New API client methods: `create_elasticsearch_check`, `delete_elasticsearch_check`, `list_elasticsearch_checks`
        - New model classes: `CreateElasticsearchCheckPayload`, `ElasticsearchCheckChildResponse`, `ElasticsearchCheckResponse`
    - PostgreSQL
        - New API client methods: `create_postgresql_check`, `delete_postgresql_check`, `list_postgresql_checks`
        - New model classes: `CreatePostgresqlCheckPayload`, `PostgresqlCheckChildResponse`, `PostgresqlCheckResponse`
- **Feature:** List offerings
    - New API client method: `list_offerings`
    - New model struct: `Offerings`
- **Feature:** Manage scrape configs
    - New API client method: `delete_scrape_configs`, `partial_update_scrape_configs`
    - New model struct: `PartialUpdateScrapeConfigsRequestInner`
- **Breaking changes**:
    - rename `CreateScrapeConfigPayloadBasicAuth` to `PartialUpdateScrapeConfigsRequestInnerBasicAuth`
    - rename `CreateScrapeConfigPayloadHttpSdConfigsInner` to `PartialUpdateScrapeConfigsRequestInnerHttpSdConfigsInner`
    - rename `CreateScrapeConfigPayloadHttpSdConfigsInnerOauth2` to `PartialUpdateScrapeConfigsRequestInnerHttpSdConfigsInnerOauth2`
    - rename `CreateScrapeConfigPayloadHttpSdConfigsInnerOauth2TlsConfig` to `PartialUpdateScrapeConfigsRequestInnerHttpSdConfigsInnerOauth2TlsConfig`
    - rename `CreateScrapeConfigPayloadMetricsRelabelConfigsInner` to `PartialUpdateScrapeConfigsRequestInnerMetricsRelabelConfigsInner`
    - rename `CreateScrapeConfigPayloadStaticConfigsInner` to `PartialUpdateScrapeConfigsRequestInnerStaticConfigsInner`

## v0.12.0
- **Breaking change:** The `PartialUpdateAlertrules` takes now `PartialUpdateAlertrulesRequestInner` instead of `UpdateAlertgroupsRequestInnerRulesInner`
- **Breaking change:** The type of `Rules` in `CreateLogsAlertgroupsPayload` and `UpdateLogsAlertgroupPayload` has changed from `[]UpdateAlertgroupsRequestInnerRulesInner` to `[]CreateLogsAlertgroupsPayloadRulesInner`
- **Deprecation:** The `GrafanaAdminPassword` and `GrafanaAdminUser` fields are now deprecated in `InstanceSensitiveData` model
- **Feature:** Add `GrafanaAdminEnabled` to `CreateInstancePayload` and `UpdateInstancePayload` models
- **Feature:** Add new field `record` in `UpdateAlertgroupsRequestInnerRulesInner` model
- **Feature:** Add `CertCheck` to `CertCheckResponse` model
- **Feature:** Add `HttpCheck` to `HttpCheckResponse` model
- **Feature:** Add new `CreateLogsAlertgroupsPayloadRulesInner` model
- **Feature:** Add `allowAssignGrafanaAdmin` to `GrafanaOauth` and `UpdateGrafanaConfigsPayloadGenericOauth` models
- **Feature:** Add `GrafanaAdminEnabled` to `InstanceSensitiveData` model
- **Feature:** Add new `PartialUpdateAlertrulesRequestInner` model

## v0.11.0
- **Deprecation:** The `JaegerHttpTracesUrl` field is now deprecated in all relevant models and will be removed after 9th April 2026. Use the new `JaegerHttpUrl` field instead.

## v0.10.1
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
