import os

from stackit.core.configuration import Configuration
from stackit.registry.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
region = "eu01"
artifactory_id = "ARTIFACTORY_ID"

config = Configuration()
client = DefaultApi(config)

# Delete an artifactory
client.delete_artifactory(project_id=project_id, region_id=region, artifactory_id=artifactory_id)
