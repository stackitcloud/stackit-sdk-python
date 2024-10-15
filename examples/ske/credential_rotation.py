import os

from stackit.ske.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get all ske instances
response = client.list_clusters(project_id)

# Rotate credentials on all instances
for cluster in response.items:
    client.start_credentials_rotation(project_id, cluster.name)
