import os

from stackit.serviceaccount.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
account_mail = "SERVICE_ACCOUNT_MAIL"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)


# Delete service account
client.delete_service_account(project_id, account_mail)
