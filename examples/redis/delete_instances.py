import os

from stackit.redis.api.default_api import DefaultApi
from stackit.core.configuration import Configuration


project_id = os.getenv("PROJECT_ID")

config = Configuration()
client = DefaultApi(config)

# get all instances
response = client.list_instances(project_id)

# delete all instances
for instance in response.instances:
    client.delete_instance(project_id=project_id, instance_id=instance.cf_guid)
