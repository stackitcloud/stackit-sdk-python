import os

from stackit.iaasalpha.api.default_api import DefaultApi
from stackit.core.configuration import Configuration


project_id = os.getenv("PROJECT_ID")
volume_id = "VOLUME_ID"

config = Configuration()
client = DefaultApi(config)

client.delete_volume(project_id=project_id, volume_id=volume_id)
