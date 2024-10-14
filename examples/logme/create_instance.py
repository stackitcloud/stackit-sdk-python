import os

from stackit.logme.api.default_api import DefaultApi
from stackit.logme.models.create_instance_payload import CreateInstancePayload
from stackit.logme.models.instance_parameters import InstanceParameters
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get the logme offerings for your project
offerings_response = client.list_offerings(project_id)

# Take the first offering an create a new instance
create_instance_payload = CreateInstancePayload(
    instanceName="exampleInstance",
    parameters=InstanceParameters(),
    planId=offerings_response.offerings[0].plans[0].id,
)
print(client.create_instance(project_id, create_instance_payload))
