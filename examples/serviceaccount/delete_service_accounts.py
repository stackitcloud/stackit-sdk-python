import os

from stackit.serviceaccount.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# List all serviceaccounts
response = client.list_service_accounts(project_id)

# Delete all accounts
for account in response.items:
    client.delete_service_account(project_id, account.email)
