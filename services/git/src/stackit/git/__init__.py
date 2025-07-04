# coding: utf-8

# flake8: noqa

"""
    STACKIT Git API

    STACKIT Git management API.

    The version of the OpenAPI document: 1beta.0.4
    Contact: git@stackit.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long


__version__ = "1.0.0"

# import apis into sdk package
from stackit.git.api.default_api import DefaultApi
from stackit.git.api_client import ApiClient

# import ApiClient
from stackit.git.api_response import ApiResponse
from stackit.git.configuration import HostConfiguration
from stackit.git.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from stackit.git.models.create_instance_payload import CreateInstancePayload
from stackit.git.models.flavor import Flavor
from stackit.git.models.generic_error_response import GenericErrorResponse
from stackit.git.models.instance import Instance
from stackit.git.models.internal_server_error_response import (
    InternalServerErrorResponse,
)
from stackit.git.models.list_flavors import ListFlavors
from stackit.git.models.list_instances import ListInstances
from stackit.git.models.unauthorized_response import UnauthorizedResponse
