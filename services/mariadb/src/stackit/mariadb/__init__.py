# coding: utf-8

# flake8: noqa

"""
    STACKIT MariaDB API

    The STACKIT MariaDB API provides endpoints to list service offerings, manage service instances and service credentials within STACKIT portal projects.

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "DefaultApi",
    "ApiResponse",
    "ApiClient",
    "HostConfiguration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "Backup",
    "CreateBackupResponseItem",
    "CreateInstancePayload",
    "CreateInstanceResponse",
    "Credentials",
    "CredentialsListItem",
    "CredentialsResponse",
    "Error",
    "GetMetricsResponse",
    "Instance",
    "InstanceLastOperation",
    "InstanceParameters",
    "InstanceSchema",
    "ListBackupsResponse",
    "ListCredentialsResponse",
    "ListInstancesResponse",
    "ListOfferingsResponse",
    "ListRestoresResponse",
    "ModelSchema",
    "Offering",
    "PartialUpdateInstancePayload",
    "Plan",
    "RawCredentials",
    "Restore",
    "TriggerRestoreResponse",
    "UpdateBackupsConfigPayload",
    "UpdateBackupsConfigResponse",
]

# import apis into sdk package
from stackit.mariadb.api.default_api import DefaultApi as DefaultApi
from stackit.mariadb.api_client import ApiClient as ApiClient

# import ApiClient
from stackit.mariadb.api_response import ApiResponse as ApiResponse
from stackit.mariadb.configuration import HostConfiguration as HostConfiguration
from stackit.mariadb.exceptions import ApiAttributeError as ApiAttributeError
from stackit.mariadb.exceptions import ApiException as ApiException
from stackit.mariadb.exceptions import ApiKeyError as ApiKeyError
from stackit.mariadb.exceptions import ApiTypeError as ApiTypeError
from stackit.mariadb.exceptions import ApiValueError as ApiValueError
from stackit.mariadb.exceptions import OpenApiException as OpenApiException

# import models into sdk package
from stackit.mariadb.models.backup import Backup as Backup
from stackit.mariadb.models.create_backup_response_item import (
    CreateBackupResponseItem as CreateBackupResponseItem,
)
from stackit.mariadb.models.create_instance_payload import (
    CreateInstancePayload as CreateInstancePayload,
)
from stackit.mariadb.models.create_instance_response import (
    CreateInstanceResponse as CreateInstanceResponse,
)
from stackit.mariadb.models.credentials import Credentials as Credentials
from stackit.mariadb.models.credentials_list_item import (
    CredentialsListItem as CredentialsListItem,
)
from stackit.mariadb.models.credentials_response import (
    CredentialsResponse as CredentialsResponse,
)
from stackit.mariadb.models.error import Error as Error
from stackit.mariadb.models.get_metrics_response import (
    GetMetricsResponse as GetMetricsResponse,
)
from stackit.mariadb.models.instance import Instance as Instance
from stackit.mariadb.models.instance_last_operation import (
    InstanceLastOperation as InstanceLastOperation,
)
from stackit.mariadb.models.instance_parameters import (
    InstanceParameters as InstanceParameters,
)
from stackit.mariadb.models.instance_schema import InstanceSchema as InstanceSchema
from stackit.mariadb.models.list_backups_response import (
    ListBackupsResponse as ListBackupsResponse,
)
from stackit.mariadb.models.list_credentials_response import (
    ListCredentialsResponse as ListCredentialsResponse,
)
from stackit.mariadb.models.list_instances_response import (
    ListInstancesResponse as ListInstancesResponse,
)
from stackit.mariadb.models.list_offerings_response import (
    ListOfferingsResponse as ListOfferingsResponse,
)
from stackit.mariadb.models.list_restores_response import (
    ListRestoresResponse as ListRestoresResponse,
)
from stackit.mariadb.models.model_schema import ModelSchema as ModelSchema
from stackit.mariadb.models.offering import Offering as Offering
from stackit.mariadb.models.partial_update_instance_payload import (
    PartialUpdateInstancePayload as PartialUpdateInstancePayload,
)
from stackit.mariadb.models.plan import Plan as Plan
from stackit.mariadb.models.raw_credentials import RawCredentials as RawCredentials
from stackit.mariadb.models.restore import Restore as Restore
from stackit.mariadb.models.trigger_restore_response import (
    TriggerRestoreResponse as TriggerRestoreResponse,
)
from stackit.mariadb.models.update_backups_config_payload import (
    UpdateBackupsConfigPayload as UpdateBackupsConfigPayload,
)
from stackit.mariadb.models.update_backups_config_response import (
    UpdateBackupsConfigResponse as UpdateBackupsConfigResponse,
)
