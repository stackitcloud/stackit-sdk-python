## v1.0.0
- **Breaking Change:** Add required `region` parameter to most API methods in `DefaultApi` class.
- **Breaking Change:** Removal of API methods from `DefaultApi` class: `list_snapshots`, `update_image_scope_local`, `update_image_scope_public`.
- **Feature:** Add new API methods to `DefaultApi` class: 
    - `add_routes_to_routing_table`
    - `add_routing_table_to_area`
    - `create_network_area_region`
    - `delete_network_area_region`
    - `delete_route_from_routing_table`
    - `delete_routing_table_from_area`
    - `get_network_area_region`
    - `get_route_of_routing_table`
    - `get_routing_table_of_area`
    - `image_from_volume`
    - `list_network_area_regions`
    - `list_routes_of_routing_table`
    - `list_routing_tables_of_area`
    - `list_snapshots_in_project`
    - `update_network_area_region`
    - `update_route_of_routing_table`
    - `update_routing_table_of_area`
- Update of regex validators for model class attributes
    - Update regex validators for `ip` attribute in `PublicIp`, `UpdatePublicIPPayload`, `CreatePublicIPPayload` model classes
    - Update regex validators for `gateway` attribute in `UpdateNetworkIPv4Body`, `UpdateNetworkIPv6Body` model classes
- **Feature:** New model classes
    - Network area: 
        - `RegionalArea`, `RegionalAreaListResponse`
        - `CreateNetworkAreaRegionPayload`
        - `RegionalAreaIPv4`, `UpdateRegionalAreaIPv4`
    - Routing tables:
        - `RoutingTable`, `RoutingTableListResponse`
        - `AddRoutesToRoutingTablePayload`
        - `AddRoutingTableToAreaPayload`
        - `UpdateRouteOfRoutingTablePayload`, `UpdateRoutingTableOfAreaPayload`
    - Routes: 
        - `RouteDestination`, `DestinationCIDRv4`, `DestinationCIDRv6`
        - `RouteNexthop`, `NexthopInternet`, `NexthopIPv4`, `NexthopIPv6`, `NexthopBlackhole`
    - Network (IPv4): `NetworkIPv4`, `CreateNetworkIPv4`, `CreateNetworkIPv4WithPrefix`, `CreateNetworkIPv4WithPrefixLength`
    - Network (IPv6): `NetworkIPv6`, `CreateNetworkIPv6`, `CreateNetworkIPv6WithPrefix`, `CreateNetworkIPv6WithPrefixLength`
    - other: `CreateServerPayloadAllOfNetworking`, `ImageFromVolumePayload`, `UpdateNetworkAreaRegionPayload`, `ServerNetworking`
- **Feature:** New attributes in model classes
    - Add `region` attribute to `PublicNetwork` model class
    - Add `destination` attribute to `Route` model class
    - Add `import_progress` attribute to model classes `CreateImagePayload`, `Image`
    - Add `encrypted` attribute to model class `Backup`
    - Add `ipv4`, `ipv6`, `routing_table_id` attributes to model class `CreateNetworkPayload`, `PartialUpdateNetworkPayload`
    - Add `ipv4`, `ipv6` `routing_table_id` attributes to model class `Network`
    - Add `items` attribute to `CreateNetworkAreaRoutePayload` model class
- **Breaking Change:**: Removal of model classes 
    - Network area: `Area`, `AreaConfig`, `CreateAreaAddressFamily`, `UpdateAreaAddressFamily`, `AreaPrefixConfigIPv4`, `CreateAreaIPv4`, `UpdateAreaIPv4` 
    - Server: `CreateServerPayloadNetworking`
    - Network: `CreateNetworkIPv4Body`, `NetworkAreaIPv4`, `CreateNetworkAddressFamily`, `UpdateNetworkAddressFamily`, `CreateNetworkIPv6Body`
- **Breaking Change:** Renaming of ID attributes in model classes
    - Renaming of attribute `network_range_id` to `id` in `NetworkRange` model class
    - Renaming of attribute `route_id` to `id` in `Route` model class
    - Renaming of attribute `network_id` to `id` in `Network` model class
    - Renaming of attribute `area_id` to `id` in `NetworkArea` model class
    - Renaming of attribute `project_id` to `id` in `Project` model class
- **Breaking Change:** Renaming of `state` attribute to `status` in model classes `Network`, `NetworkArea`, `Project`
- **Breaking Change:** Type changes of attributes of model classes
    - Change type of `networking` attribute from `CreateServerPayloadNetworking` to `ServerNetworking` in `Server` model class
    - Change type of `networking` attribute from `CreateServerPayloadNetworking` to `CreateServerPayloadAllOfNetworking` in `CreateServerPayload` model class
    - Change type of `nexthop` attribute from string to `RouteNexthop` in `Route` model class
- **Breaking Change:** 
    - Remove attribute `prefix` from `Route` model class
    - Remove attribute `ipv4` from `NetworkArea`, `CreateNetworkAreaRoutePayload` model classes
    - Remove attribute `address_family` from `CreateNetworkAreaPayload`, `CreateNetworkPayload`, `PartialUpdateNetworkAreaPayload`, `PartialUpdateNetworkPayload` model classes
    - Remove attributes `gateway`, `gatewayv6`, `nameservers`, `nameservers_v6`, `prefixes`, `prefixes_v6`, `public_ip` from `Network` model class
    - Remove attribute `openstack_project_id` from `Project` model class

## v0.9.0
- Add `created_at` and `updated_at` attribute to `SecurityGroupRule`, `BaseSecurityGroupRule` and `CreateSecurityGroupRulePayload` model classes
- Add `description` attribute to `NIC`, `CreateNicPayload` and `UpdateNicPayload` model classes
- New model class `ServerAgent`
- Add `agent` and `description` attribute to `Server` and `CreateServerPayload` model classes

## v0.8.1
- **Internal:** Add workaround to fix upstream OpenAPI generator issue where regex patterns include leading/trailing slashes that need to be removed for validation in `AllowedAddressesInner`, `AreaId`, and `CreateProtocol` models

## v0.8.0
- **Feature:** Add new method to get project details `GetProjectDetails`

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
