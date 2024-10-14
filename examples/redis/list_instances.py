import os

from stackit.redis.api.default_api import DefaultApi
from stackit.core.configuration import Configuration


project_id = os.getenv("PROJECT_ID")

config = Configuration()
client = DefaultApi(config)

# get all instances
print(client.list_instances(project_id))
