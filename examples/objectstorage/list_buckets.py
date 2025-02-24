import os

from stackit.objectstorage.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all ObjectStorage buckets instances
print(client.list_buckets(project_id))
