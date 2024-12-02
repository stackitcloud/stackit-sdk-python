import os

from stackit.dns.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
zone_id = "ZONE_ID"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

client.delete_zone(project_id=project_id, zone_id=zone_id)
