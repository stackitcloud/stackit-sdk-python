# coding: utf-8

# flake8: noqa

"""
    Application Load Balancer API

    ### DEPRECATED! This service, lb-application, is no longer maintained. Please use the alb service, version v2beta2 instead  This API offers an interface to provision and manage load balancing servers in your STACKIT project. It also has the possibility of pooling target servers for load balancing purposes.  For each application load balancer provided, two VMs are deployed in your OpenStack project subject to a fee.

    The version of the OpenAPI document: 1beta.0.0
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
    "ActiveHealthCheck",
    "CertificateConfig",
    "CookiePersistence",
    "CreateCredentialsPayload",
    "CreateCredentialsResponse",
    "CreateLoadBalancerPayload",
    "CredentialsResponse",
    "GetCredentialsResponse",
    "GetQuotaResponse",
    "GetServiceStatusResponse",
    "GoogleProtobufAny",
    "HTTPConfig",
    "Header",
    "HttpHealthChecks",
    "ListCredentialsResponse",
    "ListLoadBalancersResponse",
    "ListPlansResponse",
    "Listener",
    "LoadBalancer",
    "LoadBalancerError",
    "LoadBalancerOptions",
    "LoadbalancerOptionAccessControl",
    "LoadbalancerOptionLogs",
    "LoadbalancerOptionMetrics",
    "LoadbalancerOptionObservability",
    "Matcher",
    "Network",
    "PlanDetails",
    "ProtocolOptionsHTTPS",
    "QueryParameters",
    "Rule",
    "Status",
    "Target",
    "TargetPool",
    "UpdateCredentialsPayload",
    "UpdateCredentialsResponse",
    "UpdateLoadBalancerPayload",
    "UpdateTargetPoolPayload",
]

# import apis into sdk package
from stackit.lbapplication.api.default_api import DefaultApi as DefaultApi
from stackit.lbapplication.api_client import ApiClient as ApiClient

# import ApiClient
from stackit.lbapplication.api_response import ApiResponse as ApiResponse
from stackit.lbapplication.configuration import HostConfiguration as HostConfiguration
from stackit.lbapplication.exceptions import ApiAttributeError as ApiAttributeError
from stackit.lbapplication.exceptions import ApiException as ApiException
from stackit.lbapplication.exceptions import ApiKeyError as ApiKeyError
from stackit.lbapplication.exceptions import ApiTypeError as ApiTypeError
from stackit.lbapplication.exceptions import ApiValueError as ApiValueError
from stackit.lbapplication.exceptions import OpenApiException as OpenApiException

# import models into sdk package
from stackit.lbapplication.models.active_health_check import (
    ActiveHealthCheck as ActiveHealthCheck,
)
from stackit.lbapplication.models.certificate_config import (
    CertificateConfig as CertificateConfig,
)
from stackit.lbapplication.models.cookie_persistence import (
    CookiePersistence as CookiePersistence,
)
from stackit.lbapplication.models.create_credentials_payload import (
    CreateCredentialsPayload as CreateCredentialsPayload,
)
from stackit.lbapplication.models.create_credentials_response import (
    CreateCredentialsResponse as CreateCredentialsResponse,
)
from stackit.lbapplication.models.create_load_balancer_payload import (
    CreateLoadBalancerPayload as CreateLoadBalancerPayload,
)
from stackit.lbapplication.models.credentials_response import (
    CredentialsResponse as CredentialsResponse,
)
from stackit.lbapplication.models.get_credentials_response import (
    GetCredentialsResponse as GetCredentialsResponse,
)
from stackit.lbapplication.models.get_quota_response import (
    GetQuotaResponse as GetQuotaResponse,
)
from stackit.lbapplication.models.get_service_status_response import (
    GetServiceStatusResponse as GetServiceStatusResponse,
)
from stackit.lbapplication.models.google_protobuf_any import (
    GoogleProtobufAny as GoogleProtobufAny,
)
from stackit.lbapplication.models.header import Header as Header
from stackit.lbapplication.models.http_config import HTTPConfig as HTTPConfig
from stackit.lbapplication.models.http_health_checks import (
    HttpHealthChecks as HttpHealthChecks,
)
from stackit.lbapplication.models.list_credentials_response import (
    ListCredentialsResponse as ListCredentialsResponse,
)
from stackit.lbapplication.models.list_load_balancers_response import (
    ListLoadBalancersResponse as ListLoadBalancersResponse,
)
from stackit.lbapplication.models.list_plans_response import (
    ListPlansResponse as ListPlansResponse,
)
from stackit.lbapplication.models.listener import Listener as Listener
from stackit.lbapplication.models.load_balancer import LoadBalancer as LoadBalancer
from stackit.lbapplication.models.load_balancer_error import (
    LoadBalancerError as LoadBalancerError,
)
from stackit.lbapplication.models.load_balancer_options import (
    LoadBalancerOptions as LoadBalancerOptions,
)
from stackit.lbapplication.models.loadbalancer_option_access_control import (
    LoadbalancerOptionAccessControl as LoadbalancerOptionAccessControl,
)
from stackit.lbapplication.models.loadbalancer_option_logs import (
    LoadbalancerOptionLogs as LoadbalancerOptionLogs,
)
from stackit.lbapplication.models.loadbalancer_option_metrics import (
    LoadbalancerOptionMetrics as LoadbalancerOptionMetrics,
)
from stackit.lbapplication.models.loadbalancer_option_observability import (
    LoadbalancerOptionObservability as LoadbalancerOptionObservability,
)
from stackit.lbapplication.models.matcher import Matcher as Matcher
from stackit.lbapplication.models.network import Network as Network
from stackit.lbapplication.models.plan_details import PlanDetails as PlanDetails
from stackit.lbapplication.models.protocol_options_https import (
    ProtocolOptionsHTTPS as ProtocolOptionsHTTPS,
)
from stackit.lbapplication.models.query_parameters import (
    QueryParameters as QueryParameters,
)
from stackit.lbapplication.models.rule import Rule as Rule
from stackit.lbapplication.models.status import Status as Status
from stackit.lbapplication.models.target import Target as Target
from stackit.lbapplication.models.target_pool import TargetPool as TargetPool
from stackit.lbapplication.models.update_credentials_payload import (
    UpdateCredentialsPayload as UpdateCredentialsPayload,
)
from stackit.lbapplication.models.update_credentials_response import (
    UpdateCredentialsResponse as UpdateCredentialsResponse,
)
from stackit.lbapplication.models.update_load_balancer_payload import (
    UpdateLoadBalancerPayload as UpdateLoadBalancerPayload,
)
from stackit.lbapplication.models.update_target_pool_payload import (
    UpdateTargetPoolPayload as UpdateTargetPoolPayload,
)
