import os

from stackit.serviceaccount.api.default_api import DefaultApi
from stackit.serviceaccount.models.create_service_account_payload import (
    CreateServiceAccountPayload,
)

from stackit.core.configuration import Configuration


project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Create a new serviceaccount
create_serviceaccount_payload = CreateServiceAccountPayload(
    name="my-service-account",
)
client.create_service_account(project_id, create_serviceaccount_payload)
