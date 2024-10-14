import os

from stackit.iaas.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
organization_id = os.getenv("ORGANIZATION_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)


# List all network areas of the organization
print(client.list_network_areas(organization_id))
