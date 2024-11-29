import os

from stackit.core.configuration import Configuration
from stackit.redis.api.default_api import DefaultApi
from stackit.redis.models.create_instance_payload import CreateInstancePayload

project_id = os.getenv("PROJECT_ID")

config = Configuration()
client = DefaultApi(config)

# Check out all available offerings
available_offerings = client.list_offerings(project_id)

# Take the first available plan id
offering_id = available_offerings.offerings[0].plans[0].id
payload = CreateInstancePayload(
    instance_name="test-instance",
    plan_id=offering_id,
)

# Create the instance
instance = client.create_instance(project_id, payload)
print("Created instance with ID: " + instance.instance_id)
