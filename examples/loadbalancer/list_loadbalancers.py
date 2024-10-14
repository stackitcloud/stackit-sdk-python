import os

from stackit.loadbalancer.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all LoadBalancers
print(client.list_load_balancers(project_id))
