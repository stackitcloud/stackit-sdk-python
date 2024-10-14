import os

from stackit.mongodbflex.api.default_api import DefaultApi
from stackit.mongodbflex.models.create_user_payload import CreateUserPayload
from stackit.core.configuration import Configuration


tag = "tag"
storage_class = "premium-perf2-mongodb"
project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Get all MongoDBFlex instances
response = client.list_instances(project_id, tag)

# Create user on the first found instance
create_user_payload = CreateUserPayload(
    username="example-user",
    database="default",
    roles=["read"],
)
print(client.create_user(project_id, response.items[0].id, create_user_payload))
