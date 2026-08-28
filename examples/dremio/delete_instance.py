import os

from stackit.core.configuration import Configuration
from stackit.dremio.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
region_id = os.getenv("REGION", "eu01")
dremio_id = "DREMIO_ID"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Delete a Dremio instance
client.delete_dremio_instance(project_id, region_id, dremio_id)
