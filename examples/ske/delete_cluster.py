import os

from stackit.core.configuration import Configuration
from stackit.ske.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
cluster_name = "CLUSTER_NAME"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Delete a cluster
client.delete_cluster(project_id, cluster_name)
