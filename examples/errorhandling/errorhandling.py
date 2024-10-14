from stackit.dns.api.default_api import DefaultApi
from stackit.core.configuration import Configuration
from stackit.dns.exceptions import ForbiddenException

project_id = "thisisaninvalidid"

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Try to list DNS zones of a non-existing project.
# This will result in a ForbiddenExcpetion, as you don't have access to a
# non-existing project.
try:
    response = client.list_zones(project_id)
except ForbiddenException as e:
    print(e)
