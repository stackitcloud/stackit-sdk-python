import os

from stackit.mariadb.api.default_api import DefaultApi
from stackit.mariadb.models.create_instance_payload import CreateInstancePayload
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get all MariaDB offerings
offerings_response = client.list_offerings(project_id)

# Create an instance using the first offering
create_instance_payload = CreateInstancePayload(
    instanceName="exampleInstance",
    planId=offerings_response.offerings[0].plans[0].id,
)
client.create_instance(project_id, create_instance_payload)
