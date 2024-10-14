# coding: utf-8

# flake8: noqa

"""
    STACKIT DNS API

    This api provides dns

    The version of the OpenAPI document: 1.0
    Contact: stackit-dns@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long


__version__ = "1.0.0"

# import apis into sdk package
from stackit.dns.api.default_api import DefaultApi
from stackit.dns.api_client import ApiClient

# import ApiClient
from stackit.dns.api_response import ApiResponse
from stackit.dns.configuration import HostConfiguration
from stackit.dns.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from stackit.dns.models.clone_zone_payload import CloneZonePayload
from stackit.dns.models.create_label_payload import CreateLabelPayload
from stackit.dns.models.create_label_response import CreateLabelResponse
from stackit.dns.models.create_record_set_payload import CreateRecordSetPayload
from stackit.dns.models.create_zone_payload import CreateZonePayload
from stackit.dns.models.delete_label_response import DeleteLabelResponse
from stackit.dns.models.error_message import ErrorMessage
from stackit.dns.models.export_record_sets_payload import ExportRecordSetsPayload
from stackit.dns.models.import_record_sets_payload import ImportRecordSetsPayload
from stackit.dns.models.import_record_sets_response import ImportRecordSetsResponse
from stackit.dns.models.import_summary import ImportSummary
from stackit.dns.models.label import Label
from stackit.dns.models.list_labels_response import ListLabelsResponse
from stackit.dns.models.list_record_sets_response import ListRecordSetsResponse
from stackit.dns.models.list_zones_response import ListZonesResponse
from stackit.dns.models.message import Message
from stackit.dns.models.move_code_response import MoveCodeResponse
from stackit.dns.models.move_zone_payload import MoveZonePayload
from stackit.dns.models.partial_update_record_payload import PartialUpdateRecordPayload
from stackit.dns.models.partial_update_record_set_payload import (
    PartialUpdateRecordSetPayload,
)
from stackit.dns.models.partial_update_zone_payload import PartialUpdateZonePayload
from stackit.dns.models.record import Record
from stackit.dns.models.record_data_exchange import RecordDataExchange
from stackit.dns.models.record_payload import RecordPayload
from stackit.dns.models.record_set import RecordSet
from stackit.dns.models.record_set_response import RecordSetResponse
from stackit.dns.models.validate_move_code_payload import ValidateMoveCodePayload
from stackit.dns.models.zone import Zone
from stackit.dns.models.zone_data_exchange import ZoneDataExchange
from stackit.dns.models.zone_response import ZoneResponse
