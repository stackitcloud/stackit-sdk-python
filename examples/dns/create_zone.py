import os

from stackit.dns.api.default_api import DefaultApi
from stackit.dns.models.create_zone_payload import CreateZonePayload
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Create a new DNS zone
create_zone_payload = CreateZonePayload(name="myZone", dnsName="testZone.com")
create_zone_response = client.create_zone(create_zone_payload=create_zone_payload, project_id=project_id)

print(create_zone_payload)
