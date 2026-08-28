import os

from stackit.core.configuration import Configuration
from stackit.dremio.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
region_id = os.getenv("REGION", "eu01")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all Dremio instances
print(client.list_dremio_instances(project_id, region_id))
