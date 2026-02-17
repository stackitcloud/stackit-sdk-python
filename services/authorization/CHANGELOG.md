## v0.7.0
- **Breaking change:** removed operation `get_assignable_subjects` and related models `assignable_subject`, `list_assignable_subjects_response`

## v0.6.0
- **Feature:** Add new methods for managing roles: `AddRole`, `DeleteRole`, `GetRole`, `UpdateRole`

## v0.5.0
- Add new `etag` attribute to `Role` model class

## v0.4.1
- **Bugfix:** Prevent year 0 timestamp issue

## v0.4.0
- **Feature**: Add support for assignable subjects 

## v0.3.0
- **Version**: Minimal version is now python 3.9

## v0.2.5
- **Internal:** Improve deserializing and error types

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
