# coding: utf-8

# flake8: noqa

"""
    STACKIT PostgreSQL Flex API

    This is the documentation for the STACKIT postgres service

    The version of the OpenAPI document: 2.0.0
    Contact: support@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long


__version__ = "1.0.0"

# import apis into sdk package
from stackit.postgresflex.api.default_api import DefaultApi
from stackit.postgresflex.api_client import ApiClient

# import ApiClient
from stackit.postgresflex.api_response import ApiResponse
from stackit.postgresflex.configuration import HostConfiguration
from stackit.postgresflex.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from stackit.postgresflex.models.acl import ACL
from stackit.postgresflex.models.api_configuration import ApiConfiguration
from stackit.postgresflex.models.api_extension_config_load_response import (
    ApiExtensionConfigLoadResponse,
)
from stackit.postgresflex.models.api_extension_configure_response import (
    ApiExtensionConfigureResponse,
)
from stackit.postgresflex.models.api_extension_delete_response import (
    ApiExtensionDeleteResponse,
)
from stackit.postgresflex.models.api_extension_list import ApiExtensionList
from stackit.postgresflex.models.api_extension_load_response import (
    ApiExtensionLoadResponse,
)
from stackit.postgresflex.models.api_install_response import ApiInstallResponse
from stackit.postgresflex.models.api_installed_list_response import (
    ApiInstalledListResponse,
)
from stackit.postgresflex.models.backup import Backup
from stackit.postgresflex.models.clone_instance_payload import CloneInstancePayload
from stackit.postgresflex.models.clone_instance_response import CloneInstanceResponse
from stackit.postgresflex.models.create_database_payload import CreateDatabasePayload
from stackit.postgresflex.models.create_instance_payload import CreateInstancePayload
from stackit.postgresflex.models.create_instance_response import CreateInstanceResponse
from stackit.postgresflex.models.create_user_payload import CreateUserPayload
from stackit.postgresflex.models.create_user_response import CreateUserResponse
from stackit.postgresflex.models.error import Error
from stackit.postgresflex.models.extensions_configuration import ExtensionsConfiguration
from stackit.postgresflex.models.extensions_extension_list_response import (
    ExtensionsExtensionListResponse,
)
from stackit.postgresflex.models.extensions_new_config import ExtensionsNewConfig
from stackit.postgresflex.models.flavor import Flavor
from stackit.postgresflex.models.get_backup_response import GetBackupResponse
from stackit.postgresflex.models.get_user_response import GetUserResponse
from stackit.postgresflex.models.instance import Instance
from stackit.postgresflex.models.instance_create_database_response import (
    InstanceCreateDatabaseResponse,
)
from stackit.postgresflex.models.instance_data_point import InstanceDataPoint
from stackit.postgresflex.models.instance_database import InstanceDatabase
from stackit.postgresflex.models.instance_host import InstanceHost
from stackit.postgresflex.models.instance_host_metric import InstanceHostMetric
from stackit.postgresflex.models.instance_list_databases_response import (
    InstanceListDatabasesResponse,
)
from stackit.postgresflex.models.instance_list_instance import InstanceListInstance
from stackit.postgresflex.models.instance_metrics_response import (
    InstanceMetricsResponse,
)
from stackit.postgresflex.models.instance_response import InstanceResponse
from stackit.postgresflex.models.list_backups_response import ListBackupsResponse
from stackit.postgresflex.models.list_flavors_response import ListFlavorsResponse
from stackit.postgresflex.models.list_instances_response import ListInstancesResponse
from stackit.postgresflex.models.list_storages_response import ListStoragesResponse
from stackit.postgresflex.models.list_users_response import ListUsersResponse
from stackit.postgresflex.models.list_users_response_item import ListUsersResponseItem
from stackit.postgresflex.models.list_versions_response import ListVersionsResponse
from stackit.postgresflex.models.partial_update_instance_payload import (
    PartialUpdateInstancePayload,
)
from stackit.postgresflex.models.partial_update_instance_response import (
    PartialUpdateInstanceResponse,
)
from stackit.postgresflex.models.partial_update_user_payload import (
    PartialUpdateUserPayload,
)
from stackit.postgresflex.models.postgres_database_parameter import (
    PostgresDatabaseParameter,
)
from stackit.postgresflex.models.postgres_database_parameter_response import (
    PostgresDatabaseParameterResponse,
)
from stackit.postgresflex.models.reset_user_response import ResetUserResponse
from stackit.postgresflex.models.storage import Storage
from stackit.postgresflex.models.storage_range import StorageRange
from stackit.postgresflex.models.update_backup_schedule_payload import (
    UpdateBackupSchedulePayload,
)
from stackit.postgresflex.models.update_instance_payload import UpdateInstancePayload
from stackit.postgresflex.models.update_user_payload import UpdateUserPayload
from stackit.postgresflex.models.user import User
from stackit.postgresflex.models.user_response import UserResponse
