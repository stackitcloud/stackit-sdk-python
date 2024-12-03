import os

from stackit.objectstorage.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
bucket_name = "BUCKET_NAME"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

client.delete_bucket(project_id, bucket_name)
