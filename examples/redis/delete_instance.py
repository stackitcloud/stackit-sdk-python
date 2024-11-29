import os

from stackit.core.configuration import Configuration
from stackit.redis.api.default_api import DefaultApi

project_id = os.getenv("PROJECT_ID")
instance_id = "INSTANCE_ID"

config = Configuration()
client = DefaultApi(config)

# Delete an instance
client.delete_instance(project_id=project_id, instance_id=instance_id)
