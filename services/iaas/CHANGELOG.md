## v0.7.0
- **Docs:** Improved descriptions of properties in structs with their possible values
- **Feature:** Add `Agent` field to `CreateImagePayload`, `UpdateImagePayload` and `Image` model
- **Feature:** Add `Encrypted` and `EncryptionsParameters` fields to `CreateVolumePayload` model

## v0.6.0
- **Version**: Minimal version is now python 3.9

## v0.5.5
- **Improvement:** Add proper noqa comments for docstrings
- **Improvement:** Update type annotations for better type safety

## v0.5.4
- **Improvement:** Increase max length of `machine_type` and `volume_performance_class` fields from 63 to 127 characters in API methods
- **Improvement:** Increase max length of `name` fields from 63 to 127 characters for various models:
    - `AffinityGroup`, `Backup`, `BootVolume`, `CreateAffinityGroupPayload`, `CreateBackupPayload`
    `CreateImagePayload`, `CreateNetworkAreaPayload`, `CreateNetworkPayload`, `CreateNicPayload`
    `CreateSecurityGroupPayload`, `CreateServerPayload`, `CreateSnapshotPayload`, `CreateVolumePayload`
    `Image`, `MachineType`, `Nic`, `PartialUpdateNetworkAreaPayload`, `PartialUpdateNetworkPayload`
    `ResizeServerPayload`, `SecurityGroup`, `Server`, `ServerNetwork`, `Snapshot`
    `UpdateBackupPayload`, `UpdateImagePayload`, `UpdateNicPayload`, `UpdateSecurityGroupPayload`
    `UpdateServerPayload`, `UpdateSnapshotPayload`, `UpdateVolumePayload`, `Volume`, `VolumePerformanceClass`
- **Improvement:** Update regular expression pattern for name validation to allow more flexible naming conventions

## v0.5.3 (2025-06-12)
- Increase max length of description from 127 to 255 for 
    - Security groups: `BaseSecurityGroupRule`, `CreateSecurityGroupPayload`, `CreateSecurityGroupRulePayload`, `SecurityGroup`, `SecurityGroupRule`, `UpdateSecurityGroupPayload`
    - Volumes: `CreateVolumePayload`, `UpdateVolumePayload`, `Volume`, `VolumePerformanceClass`
    - `MachineType`
- Set max length of description of `Network` to 255
- Update the description of `Server` and `CreateServerPayload` status field to include new possible value `PAUSED`

## v0.5.2 (2025-05-19)
- **Improvement:** Update descriptions

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
