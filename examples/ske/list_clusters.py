import os

from stackit.core.configuration import Configuration
from stackit.ske.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all ske instances
print(client.list_clusters(project_id))
