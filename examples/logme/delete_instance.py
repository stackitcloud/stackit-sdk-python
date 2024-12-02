import os

from stackit.logme.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
instance_id = "INSTANCE_ID"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Delete an instance
client.delete_instance(project_id, instance_id)
