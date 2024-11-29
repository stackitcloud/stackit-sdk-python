import os

from stackit.core.configuration import Configuration
from stackit.rabbitmq.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
instance_id = "INSTANCE_ID"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Delete an instance
client.delete_instance(project_id, instance_id)
