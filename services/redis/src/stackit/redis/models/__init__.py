# coding: utf-8

# flake8: noqa
"""
    STACKIT Redis API

    The STACKIT Redis API provides endpoints to list service offerings, manage service instances and service credentials within STACKIT portal projects.

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from stackit.redis.models.backup import Backup
from stackit.redis.models.create_backup_response_item import CreateBackupResponseItem
from stackit.redis.models.create_instance_payload import CreateInstancePayload
from stackit.redis.models.create_instance_response import CreateInstanceResponse
from stackit.redis.models.credentials import Credentials
from stackit.redis.models.credentials_list_item import CredentialsListItem
from stackit.redis.models.credentials_response import CredentialsResponse
from stackit.redis.models.error import Error
from stackit.redis.models.get_metrics_response import GetMetricsResponse
from stackit.redis.models.instance import Instance
from stackit.redis.models.instance_last_operation import InstanceLastOperation
from stackit.redis.models.instance_parameters import InstanceParameters
from stackit.redis.models.instance_schema import InstanceSchema
from stackit.redis.models.list_backups_response import ListBackupsResponse
from stackit.redis.models.list_credentials_response import ListCredentialsResponse
from stackit.redis.models.list_instances_response import ListInstancesResponse
from stackit.redis.models.list_offerings_response import ListOfferingsResponse
from stackit.redis.models.list_restores_response import ListRestoresResponse
from stackit.redis.models.model_schema import ModelSchema
from stackit.redis.models.offering import Offering
from stackit.redis.models.partial_update_instance_payload import (
    PartialUpdateInstancePayload,
)
from stackit.redis.models.plan import Plan
from stackit.redis.models.raw_credentials import RawCredentials
from stackit.redis.models.restore import Restore
from stackit.redis.models.trigger_restore_response import TriggerRestoreResponse
from stackit.redis.models.update_backups_config_payload import (
    UpdateBackupsConfigPayload,
)
from stackit.redis.models.update_backups_config_response import (
    UpdateBackupsConfigResponse,
)
