import os

from stackit.sqlserverflex.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all sqlserverflex instances
print(client.list_instances(project_id))
