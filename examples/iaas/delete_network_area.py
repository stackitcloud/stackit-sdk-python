import os

from stackit.iaas.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

organization_id = os.getenv("ORGANIZATION_ID")
network_id = "NETWORK_ID"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

client.delete_network_area(organization_id, network_id)
