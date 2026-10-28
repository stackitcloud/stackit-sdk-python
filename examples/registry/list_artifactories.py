import os

from stackit.core.configuration import Configuration
from stackit.registry.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
region = "eu01"

config = Configuration()
client = DefaultApi(config)

# Get all artifactories
print(client.list_artifactories(project_id, region))
