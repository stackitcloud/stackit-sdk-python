import os

from stackit.core.configuration import Configuration
from stackit.dns.api.default_api import DefaultApi
from stackit.dns.models.create_record_set_payload import CreateRecordSetPayload
from stackit.dns.models.create_zone_payload import CreateZonePayload
from stackit.dns.models.record_payload import RecordPayload
from stackit.dns.wait import (
    wait_for_create_recordset,
    wait_for_create_zone,
    wait_for_delete_recordset,
    wait_for_delete_zone,
)

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)


# Create a new DNS zone
create_zone_response = client.create_zone(
    create_zone_payload=CreateZonePayload(name="myZone", dnsName="testZone.com"), project_id=project_id
)
zone_id = create_zone_response.zone.id

# Wait for the zone to be fully created
wait_for_zone_response = wait_for_create_zone(client, project_id, zone_id)

# Create a DNS record in the newly created DNS zone
create_record_response = client.create_record_set(
    project_id,
    zone_id,
    CreateRecordSetPayload(
        name="a",
        records=[
            RecordPayload(content="192.168.0.1"),  # Will go nowhere
        ],
        type="A",
    ),
)
rr_set_id = create_record_response.rrset.id

# Wait for the DNS record to be fully created
wait_for_rr_set_record_response = wait_for_create_recordset(client, project_id, zone_id, rr_set_id)

# delete newly created recordset
delete_rr_set_message = client.delete_record_set(project_id, zone_id, rr_set_id)

# Wait for rr_set deletion
wait_for_rr_set_deletion_response = wait_for_delete_recordset(client, project_id, zone_id, rr_set_id)

# Delete newly created DNS zone
delete_zone_message = client.delete_zone(project_id, zone_id)

# Wait for deletion of DNS zone
wait_for_zone_deletion_response = wait_for_delete_zone(client, project_id, zone_id)
