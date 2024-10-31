from typing import List
from unittest.mock import Mock

import pytest

from stackit.dns.models.record import Record
from stackit.dns.models.record_set import RecordSet
from stackit.dns.models.record_set_response import RecordSetResponse
from stackit.dns.models.zone import Zone
from stackit.dns.models.zone_response import ZoneResponse
from stackit.dns.wait import *


def zone_response(state: str, zone_id: str) -> ZoneResponse:
    return ZoneResponse(
        zone=Zone(
            id=zone_id,
            acl="acl",
            creationFinished="creationFinished",
            creationStarted="creationStarted",
            defaultTTL=60,
            dnsName="dnsName",
            expireTime=60,
            name="name",
            negativeCache=60,
            primaryNameServer="fqdn",
            refreshTime=60,
            retryTime=60,
            serialNumber=123456,
            state=state,
            type="primary",
            updateFinished="updateFinished",
            updateStarted="updateStarted",
            visibility="public",
        )
    )


def rr_set_response(state: str, rr_set_id: str) -> ZoneResponse:
    return RecordSetResponse(
        rrset=RecordSet(
            creationFinished="creationFinished",
            creationStarted="creationStarted",
            id=rr_set_id,
            name="name",
            records=[Record(id="id", content="content")],
            state=state,
            ttl=60,
            type="A",
            updateFinished="updateFinished",
            updateStarted="updateStarted",
        )
    )


@pytest.mark.parametrize(
    "zone_id,project_id,api_response", [("zone_id", "project_id", zone_response("CREATING", "incorrect_zone_id"))]
)
def test_create_zone_wait_handler_fails_for_wrong_id(zone_id: str, project_id: str, api_response: ZoneResponse):
    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(ValueError, match="ID of zone in return not equal to ID of requested zone."):
        wait_for_create_zone(api_client, project_id, zone_id)


@pytest.mark.parametrize(
    "zone_id,project_id,expected_api_response",
    [("zone_id", "project_id", zone_response("CREATE_SUCCEEDED", "zone_id"))],
)
def test_create_zone_wait_handler_retuns_response(zone_id: str, project_id: str, expected_api_response: ZoneResponse):
    api_client = Mock()
    api_client.get_zone.return_value = expected_api_response

    response = wait_for_create_zone(api_client, project_id, zone_id)

    assert response == expected_api_response


@pytest.mark.parametrize(
    "zone_id,project_id,api_response", [("zone_id", "project_id", zone_response("CREATE_FAILED", "zone_id"))]
)
def test_create_zone_wait_handler_fails_for_failure(zone_id: str, project_id: str, api_response: ZoneResponse):
    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(Exception, match=f"Create failed for zone with ID {zone_id}"):
        wait_for_create_zone(api_client, project_id, zone_id)


@pytest.mark.parametrize(
    "zone_id,project_id,api_responses",
    [
        (
            "zone_id",
            "project_id",
            [
                zone_response("CREATING", "zone_id"),
                zone_response("CREATING", "zone_id"),
                zone_response("CREATE_SUCCEEDED", "zone_id"),
            ],
        )
    ],
)
def test_create_zone_wait_handler_waits(zone_id: str, project_id: str, api_responses: List[ZoneResponse]):
    api_client = Mock()
    api_client.get_zone.side_effect = api_responses

    assert wait_for_create_zone(api_client, project_id, zone_id) == api_responses[-1]


@pytest.mark.parametrize(
    "zone_id,project_id,api_response", [("zone_id", "project_id", zone_response("UPDATING", "incorrect_zone_id"))]
)
def test_wait_for_partial_update_zone_fails_for_wrong_id(zone_id: str, project_id: str, api_response: ZoneResponse):
    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(ValueError, match="ID of zone in return not equal to ID of requested zone."):
        wait_for_partial_update_zone(api_client, project_id, zone_id)


@pytest.mark.parametrize(
    "zone_id,project_id,expected_api_response",
    [("zone_id", "project_id", zone_response("UPDATE_SUCCEEDED", "zone_id"))],
)
def test_wait_for_partial_update_zone_handler_retuns_response(
    zone_id: str, project_id: str, expected_api_response: ZoneResponse
):
    api_client = Mock()
    api_client.get_zone.return_value = expected_api_response

    response = wait_for_partial_update_zone(api_client, project_id, zone_id)

    assert response == expected_api_response


@pytest.mark.parametrize(
    "zone_id,project_id,api_response", [("zone_id", "project_id", zone_response("UPDATE_FAILED", "zone_id"))]
)
def test_wait_for_partial_update_zone_handler_fails_for_failure(
    zone_id: str, project_id: str, api_response: ZoneResponse
):
    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(Exception, match=f"Update failed for zone with ID {zone_id}"):
        wait_for_partial_update_zone(api_client, project_id, zone_id)


@pytest.mark.parametrize(
    "zone_id,project_id,api_responses",
    [
        (
            "zone_id",
            "project_id",
            [
                zone_response("UPDATING", "zone_id"),
                zone_response("UPDATING", "zone_id"),
                zone_response("UPDATE_SUCCEEDED", "zone_id"),
            ],
        )
    ],
)
def test_wait_for_partial_update_zone_waits(zone_id: str, project_id: str, api_responses: List[ZoneResponse]):
    api_client = Mock()
    api_client.get_zone.side_effect = api_responses

    assert wait_for_partial_update_zone(api_client, project_id, zone_id) == api_responses[-1]


@pytest.mark.parametrize(
    "zone_id,project_id,api_response", [("zone_id", "project_id", zone_response("DELETING", "incorrect_zone_id"))]
)
def test_wait_for_delete_zone_fails_for_wrong_id(zone_id: str, project_id: str, api_response: ZoneResponse):
    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(ValueError, match="ID of zone in return not equal to ID of requested zone."):
        wait_for_delete_zone(api_client, project_id, zone_id)


@pytest.mark.parametrize(
    "zone_id,project_id,expected_api_response",
    [("zone_id", "project_id", zone_response("DELETE_SUCCEEDED", "zone_id"))],
)
def test_wait_for_delete_zone_handler_retuns_response(
    zone_id: str, project_id: str, expected_api_response: ZoneResponse
):
    api_client = Mock()
    api_client.get_zone.return_value = expected_api_response

    response = wait_for_delete_zone(api_client, project_id, zone_id)

    assert response == expected_api_response


@pytest.mark.parametrize(
    "zone_id,project_id,api_response", [("zone_id", "project_id", zone_response("DELETE_FAILED", "zone_id"))]
)
def test_wait_for_delete_zone_handler_fails_for_failure(zone_id: str, project_id: str, api_response: ZoneResponse):
    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(Exception, match=f"Delete failed for zone with ID {zone_id}"):
        wait_for_delete_zone(api_client, project_id, zone_id)


@pytest.mark.parametrize(
    "zone_id,project_id,api_responses",
    [
        (
            "zone_id",
            "project_id",
            [
                zone_response("DELETING", "zone_id"),
                zone_response("DELETING", "zone_id"),
                zone_response("DELETE_SUCCEEDED", "zone_id"),
            ],
        )
    ],
)
def test_wait_for_delete_zone_zone_waits(zone_id: str, project_id: str, api_responses: List[ZoneResponse]):
    api_client = Mock()
    api_client.get_zone.side_effect = api_responses

    assert wait_for_delete_zone(api_client, project_id, zone_id) == api_responses[-1]


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_response",
    [("rr_set_id", "zone_id", "project_id", rr_set_response("CREATING", "incorrect_rr_set_id"))],
)
def test_wait_for_create_recordset_fails_for_wrong_id(
    rr_set_id: str, zone_id: str, project_id: str, api_response: RecordSetResponse
):
    api_client = Mock()
    api_client.get_record_set.return_value = api_response

    with pytest.raises(ValueError, match="ID of rrset in return not equal to ID of requested rrset."):
        wait_for_create_recordset(api_client, project_id, zone_id, rr_set_id)


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_response",
    [("rr_set_id", "zone_id", "project_id", rr_set_response("CREATE_FAILED", "rr_set_id"))],
)
def test_wait_for_create_recordset_fails_for_failure(
    rr_set_id: str, zone_id: str, project_id: str, api_response: RecordSetResponse
):
    api_client = Mock()
    api_client.get_record_set.return_value = api_response

    with pytest.raises(Exception, match=f"Create failed for rrset with ID {rr_set_id}"):
        wait_for_create_recordset(api_client, project_id, zone_id, rr_set_id)


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_responses",
    [
        (
            "rr_set_id",
            "zone_id",
            "project_id",
            [
                rr_set_response("CREATING", "rr_set_id"),
                rr_set_response("CREATING", "rr_set_id"),
                rr_set_response("CREATE_SUCCEEDED", "rr_set_id"),
            ],
        )
    ],
)
def test_wait_for_create_recordset_waits(
    rr_set_id: str, zone_id: str, project_id: str, api_responses: List[RecordSetResponse]
):
    api_client = Mock()
    api_client.get_record_set.side_effect = api_responses

    assert wait_for_create_recordset(api_client, project_id, zone_id, rr_set_id) == api_responses[-1]


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_response",
    [("rr_set_id", "zone_id", "project_id", rr_set_response("UPDATING", "incorrect_rr_set_id"))],
)
def test_wait_for_partial_update_recordset_fails_for_wrong_id(
    rr_set_id: str, zone_id: str, project_id: str, api_response: RecordSetResponse
):
    api_client = Mock()
    api_client.get_record_set.return_value = api_response

    with pytest.raises(ValueError, match="ID of rrset in return not equal to ID of requested rrset."):
        wait_for_partial_update_recordset(api_client, project_id, zone_id, rr_set_id)


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_response",
    [("rr_set_id", "zone_id", "project_id", rr_set_response("UPDATE_FAILED", "rr_set_id"))],
)
def test_wait_for_partial_update_recordset_fails_for_failure(
    rr_set_id: str, zone_id: str, project_id: str, api_response: RecordSetResponse
):
    api_client = Mock()
    api_client.get_record_set.return_value = api_response

    with pytest.raises(Exception, match=f"Update failed for rrset with ID {rr_set_id}"):
        wait_for_partial_update_recordset(api_client, project_id, zone_id, rr_set_id)


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_responses",
    [
        (
            "rr_set_id",
            "zone_id",
            "project_id",
            [
                rr_set_response("UPDATING", "rr_set_id"),
                rr_set_response("UPDATING", "rr_set_id"),
                rr_set_response("UPDATE_SUCCEEDED", "rr_set_id"),
            ],
        )
    ],
)
def test_wait_for_partial_update_recordset_waits(
    rr_set_id: str, zone_id: str, project_id: str, api_responses: List[RecordSetResponse]
):
    api_client = Mock()
    api_client.get_record_set.side_effect = api_responses

    assert wait_for_partial_update_recordset(api_client, project_id, zone_id, rr_set_id) == api_responses[-1]


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_response",
    [("rr_set_id", "zone_id", "project_id", rr_set_response("DELETING", "incorrect_rr_set_id"))],
)
def test_wait_for_delete_recordset_fails_for_wrong_id(
    rr_set_id: str, zone_id: str, project_id: str, api_response: RecordSetResponse
):
    api_client = Mock()
    api_client.get_record_set.return_value = api_response

    with pytest.raises(ValueError, match="ID of rrset in return not equal to ID of requested rrset."):
        wait_for_delete_recordset(api_client, project_id, zone_id, rr_set_id)


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_response",
    [("rr_set_id", "zone_id", "project_id", rr_set_response("DELETE_FAILED", "rr_set_id"))],
)
def test_wait_for_delete_recordset_fails_for_failure(
    rr_set_id: str, zone_id: str, project_id: str, api_response: RecordSetResponse
):
    api_client = Mock()
    api_client.get_record_set.return_value = api_response

    with pytest.raises(Exception, match=f"Delete failed for rrset with ID {rr_set_id}"):
        wait_for_delete_recordset(api_client, project_id, zone_id, rr_set_id)


@pytest.mark.parametrize(
    "rr_set_id,zone_id,project_id,api_responses",
    [
        (
            "rr_set_id",
            "zone_id",
            "project_id",
            [
                rr_set_response("DELETING", "rr_set_id"),
                rr_set_response("DELETING", "rr_set_id"),
                rr_set_response("DELETE_SUCCEEDED", "rr_set_id"),
            ],
        )
    ],
)
def test_wait_for_delete_recordset_waits(
    rr_set_id: str, zone_id: str, project_id: str, api_responses: List[RecordSetResponse]
):
    api_client = Mock()
    api_client.get_record_set.side_effect = api_responses

    assert wait_for_delete_recordset(api_client, project_id, zone_id, rr_set_id) == api_responses[-1]
