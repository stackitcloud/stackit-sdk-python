import os

from stackit.secretsmanager.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all secretsmanager instances
print(client.list_instances(project_id))
