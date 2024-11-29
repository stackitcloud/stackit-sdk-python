from stackit.core.configuration import Configuration
from stackit.ske.api.default_api import DefaultApi

project_id = "16f49d71-37ad-4137-8b97-44d9c55c4094"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all ske instances
print(client.list_clusters(project_id))
