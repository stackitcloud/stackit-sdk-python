import os

from stackit.dns.api.default_api import DefaultApi
from stackit.dns.models.create_record_set_payload import CreateRecordSetPayload
from stackit.dns.models.record_payload import RecordPayload
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

zones = client.list_zones(project_id)

# Get first active zone
zone_id = [zone.id for zone in zones.zones if zone.active][0]

# Create a DNS recors in the first DNS zone
create_recordset_payload = CreateRecordSetPayload(
    name="a",
    records=[
        RecordPayload(content="192.168.0.1"),  # Will go nowhere
    ],
    type="A",
)
create_record_response = client.create_record_set(project_id, zone_id, create_recordset_payload)

# Get the DNS record for the newly create DNS zone
print(
    client.get_record_set(
        project_id=project_id,
        zone_id=zone_id,
        rr_set_id=create_record_response.rrset.id,
    )
)
