# coding: utf-8

# flake8: noqa

"""
    STACKIT MongoDB Service API

    This is the documentation for the STACKIT MongoDB Flex Service API

    The version of the OpenAPI document: 1.0.0
    Contact: support@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long


__version__ = "1.0.0"

# import apis into sdk package
from stackit.mongodbflex.api.default_api import DefaultApi
from stackit.mongodbflex.api_client import ApiClient

# import ApiClient
from stackit.mongodbflex.api_response import ApiResponse
from stackit.mongodbflex.configuration import HostConfiguration
from stackit.mongodbflex.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from stackit.mongodbflex.models.acl import ACL
from stackit.mongodbflex.models.backup import Backup
from stackit.mongodbflex.models.backup_schedule import BackupSchedule
from stackit.mongodbflex.models.clone_instance_payload import CloneInstancePayload
from stackit.mongodbflex.models.clone_instance_response import CloneInstanceResponse
from stackit.mongodbflex.models.create_instance_payload import CreateInstancePayload
from stackit.mongodbflex.models.create_instance_response import CreateInstanceResponse
from stackit.mongodbflex.models.create_user_payload import CreateUserPayload
from stackit.mongodbflex.models.create_user_response import CreateUserResponse
from stackit.mongodbflex.models.data_point import DataPoint
from stackit.mongodbflex.models.error import Error
from stackit.mongodbflex.models.flavor import Flavor
from stackit.mongodbflex.models.get_backup_response import GetBackupResponse
from stackit.mongodbflex.models.get_instance_response import GetInstanceResponse
from stackit.mongodbflex.models.get_user_response import GetUserResponse
from stackit.mongodbflex.models.handlers_infra_flavor import HandlersInfraFlavor
from stackit.mongodbflex.models.handlers_infra_get_flavors_response import (
    HandlersInfraGetFlavorsResponse,
)
from stackit.mongodbflex.models.handlers_instances_get_instance_response import (
    HandlersInstancesGetInstanceResponse,
)
from stackit.mongodbflex.models.handlers_instances_slow_queries_response import (
    HandlersInstancesSlowQueriesResponse,
)
from stackit.mongodbflex.models.handlers_instances_suggested_indexes_response import (
    HandlersInstancesSuggestedIndexesResponse,
)
from stackit.mongodbflex.models.host import Host
from stackit.mongodbflex.models.host_metric import HostMetric
from stackit.mongodbflex.models.instance import Instance
from stackit.mongodbflex.models.instance_list_instance import InstanceListInstance
from stackit.mongodbflex.models.instance_response_user import InstanceResponseUser
from stackit.mongodbflex.models.list_backups_response import ListBackupsResponse
from stackit.mongodbflex.models.list_flavors_response import ListFlavorsResponse
from stackit.mongodbflex.models.list_instances_response import ListInstancesResponse
from stackit.mongodbflex.models.list_metrics_response import ListMetricsResponse
from stackit.mongodbflex.models.list_restore_jobs_response import (
    ListRestoreJobsResponse,
)
from stackit.mongodbflex.models.list_storages_response import ListStoragesResponse
from stackit.mongodbflex.models.list_user import ListUser
from stackit.mongodbflex.models.list_users_response import ListUsersResponse
from stackit.mongodbflex.models.list_versions_response import ListVersionsResponse
from stackit.mongodbflex.models.mongodbatlas_operation import MongodbatlasOperation
from stackit.mongodbflex.models.mongodbatlas_stats import MongodbatlasStats
from stackit.mongodbflex.models.partial_update_instance_payload import (
    PartialUpdateInstancePayload,
)
from stackit.mongodbflex.models.partial_update_user_payload import (
    PartialUpdateUserPayload,
)
from stackit.mongodbflex.models.restore_instance_payload import RestoreInstancePayload
from stackit.mongodbflex.models.restore_instance_response import RestoreInstanceResponse
from stackit.mongodbflex.models.restore_instance_status import RestoreInstanceStatus
from stackit.mongodbflex.models.shape import Shape
from stackit.mongodbflex.models.slow_query import SlowQuery
from stackit.mongodbflex.models.storage import Storage
from stackit.mongodbflex.models.storage_range import StorageRange
from stackit.mongodbflex.models.suggested_index import SuggestedIndex
from stackit.mongodbflex.models.update_backup_schedule_payload import (
    UpdateBackupSchedulePayload,
)
from stackit.mongodbflex.models.update_instance_payload import UpdateInstancePayload
from stackit.mongodbflex.models.update_instance_response import UpdateInstanceResponse
from stackit.mongodbflex.models.update_user_payload import UpdateUserPayload
from stackit.mongodbflex.models.user import User
