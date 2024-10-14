import os

from stackit.secretsmanager.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all secretsmanager instances
response = client.list_instances(project_id)

# Delete all instances
for instance in response.instances:
    client.delete_instance(project_id, instance.id)
