import os

from stackit.redis.api.default_api import DefaultApi
from stackit.redis.models.create_instance_payload import CreateInstancePayload
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

config = Configuration()
client = DefaultApi(config)

# check out all available offerings
available_offerings = client.list_offerings(project_id)

# take the first available plan id
offering_id = available_offerings.offerings[0].plans[0].id
payload = CreateInstancePayload(
    instance_name="Test Instance",
    plan_id=offering_id,
)

# create the instance
response = client.create_instance(project_id, payload)
instance_id = response.instance_id

print(f"Instance with id:{instance_id} has been created.")
