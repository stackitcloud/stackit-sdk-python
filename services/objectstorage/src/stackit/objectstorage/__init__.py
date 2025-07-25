# coding: utf-8

# flake8: noqa

"""
    STACKIT Object Storage API

    STACKIT API to manage the Object Storage 

    The version of the OpenAPI document: 2.0.1
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
    "AccessKey",
    "Bucket",
    "CreateAccessKeyPayload",
    "CreateAccessKeyResponse",
    "CreateBucketResponse",
    "CreateCredentialsGroupPayload",
    "CreateCredentialsGroupResponse",
    "CredentialsGroup",
    "DeleteAccessKeyResponse",
    "DeleteBucketResponse",
    "DeleteCredentialsGroupResponse",
    "DetailedError",
    "ErrorMessage",
    "GetBucketResponse",
    "HTTPValidationError",
    "ListAccessKeysResponse",
    "ListBucketsResponse",
    "ListCredentialsGroupsResponse",
    "LocationInner",
    "ProjectScope",
    "ProjectStatus",
    "ValidationError",
]

# import apis into sdk package
from stackit.objectstorage.api.default_api import DefaultApi as DefaultApi
from stackit.objectstorage.api_client import ApiClient as ApiClient

# import ApiClient
from stackit.objectstorage.api_response import ApiResponse as ApiResponse
from stackit.objectstorage.configuration import HostConfiguration as HostConfiguration
from stackit.objectstorage.exceptions import ApiAttributeError as ApiAttributeError
from stackit.objectstorage.exceptions import ApiException as ApiException
from stackit.objectstorage.exceptions import ApiKeyError as ApiKeyError
from stackit.objectstorage.exceptions import ApiTypeError as ApiTypeError
from stackit.objectstorage.exceptions import ApiValueError as ApiValueError
from stackit.objectstorage.exceptions import OpenApiException as OpenApiException

# import models into sdk package
from stackit.objectstorage.models.access_key import AccessKey as AccessKey
from stackit.objectstorage.models.bucket import Bucket as Bucket
from stackit.objectstorage.models.create_access_key_payload import (
    CreateAccessKeyPayload as CreateAccessKeyPayload,
)
from stackit.objectstorage.models.create_access_key_response import (
    CreateAccessKeyResponse as CreateAccessKeyResponse,
)
from stackit.objectstorage.models.create_bucket_response import (
    CreateBucketResponse as CreateBucketResponse,
)
from stackit.objectstorage.models.create_credentials_group_payload import (
    CreateCredentialsGroupPayload as CreateCredentialsGroupPayload,
)
from stackit.objectstorage.models.create_credentials_group_response import (
    CreateCredentialsGroupResponse as CreateCredentialsGroupResponse,
)
from stackit.objectstorage.models.credentials_group import (
    CredentialsGroup as CredentialsGroup,
)
from stackit.objectstorage.models.delete_access_key_response import (
    DeleteAccessKeyResponse as DeleteAccessKeyResponse,
)
from stackit.objectstorage.models.delete_bucket_response import (
    DeleteBucketResponse as DeleteBucketResponse,
)
from stackit.objectstorage.models.delete_credentials_group_response import (
    DeleteCredentialsGroupResponse as DeleteCredentialsGroupResponse,
)
from stackit.objectstorage.models.detailed_error import DetailedError as DetailedError
from stackit.objectstorage.models.error_message import ErrorMessage as ErrorMessage
from stackit.objectstorage.models.get_bucket_response import (
    GetBucketResponse as GetBucketResponse,
)
from stackit.objectstorage.models.http_validation_error import (
    HTTPValidationError as HTTPValidationError,
)
from stackit.objectstorage.models.list_access_keys_response import (
    ListAccessKeysResponse as ListAccessKeysResponse,
)
from stackit.objectstorage.models.list_buckets_response import (
    ListBucketsResponse as ListBucketsResponse,
)
from stackit.objectstorage.models.list_credentials_groups_response import (
    ListCredentialsGroupsResponse as ListCredentialsGroupsResponse,
)
from stackit.objectstorage.models.location_inner import LocationInner as LocationInner
from stackit.objectstorage.models.project_scope import ProjectScope as ProjectScope
from stackit.objectstorage.models.project_status import ProjectStatus as ProjectStatus
from stackit.objectstorage.models.validation_error import (
    ValidationError as ValidationError,
)
