import os

from stackit.opensearch.api.default_api import DefaultApi
from stackit.opensearch.models.create_instance_payload import CreateInstancePayload
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get all offerings
response = client.list_offerings(project_id)

# Create instance using the first found offer
create_instance_payload = CreateInstancePayload(
    instanceName="myInstance",
    planId=response.offerings[0].plans[0].id,
)
client.create_instance(project_id, create_instance_payload)
