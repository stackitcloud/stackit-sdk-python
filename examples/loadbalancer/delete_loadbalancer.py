import os

from stackit.core.configuration import Configuration
from stackit.loadbalancer.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
instance_name = "INSTANCE_NAME"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Delete an instance
client.delete_load_balancer(project_id, instance_name)
