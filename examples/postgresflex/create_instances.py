import os

from stackit.postgresflex.api.default_api import DefaultApi
from stackit.postgresflex.models.create_instance_payload import CreateInstancePayload
from stackit.postgresflex.models.acl import ACL
from stackit.postgresflex.models.storage import Storage
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
storage_class = "premium-perf2-stackit"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get possible flavors
flavor_response = client.list_flavors(project_id)

# Create instance using the first flvaor
create_instance_payload = CreateInstancePayload(
    name="example-instance",
    backupSchedule="0 0 1 * *",
    acl=ACL(items=["45.129.40.0/21", "193.148.160.0/19"]),
    storage=Storage(var_class=storage_class, size=20),
    flavorId=flavor_response.flavors[0].id,
    replicas=1,
    version="16",
    options={"type": "Single"},
)
client.create_instance(project_id, create_instance_payload)
