import os

from stackit.kms.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
region = os.getenv("REGION")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all logme instances
for keyring in client.list_key_rings(project_id, region).key_rings:
    print(keyring.id, keyring.description)
