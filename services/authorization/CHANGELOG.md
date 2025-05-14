## v0.2.4 (2025-05-13)
- **Bugfix:** Updated regex validator

## v0.2.3 (2025-05-09)
- **Feature:** Update user-agent header

## v0.2.2 (2025-01-21)
- **Bugfix:** Revert back to global URL configuration

## v0.2.1 (2025-01-14)
- **Bugfix**: `configuration.py` region adjustment was missing

## v0.2.0 (2025-01-13)
- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.1.0 (2024-12-04)
- Manage authorization of your STACKIT resources
