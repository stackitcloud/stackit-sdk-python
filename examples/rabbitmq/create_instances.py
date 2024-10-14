import os

from stackit.rabbitmq.api.default_api import DefaultApi
from stackit.rabbitmq.models.create_instance_payload import CreateInstancePayload

from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
storage_class = "premium-perf2-stackit"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get all offerings
response = client.list_offerings(project_id)

# Create instance using the first flvaor
create_instance_payload = CreateInstancePayload(
    instance_name="exampleInstance",
    plan_id=response.offerings[0].plans[0].id,
)
client.create_instance(project_id, create_instance_payload)
