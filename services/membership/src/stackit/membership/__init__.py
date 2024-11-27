# coding: utf-8

# flake8: noqa

"""
    STACKIT Membership API

    The Membership API is used to manage memberships, roles and permissions of STACKIT resources, like projects, folders, organizations and other resources.

    The version of the OpenAPI document: 2.0
    Contact: SIT-STACKIT-Core-Platform-Security@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long


__version__ = "1.0.0"

# import apis into sdk package
from stackit.membership.api.default_api import DefaultApi
from stackit.membership.api_client import ApiClient

# import ApiClient
from stackit.membership.api_response import ApiResponse
from stackit.membership.configuration import HostConfiguration
from stackit.membership.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from stackit.membership.models.add_members_payload import AddMembersPayload
from stackit.membership.models.add_roles_payload import AddRolesPayload
from stackit.membership.models.add_roles_payload_item import AddRolesPayloadItem
from stackit.membership.models.consistency import Consistency
from stackit.membership.models.create_resource_payload import CreateResourcePayload
from stackit.membership.models.create_resource_response import CreateResourceResponse
from stackit.membership.models.delete_resource_response import DeleteResourceResponse
from stackit.membership.models.delete_subject_response import DeleteSubjectResponse
from stackit.membership.models.enforce_permission_payload import (
    EnforcePermissionPayload,
)
from stackit.membership.models.error_response import ErrorResponse
from stackit.membership.models.existing_permission import ExistingPermission
from stackit.membership.models.list_members_response import ListMembersResponse
from stackit.membership.models.list_permissions_response import ListPermissionsResponse
from stackit.membership.models.list_subject_ids_response import ListSubjectIdsResponse
from stackit.membership.models.list_subjects_response import ListSubjectsResponse
from stackit.membership.models.list_user_memberships_response import (
    ListUserMembershipsResponse,
)
from stackit.membership.models.list_user_permissions_response import (
    ListUserPermissionsResponse,
)
from stackit.membership.models.member import Member
from stackit.membership.models.members_response import MembersResponse
from stackit.membership.models.permission import Permission
from stackit.membership.models.permission_request import PermissionRequest
from stackit.membership.models.remove_members_payload import RemoveMembersPayload
from stackit.membership.models.remove_role_request import RemoveRoleRequest
from stackit.membership.models.remove_roles_payload import RemoveRolesPayload
from stackit.membership.models.resource import Resource
from stackit.membership.models.role import Role
from stackit.membership.models.roles_response import RolesResponse
from stackit.membership.models.subject import Subject
from stackit.membership.models.transfer_subject_memberships_payload import (
    TransferSubjectMembershipsPayload,
)
from stackit.membership.models.user_membership import UserMembership
from stackit.membership.models.user_permission import UserPermission
from stackit.membership.models.user_resources_response import UserResourcesResponse
from stackit.membership.models.validate_child_members_payload import (
    ValidateChildMembersPayload,
)
from stackit.membership.models.write_schema_payload import WriteSchemaPayload
from stackit.membership.models.write_schema_response import WriteSchemaResponse
from stackit.membership.models.zookie import Zookie
