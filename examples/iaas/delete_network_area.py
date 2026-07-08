import os
import time

from stackit.iaas.api.default_api import DefaultApi
from stackit.core.configuration import Configuration

organization_id = os.getenv("ORGANIZATION_ID")
network_area_id = os.getenv("NETWORK_AREA_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)

# Delete all configured network area regions first
list_regions_resp = client.list_network_area_regions(organization_id, network_area_id)
for region_id in list_regions_resp.regions:
    client.delete_network_area_region(organization_id, network_area_id, region_id)

# wait for all network area regions to be deleted
while True:
    list_regions_resp = client.list_network_area_regions(organization_id, network_area_id)
    if len(list_regions_resp.regions) < 1:
        break
    time.sleep(3)

# Delete the network area
client.delete_network_area(organization_id, network_area_id)
