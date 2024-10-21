import os
import time

from stackit.core.configuration import Configuration
from stackit.iaas.api.default_api import DefaultApi
from stackit.iaas.models.create_area_address_family import CreateAreaAddressFamily
from stackit.iaas.models.create_area_ipv4 import CreateAreaIPv4
from stackit.iaas.models.create_network_area_payload import CreateNetworkAreaPayload
from stackit.iaas.models.create_network_payload import CreateNetworkPayload
from stackit.iaas.models.network_range import NetworkRange
from stackit.iaas.models.boot_volume import BootVolume
from stackit.iaas.models.boot_volume_source import BootVolumeSource
from stackit.iaas.models.create_nic_payload import CreateNICPayload
from stackit.iaas.models.create_public_ip_payload import CreatePublicIPPayload
from stackit.iaas.models.create_security_group_payload import CreateSecurityGroupPayload
from stackit.iaas.models.create_server_payload import CreateServerPayload
from stackit.resourcemanager.api.default_api import DefaultApi as ResourceDefaultApi
from stackit.resourcemanager.models.create_project_payload import CreateProjectPayload
from stackit.resourcemanager.models.member import Member

project_id = os.getenv("PROJECT_ID")
organization_id = os.getenv("ORGANIZATION_ID")
image_id = os.getenv("IMAGE_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)
resource_client = ResourceDefaultApi(config)

create_network_area_payload = CreateNetworkAreaPayload(
    name="network-area",
    addressFamily=CreateAreaAddressFamily(
        ipv4=CreateAreaIPv4(
            networkRanges=[
                NetworkRange(prefix="192.0.2.0/24"),
            ],
            transferNetwork="192.0.2.0/24",
            default_nameservers=["192.0.2.0"],
        )
    ),
)
network_area = client.create_network_area(organization_id, create_network_area_payload)


project = resource_client.create_project(
    CreateProjectPayload(
        name="network_area",
        container_parent_id=organization_id,
        labels={"networkArea": network_area.area_id},
        members=[Member(role="owner", subject="example@stackit.cloud")],
    )
)
project_id = project.project_id
network_area_area_id = network_area.area_id

default_network_creation_response = client.create_network(
    project_id,
    CreateNetworkPayload(
        name="default",
    ),
)

security_group1 = client.create_security_group(
    project_id,
    CreateSecurityGroupPayload(
        name="My-security-group",
        description="This is created via Python SDK",
        labels={"key": "value"},
    ),
)
security_group1_groupid = security_group1.id

network = client.create_network(
    project_id,
    CreateNetworkPayload(
        name="network",
    ),
)

nic1 = client.create_nic(
    project_id,
    network.network_id,
    CreateNICPayload(
        allowed_addresses=["192.0.2.0/24"],
        security_groups=[security_group1_groupid],
    ),
)

public_ip = client.create_public_ip(project_id, CreatePublicIPPayload(network_interface=nic1.id))

server = client.create_server(
    project_id,
    CreateServerPayload(
        name="example-server",
        boot_volume=BootVolume(
            size=64,
            source=BootVolumeSource(
                id=image_id,
                type="image",
            ),
        ),
        keypair_name="key",
        labels={"key": "value"},
        machine_type="t1.2",
        availability_zone="eu01-1",
    ),
)
time.sleep(180)  # wait for server to be created, temporary sleep until waiter methods are implemented
client.add_nicto_server(project_id, server.id, nic1.id)
