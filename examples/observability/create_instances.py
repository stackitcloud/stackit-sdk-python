import os

from stackit.observability.api.default_api import DefaultApi
from stackit.observability.models.create_instance_payload import CreateInstancePayload
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get all offerings
response = client.v1_projects_offerings_list(project_id)

# Create instance using the first found offer
create_instance_payload = CreateInstancePayload(
    name="myInstance",
    planId=response.plans[0].id,
)
client.create_instance(project_id, create_instance_payload)
