import os

from stackit.mongodbflex.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

tag = "tag"
project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get all MongoDBFlex instances
response = client.list_instances(project_id, tag)

for instance in response.items:
    client.delete_instance(project_id, instance.id)
