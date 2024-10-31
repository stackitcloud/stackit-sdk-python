import os
from http import HTTPStatus

from stackit.core.configuration import Configuration
from stackit.core.wait import WaitConfig
from stackit.dns.api.default_api import DefaultApi
from stackit.dns.models.create_zone_payload import CreateZonePayload
from stackit.dns.wait import wait_for_create_zone

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)


# Create a new DNS zone
create_zone_response = client.create_zone(
    create_zone_payload=CreateZonePayload(name="myZone", dnsName="testZone.com"), project_id=project_id
)
zone1_id = create_zone_response.zone.id
zone2_id = client.create_zone(
    create_zone_payload=CreateZonePayload(name="myZone2", dnsName="testZone2.com"), project_id=project_id
).zone.id
zone3_id = client.create_zone(
    create_zone_payload=CreateZonePayload(name="myZone3", dnsName="testZone3.com"), project_id=project_id
).zone.id

# Wait for the zone to be fully created.
wait_for_zone_response = wait_for_create_zone(client, project_id, zone1_id)

# Optionally the wait configuration can be adjusted. It's possible to adjust just one of the parameters....
wait_for_zone_response = wait_for_create_zone(client, project_id, zone2_id, WaitConfig(sleep_before_wait=5))

# ... or all of them
wait_for_zone_response = wait_for_create_zone(
    client,
    project_id,
    zone3_id,
    WaitConfig(
        sleep_before_wait=6,
        throttle=10,
        timeout=10,
        temp_error_retry_limit=10,
        retry_http_error_status_codes=[HTTPStatus.BAD_GATEWAY, HTTPStatus.GATEWAY_TIMEOUT],
    ),
)

# Delete all of the zones again
delete_zone_message = client.delete_zone(project_id, zone1_id)
delete_zone_message = client.delete_zone(project_id, zone2_id)
delete_zone_message = client.delete_zone(project_id, zone3_id)
