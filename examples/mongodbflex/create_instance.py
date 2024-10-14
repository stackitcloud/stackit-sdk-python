import os

from stackit.mongodbflex.api.default_api import DefaultApi
from stackit.mongodbflex.models.create_instance_payload import CreateInstancePayload
from stackit.mongodbflex.models.acl import ACL
from stackit.mongodbflex.models.storage import Storage
from stackit.core.configuration import Configuration


tag = "tag"
storage_class = "premium-perf2-mongodb"
project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get all MongoDBFlex flavors
flavors_response = client.list_flavors(project_id)

# Create an instance using the first offering
create_instance_payload = CreateInstancePayload(
    name="exampleInstance",
    backupSchedule="0 0 1 * *",
    acl=ACL(items=["45.129.40.0/21", "193.148.160.0/19"]),
    tag=tag,
    storage=Storage(var_class=storage_class, size=20),
    replicas=1,
    version="7.0",
    flavorId=flavors_response.flavors[0].id,
    options={"type": "Single"},
)
client.create_instance(project_id, create_instance_payload)
