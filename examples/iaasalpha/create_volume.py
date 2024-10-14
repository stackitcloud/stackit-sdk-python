import os

from stackit.iaasalpha.api.default_api import DefaultApi
from stackit.iaasalpha.models.create_volume_payload import CreateVolumePayload
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Create a volume
payload = CreateVolumePayload(
    name="example-volume",
    availability_zone="eu01-1",
    size=10,
)
client.create_volume(project_id, payload)
