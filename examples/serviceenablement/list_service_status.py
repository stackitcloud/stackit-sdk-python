import os

from stackit.serviceenablement.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List service status
response = client.list_service_status(project_id)
print(response)

# Get status of one service
service_id = response.items[0].service_id
print(client.get_service_status(project_id, service_id))
