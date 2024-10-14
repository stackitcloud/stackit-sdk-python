import os

from stackit.sqlserverflex.api.default_api import DefaultApi
from stackit.sqlserverflex.models.create_instance_payload import CreateInstancePayload
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
storage_class = "premium-perf2-stackit"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get possible flavors
flavor_response = client.list_flavors(project_id)

# Create instance using the first flvaor
create_instance_payload = CreateInstancePayload(
    name="my-instance",
    flavorId=flavor_response.flavors[0].id,
)
client.create_instance(project_id, create_instance_payload)
