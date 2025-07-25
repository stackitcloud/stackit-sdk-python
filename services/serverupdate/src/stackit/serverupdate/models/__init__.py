# coding: utf-8

# flake8: noqa
"""
    STACKIT Server Update Management API

    API endpoints for Server Update Operations on STACKIT Servers.

    The version of the OpenAPI document: 2.0
    Contact: support@stackit.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from stackit.serverupdate.models.create_update_payload import CreateUpdatePayload
from stackit.serverupdate.models.create_update_schedule_payload import (
    CreateUpdateSchedulePayload,
)
from stackit.serverupdate.models.enable_service_resource_payload import (
    EnableServiceResourcePayload,
)
from stackit.serverupdate.models.error_response import ErrorResponse
from stackit.serverupdate.models.get_update_policies_response import (
    GetUpdatePoliciesResponse,
)
from stackit.serverupdate.models.get_update_schedules_response import (
    GetUpdateSchedulesResponse,
)
from stackit.serverupdate.models.get_update_service_response import (
    GetUpdateServiceResponse,
)
from stackit.serverupdate.models.get_updates_list_response import GetUpdatesListResponse
from stackit.serverupdate.models.update import Update
from stackit.serverupdate.models.update_policy import UpdatePolicy
from stackit.serverupdate.models.update_schedule import UpdateSchedule
from stackit.serverupdate.models.update_schedule_create_request import (
    UpdateScheduleCreateRequest,
)
from stackit.serverupdate.models.update_update_schedule_payload import (
    UpdateUpdateSchedulePayload,
)
