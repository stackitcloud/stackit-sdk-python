import os

from stackit.core.configuration import Configuration
from stackit.dremio.api.default_api import DefaultApi
from stackit.dremio.models.create_dremio_instance_payload import CreateDremioInstancePayload

project_id = os.getenv("PROJECT_ID")
region_id = os.getenv("REGION", "eu01")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Create a new Dremio instance
create_dremio_instance_payload = CreateDremioInstancePayload(
    displayName="exampleInstance",
)
instance = client.create_dremio_instance(project_id, region_id, create_dremio_instance_payload)
print("Created Dremio instance with ID: " + str(instance.id))
