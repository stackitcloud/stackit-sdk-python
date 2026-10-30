import os
import uuid

from stackit.core.configuration import Configuration
from stackit.registry.api.default_api import DefaultApi
from stackit.registry.models.create_artifactory_payload import (
    CreateArtifactoryPayload,
)

project_id = os.getenv("PROJECT_ID")
region = "eu01"

config = Configuration()
client = DefaultApi(config)

# Artifactory names must be unique, so a random suffix is appended
payload = CreateArtifactoryPayload(
    name="my-registry-" + uuid.uuid4().hex[:8],
)

# Create the artifactory
artifactory = client.create_artifactory(project_id, region, payload)
print("Created artifactory with ID: " + str(artifactory.id))
