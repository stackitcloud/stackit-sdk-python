## v0.3.2 (2025-05-14)
- **Deprecated:** `lbapplication` service is deprecated and no longer maintained. Use the `alb` service instead

## v0.3.1 (2025-03-18)
- Adapted to minor API changes

## v0.3.0 (2025-02-07)

- **Bugfix**: Set type from interface to int64 of `HealthyThreshold`, `UnhealthyThreshold`, `MaxLoadBalancers`, `Port`, `MaxConnections`, `Code` and `TargetPort`

## v0.2.1 (2025-01-14)

- **Bugfix**: `configuration.py` region adjustment was missing

## v0.2.0 (2025-01-13)

- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.0 (2024-12-23)

- Manage your STACKIT Load Balancer applications
