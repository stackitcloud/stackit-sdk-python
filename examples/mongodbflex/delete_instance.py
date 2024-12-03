import os

from stackit.mongodbflex.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

tag = "tag"
project_id = os.getenv("PROJECT_ID")
instance_id = "INSTANCE_ID"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

client.delete_instance(project_id, instance_id)
