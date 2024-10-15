import os

from stackit.ske.api.default_api import DefaultApi
from stackit.ske.models.create_or_update_cluster_payload import (
    CreateOrUpdateClusterPayload,
)
from stackit.ske.models.kubernetes import Kubernetes
from stackit.ske.models.nodepool import Nodepool
from stackit.ske.models.machine import Machine
from stackit.ske.models.volume import Volume
from stackit.ske.models.image import Image

from stackit.core.configuration import Configuration


project_id = os.getenv("PROJECT_ID")
volume_type = "storage_premium_perf0"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get available options
options_resonse = client.list_provider_options()

# Create a new instance using the first option for everything
cluser_name = "cl-name"
create_instance_payload = CreateOrUpdateClusterPayload(
    kubernetes=Kubernetes(version=options_resonse.kubernetes_versions[0].version),
    nodepools=[
        Nodepool(
            availability_zones=[options_resonse.availability_zones[0].name],
            machine=Machine(
                image=Image(
                    name=options_resonse.machine_images[0].name,
                    version=options_resonse.machine_images[0].versions[0].version,
                ),
                type=options_resonse.machine_types[0].name,
            ),
            maximum=3,
            minimum=2,
            name="my-nodepool",
            volume=Volume(
                size=20,
                type=volume_type,
            ),
        )
    ],
)
client.create_or_update_cluster(project_id, cluser_name, create_instance_payload)
