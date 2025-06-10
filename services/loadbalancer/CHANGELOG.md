## v0.3.0 (2025-06-10)
- **Feature:** Add new field `target_security_group` in `LoadBalancer` Model

## v0.2.4 (2025-06-02)
- **Improvement:** Adjusted `GetQuotaResponse` and `RESTResponseType` message

## v0.2.3 (2025-05-09)
- **Feature:** Update user-agent header

## v0.2.2 (2025-03-18)
- Adapted to minor API changes

## v0.2.1 (2025-01-14)

- **Bugfix**: `configuration.py` region adjustment was missing

## v0.2.0 (2025-01-13)

- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.0 (2024-12-04)

- Manage your STACKIT Load Balancer resources
- [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/loadbalancer)
