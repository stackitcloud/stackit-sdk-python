import os

from stackit.objectstorage.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
bucket_name = "example-bucket43432432"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Create new ObjectStorage bucket instances
client.create_bucket(project_id, bucket_name)
