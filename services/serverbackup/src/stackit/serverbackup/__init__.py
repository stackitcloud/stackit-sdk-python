# coding: utf-8

# flake8: noqa

"""
    STACKIT Server Backup Management API

    API endpoints for Server Backup Operations on STACKIT Servers.

    The version of the OpenAPI document: 2.0
    Contact: support@stackit.de
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
    "BackupJob",
    "BackupPolicy",
    "BackupPolicyBackupProperties",
    "BackupProperties",
    "BackupSchedule",
    "BackupVolumeBackupsInner",
    "CreateBackupPayload",
    "CreateBackupSchedulePayload",
    "EnableServiceResourcePayload",
    "ErrorResponse",
    "GetBackupPoliciesResponse",
    "GetBackupSchedulesResponse",
    "GetBackupServiceResponse",
    "GetBackupsListResponse",
    "RestoreBackupPayload",
    "RestoreVolumeBackupPayload",
    "UpdateBackupSchedulePayload",
]

# import apis into sdk package
from stackit.serverbackup.api.default_api import DefaultApi as DefaultApi
from stackit.serverbackup.api_client import ApiClient as ApiClient

# import ApiClient
from stackit.serverbackup.api_response import ApiResponse as ApiResponse
from stackit.serverbackup.configuration import HostConfiguration as HostConfiguration
from stackit.serverbackup.exceptions import ApiAttributeError as ApiAttributeError
from stackit.serverbackup.exceptions import ApiException as ApiException
from stackit.serverbackup.exceptions import ApiKeyError as ApiKeyError
from stackit.serverbackup.exceptions import ApiTypeError as ApiTypeError
from stackit.serverbackup.exceptions import ApiValueError as ApiValueError
from stackit.serverbackup.exceptions import OpenApiException as OpenApiException

# import models into sdk package
from stackit.serverbackup.models.backup import Backup as Backup
from stackit.serverbackup.models.backup_job import BackupJob as BackupJob
from stackit.serverbackup.models.backup_policy import BackupPolicy as BackupPolicy
from stackit.serverbackup.models.backup_policy_backup_properties import (
    BackupPolicyBackupProperties as BackupPolicyBackupProperties,
)
from stackit.serverbackup.models.backup_properties import (
    BackupProperties as BackupProperties,
)
from stackit.serverbackup.models.backup_schedule import BackupSchedule as BackupSchedule
from stackit.serverbackup.models.backup_volume_backups_inner import (
    BackupVolumeBackupsInner as BackupVolumeBackupsInner,
)
from stackit.serverbackup.models.create_backup_payload import (
    CreateBackupPayload as CreateBackupPayload,
)
from stackit.serverbackup.models.create_backup_schedule_payload import (
    CreateBackupSchedulePayload as CreateBackupSchedulePayload,
)
from stackit.serverbackup.models.enable_service_resource_payload import (
    EnableServiceResourcePayload as EnableServiceResourcePayload,
)
from stackit.serverbackup.models.error_response import ErrorResponse as ErrorResponse
from stackit.serverbackup.models.get_backup_policies_response import (
    GetBackupPoliciesResponse as GetBackupPoliciesResponse,
)
from stackit.serverbackup.models.get_backup_schedules_response import (
    GetBackupSchedulesResponse as GetBackupSchedulesResponse,
)
from stackit.serverbackup.models.get_backup_service_response import (
    GetBackupServiceResponse as GetBackupServiceResponse,
)
from stackit.serverbackup.models.get_backups_list_response import (
    GetBackupsListResponse as GetBackupsListResponse,
)
from stackit.serverbackup.models.restore_backup_payload import (
    RestoreBackupPayload as RestoreBackupPayload,
)
from stackit.serverbackup.models.restore_volume_backup_payload import (
    RestoreVolumeBackupPayload as RestoreVolumeBackupPayload,
)
from stackit.serverbackup.models.update_backup_schedule_payload import (
    UpdateBackupSchedulePayload as UpdateBackupSchedulePayload,
)
