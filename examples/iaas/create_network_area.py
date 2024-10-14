import os

from stackit.iaas.api.default_api import DefaultApi
from stackit.iaas.models.create_network_area_payload import CreateNetworkAreaPayload
from stackit.iaas.models.create_area_address_family import CreateAreaAddressFamily
from stackit.iaas.models.create_area_ipv4 import CreateAreaIPv4
from stackit.iaas.models.network_range import NetworkRange
from stackit.core.configuration import Configuration

project_id = os.getenv("PROJECT_ID")
organization_id = os.getenv("ORGANIZATION_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)


# Create new network area
create_network_area_payload = CreateNetworkAreaPayload(
    name="example-network-area",
    addressFamily=CreateAreaAddressFamily(
        ipv4=CreateAreaIPv4(
            defaultPrefixLen=25,
            maxPrefixLen=29,
            minPrefixLen=24,
            networkRanges=[
                NetworkRange(prefix="192.168.0.0/24"),
            ],
            transferNetwork="192.160.0.0/24",
        )
    ),
)
print(client.create_network_area(organization_id, create_network_area_payload))
