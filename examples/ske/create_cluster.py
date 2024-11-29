import os

from stackit.core.configuration import Configuration
from stackit.ske.api.default_api import DefaultApi
from stackit.ske.models.create_or_update_cluster_payload import (
    CreateOrUpdateClusterPayload,
)
from stackit.ske.models.image import Image
from stackit.ske.models.kubernetes import Kubernetes
from stackit.ske.models.machine import Machine
from stackit.ske.models.nodepool import Nodepool
from stackit.ske.models.volume import Volume

project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Create a new cluster
cluster_name = "my-cl"
create_cluster_payload = CreateOrUpdateClusterPayload(
    kubernetes=Kubernetes(version="1.30.6"),
    nodepools=[
        Nodepool(
            availability_zones=["eu01-3"],
            machine=Machine(
                image=Image(
                    name="ubuntu",
                    version="2204.20240912.0",
                ),
                type="b1.2",
            ),
            maximum=3,
            minimum=2,
            name="my-nodepool",
            volume=Volume(
                size=20,
                type="storage_premium_perf0",
            ),
        )
    ],
)
cluster = client.create_or_update_cluster(
    project_id, cluster_name, create_cluster_payload
)
print("Created cluster with name: " + cluster.name)
