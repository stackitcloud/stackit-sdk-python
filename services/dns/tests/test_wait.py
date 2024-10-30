from unittest.mock import Mock

import pytest

from stackit.dns.models.zone import Zone
from stackit.dns.models.zone_response import ZoneResponse
from stackit.dns.wait import *


def test_create_zone_wait_handler_fails_for_wrong_id():
    zone_id = "zone_id"
    project_id = "project_id"

    api_response = ZoneResponse(
        zone=Zone(
            id="incorrect_id",
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
            state="CREATING",
            type="primary",
            updateFinished="updateFinished",
            updateStarted="updateStarted",
            visibility="public",
        )
    )

    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(ValueError, match="ID of zone in return not equal to ID of requested zone."):
        wait_for_create_zone(api_client, project_id, zone_id)


def test_create_zone_wait_handler_retuns_response():
    zone_id = "zone_id"
    project_id = "project_id"

    expected_api_response = ZoneResponse(
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
            state="CREATE_SUCCEEDED",
            type="primary",
            updateFinished="updateFinished",
            updateStarted="updateStarted",
            visibility="public",
        )
    )

    api_client = Mock()
    api_client.get_zone.return_value = expected_api_response

    response = wait_for_create_zone(api_client, project_id, zone_id)

    assert response == expected_api_response


def test_create_zone_wait_handler_fails_for_failure():
    zone_id = "zone_id"
    project_id = "project_id"

    api_response = ZoneResponse(
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
            state="CREATE_FAILED",
            type="primary",
            updateFinished="updateFinished",
            updateStarted="updateStarted",
            visibility="public",
        )
    )

    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(Exception, match=f"Create failed for zone with id {zone_id}"):
        wait_for_create_zone(api_client, project_id, zone_id)


def test_create_zone_wait_handler_waits():
    zone_id = "zone_id"
    project_id = "project_id"

    api_response = ZoneResponse(
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
            state="CREATING",
            type="primary",
            updateFinished="updateFinished",
            updateStarted="updateStarted",
            visibility="public",
        )
    )

    api_client = Mock()
    api_client.get_zone.return_value = api_response

    with pytest.raises(TimeoutError, match="Wait has timed out"):
        wait_for_create_zone(api_client, project_id, zone_id, timeout=1)
