import os

from stackit.core.configuration import Configuration
from stackit.valkey.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")

config = Configuration()
client = DefaultApi(config)

# Get all instances
print(client.list_instances(project_id))
