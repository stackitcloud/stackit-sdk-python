import os

from stackit.ske.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all ske clusters
response = client.list_clusters(project_id)

# Delete all cluster
for cluster in response.items:
    client.delete_cluster(project_id, cluster.name)
