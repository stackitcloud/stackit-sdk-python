import os

from stackit.secretsmanager.api.default_api import DefaultApi
from stackit.secretsmanager.models.create_instance_payload import CreateInstancePayload

from stackit.core.configuration import Configuration


project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Create a new instance using the first flvaor
create_instance_payload = CreateInstancePayload(
    name="my-secrets-manager",
)
client.create_instance(project_id, create_instance_payload)
