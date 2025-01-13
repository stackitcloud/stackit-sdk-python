## Release (2025-XX-XX)

### Highlights

- `certificates`: [v0.1.0](services/certificates/CHANGELOG.md#v010-2024-12-23)
  - Manage your STACKIT Load Balancer certificates
- `lbapplication`: [v0.1.0](services/lbapplication/CHANGELOG.md#v010-2024-12-23)
  - Manage your STACKIT Load Balancer applications
- `iaas`: [v0.2.0](services/iaas/CHANGELOG.md#v020-2024-12-23)
  - **Feature:** Add new methods to manage affinity groups: `create_affinity_group`, `delete_affinity_group`, `get_affinity_group`, and `list_affinity_group`
  - **Feature:** Add new methods to manage backups: `create_backup`, `delete_backup`, `get_backup`, `list_backup`, `restore_backup`, `execute_backup`, `update_backup`
  - **Feature:** Add new methods to manage images: `create_image`, `delete_image`, `get_image`, `list_image`, `update_image`
  - **Feature:** Add new methods to manage imageshares: `delete_image_share`, `get_image_share`, `set_image_share`, `update_image_share`
  - **Feature:** Add new methods to manage imageshare consumers: `delete_image_share_consumer`, `get_image_share_consumer`, `set_image_share`, `update_image_share`
  - **Feature:** Add new methods to manage project NICs: `get_project_nic`, `list_project_nics`
  - **Feature:** Add new methods to manage snapshots: `create_snapshot`, `delete_snapshot`, `get_snapshot`, `list_snapshot`, `update_snapshot`
- `serverupdate`: [v0.1.1](services/serverupdate/CHANGELOG.md#v011-2024-12-23)
  - **Bugfix:** `Id` field of `Update` model is now of type `int64` (was `string`)
- `stackitmarketplace`: [v0.1.0](services/stackitmarketplace/CHANGELOG.md#v010-2025-01-13)
  - **New**: STACKIT Marketplace module can be used to manage the STACKIT Marketplace.

## Release (2024-12-04)

This is the first GitHub release of the STACKIT Python SDK.

### Highlights

List of modules:

- `core`: [v0.1.0](core/CHANGELOG.md#v010-2024-12-04)
  - The core module offers functionality, such as authorization and configuration, to be used together with the Python SDK service modules
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/core)
- `authorization`: [v0.1.0](services/authorization/CHANGELOG.md#v010-2024-12-04)
  - Manage authorization of your STACKIT resources
- `dns`: [v0.1.0](services/dns/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT DNS resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/dns)
- `iaas`: [v0.1.0](services/iaas/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Infrastructure as a Service (IaaS) resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/iaas)
- `loadbalancer`: [v0.1.0](services/loadbalancer/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Load Balancer resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/loadbalancer)
- `logme`: [v0.1.0](services/logme/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Logme resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/logme)
- `mariadb`: [v0.1.0](services/mariadb/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT MariaDB resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/mariadb)
- `mongodbflex`: [v0.1.0](services/mongodbflex/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT MongoDB Flex resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/mongodbflex)
- `objectstorage`: [v0.1.0](services/objectstorage/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Object Storage resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/objectstorage)
- `opensearch`: [v0.1.0](services/opensearch/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT OpenSearch resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/opensearch)
- `postgresflex`: [v0.1.0](services/postgresflex/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT PostgreSQL Flex resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/postgresflex)
- `rabbitmq`: [v0.1.0](services/rabbitmq/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT RabbitMQ resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/rabbitmq)
- `redis`: [v0.1.0](services/redis/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Redis resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/redis)
- `resourcemanager`: [v0.1.0](services/resourcemanager/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT resources such as projects, organizations and folders
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/resourcemanager)
- `runcommand`: [v0.1.0](services/runcommand/CHANGELOG.md#v010-2024-12-04)
  - STACKIT Run Command module can be used to run remote commands and custom scripts on VMs
- `secretsmanager`: [v0.1.0](services/secretsmanager/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Secrets Manager resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/secretsmanager)
- `serverupdate`: [v0.1.0](services/serverupdate/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Server Backups
- `serverbackup`: [v0.1.0](services/serverbackup/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Server Updates
- `serviceaccount`: [v0.1.0](services/serviceaccount/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT service accounts
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/serviceaccount)
- `serviceenablement`: [v0.1.0](services/serviceenablement/CHANGELOG.md#v010-2024-12-04)
  - STACKIT Service Enablement module can be used to enable services
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/serviceenablement)
- `ske`: [v0.1.0](services/ske/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT Kubernetes Engine resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/ske)
- `sqlserverflex`: [v0.1.0](services/sqlserverflex/CHANGELOG.md#v010-2024-12-04)
  - Manage your STACKIT SQLServer Flex resources
  - [Usage example](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples/sqlserverflex)
