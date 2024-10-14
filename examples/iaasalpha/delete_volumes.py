import os

from stackit.iaasalpha.api.default_api import DefaultApi
from stackit.core.configuration import Configuration


project_id = os.getenv("PROJECT_ID")

config = Configuration()
client = DefaultApi(config)

# get all volumes
response = client.list_volumes(project_id)

# delete all volumes
for item in response.items:
    client.delete_volume(project_id=project_id, volume_id=item.id)
