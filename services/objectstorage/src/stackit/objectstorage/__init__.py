# coding: utf-8

# flake8: noqa

"""
    STACKIT Object Storage API

    STACKIT API to manage the Object Storage 

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long


__version__ = "1.0.0"

# import apis into sdk package
from stackit.objectstorage.api.default_api import DefaultApi
from stackit.objectstorage.api_client import ApiClient

# import ApiClient
from stackit.objectstorage.api_response import ApiResponse
from stackit.objectstorage.configuration import HostConfiguration
from stackit.objectstorage.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from stackit.objectstorage.models.access_key import AccessKey
from stackit.objectstorage.models.bucket import Bucket
from stackit.objectstorage.models.create_access_key_payload import (
    CreateAccessKeyPayload,
)
from stackit.objectstorage.models.create_access_key_response import (
    CreateAccessKeyResponse,
)
from stackit.objectstorage.models.create_bucket_response import CreateBucketResponse
from stackit.objectstorage.models.create_credentials_group_payload import (
    CreateCredentialsGroupPayload,
)
from stackit.objectstorage.models.create_credentials_group_response import (
    CreateCredentialsGroupResponse,
)
from stackit.objectstorage.models.credentials_group import CredentialsGroup
from stackit.objectstorage.models.delete_access_key_response import (
    DeleteAccessKeyResponse,
)
from stackit.objectstorage.models.delete_bucket_response import DeleteBucketResponse
from stackit.objectstorage.models.delete_credentials_group_response import (
    DeleteCredentialsGroupResponse,
)
from stackit.objectstorage.models.detailed_error import DetailedError
from stackit.objectstorage.models.error_message import ErrorMessage
from stackit.objectstorage.models.get_bucket_response import GetBucketResponse
from stackit.objectstorage.models.http_validation_error import HTTPValidationError
from stackit.objectstorage.models.list_access_keys_response import (
    ListAccessKeysResponse,
)
from stackit.objectstorage.models.list_buckets_response import ListBucketsResponse
from stackit.objectstorage.models.list_credentials_groups_response import (
    ListCredentialsGroupsResponse,
)
from stackit.objectstorage.models.location_inner import LocationInner
from stackit.objectstorage.models.project_scope import ProjectScope
from stackit.objectstorage.models.project_status import ProjectStatus
from stackit.objectstorage.models.validation_error import ValidationError
