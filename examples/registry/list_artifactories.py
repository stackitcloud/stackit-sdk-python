import os

from stackit.core.configuration import Configuration
from stackit.registry.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
region = "eu01"

config = Configuration()
client = DefaultApi(config)

# Get all artifactories, following pagination tokens.
next_page_token = None

while True:
    response = client.list_artifactories(
        project_id=project_id,
        region_id=region,
        next_page_token=next_page_token,
    )

    for artifactory in response.artifactories:
        print(artifactory)

    next_page_token = response.next_page_token
    if not next_page_token:
        break
