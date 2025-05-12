## v0.5.1 (2025-05-09)
- **Feature:** Update user-agent header

## v0.5.0 (2025-03-24)
- **Improvement:** Upgrading from IaaS **beta** endpoints to **v1**
- **Feature:** Add new method to filter `ListMachineTypes`: `Filter`

## v0.4.0 (2025-02-27)

- **Feature:** Add method to list all public ip ranges: `list_public_ip_ranges`
- Add size attribute to image model
- Add CPU architecture attribute to image config model

## v0.3.1 (2025-01-14)

- **Bugfix**: `configuration.py` region adjustment was missing

## v0.3.0 (2025-01-13)

- **Breaking Change:**: `get_host_from_settings` returns an error if a region is specified for a global URL.

STACKIT will move to a new way of specifying regions, where the region is provided as a function argument instead of being set in the client configuration. Once all services have migrated, the methods to specify the region in the client configuration will be removed.

## v0.2.0 (2024-12-23)

- **Feature:** Add new methods to manage affinity groups: `create_affinity_group`, `delete_affinity_group`, `get_affinity_group`, and `list_affinity_group`
- **Feature:** Add new methods to manage backups: `create_backup`, `delete_backup`, `get_backup`, `list_backup`, `restore_backup`, `execute_backup`, `update_backup`
- **Feature:** Add new methods to manage images: `create_image`, `delete_image`, `get_image`, `list_image`, `update_image`
- **Feature:** Add new methods to manage imageshares: `delete_image_share`, `get_image_share`, `set_image_share`, `update_image_share`
- **Feature:** Add new methods to manage imageshare consumers: `delete_image_share_consumer`, `get_image_share_consumer`, `set_image_share`, `update_image_share`
- **Feature:** Add new methods to manage project NICs: `get_project_nic`, `list_project_nics`
- **Feature:** Add new methods to manage snapshots: `create_snapshot`, `delete_snapshot`, `get_snapshot`, `list_snapshot`, `update_snapshot`

## v0.1.0 (2024-12-04)

- Manage your STACKIT Infrastructure as a Service (IaaS) resources
- [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/iaas)
