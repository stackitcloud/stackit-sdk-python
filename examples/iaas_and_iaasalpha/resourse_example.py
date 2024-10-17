import os
import time

from stackit.core.configuration import Configuration
from stackit.iaas.api.default_api import DefaultApi
from stackit.iaas.models.create_area_address_family import CreateAreaAddressFamily
from stackit.iaas.models.create_area_ipv4 import CreateAreaIPv4
from stackit.iaas.models.create_network_area_payload import CreateNetworkAreaPayload
from stackit.iaas.models.create_network_area_route_payload import CreateNetworkAreaRoutePayload
from stackit.iaas.models.create_network_payload import CreateNetworkPayload
from stackit.iaas.models.network_range import NetworkRange
from stackit.iaas.models.route import Route
from stackit.iaasalpha.api.default_api import DefaultApi as AlphaDefaultApi
from stackit.iaasalpha.models.boot_volume import BootVolume
from stackit.iaasalpha.models.boot_volume_source import BootVolumeSource
from stackit.iaasalpha.models.create_nic_payload import CreateNICPayload
from stackit.iaasalpha.models.create_public_ip_payload import CreatePublicIPPayload
from stackit.iaasalpha.models.create_security_group_payload import CreateSecurityGroupPayload
from stackit.iaasalpha.models.create_server_networking_with_nics import CreateServerNetworkingWithNics
from stackit.iaasalpha.models.create_server_payload import CreateServerPayload
from stackit.iaasalpha.models.create_server_payload_networking import CreateServerPayloadNetworking
from stackit.resourcemanager.api.default_api import DefaultApi as ResourceDefaultApi
from stackit.resourcemanager.models.create_project_payload import CreateProjectPayload
from stackit.resourcemanager.models.member import Member

project_id = os.getenv("PROJECT_ID")
organization_id = os.getenv("ORGANIZATION_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)
alpha_client = AlphaDefaultApi(config)
resource_client = ResourceDefaultApi(config)

admin_vps_routes = ["147.204.0.0/16", "100.64.0.0/10", "8.8.8.8/32"]

create_network_area_payload = CreateNetworkAreaPayload(
    name="demo-network-area",
    addressFamily=CreateAreaAddressFamily(
        ipv4=CreateAreaIPv4(
            networkRanges=[
                NetworkRange(prefix="10.0.0.0/16"),
            ],
            transferNetwork="192.160.0.0/24",
            default_nameservers=["9.9.9.9"],
        )
    ),
)
demo_network_area = client.create_network_area(organization_id, create_network_area_payload)


project = resource_client.create_project(
    CreateProjectPayload(
        name="demo_network_area",
        container_parent_id=organization_id,
        labels={"networkArea": demo_network_area.area_id},
        members=[Member(role="owner", subject="example@stackit.cloud")],
    )
)
project_id = project.project_id
demo_network_area_area_id = demo_network_area.area_id

default_network_creation_response = client.create_network(
    project_id,
    CreateNetworkPayload(
        name="default",
    ),
)

security_group1 = alpha_client.create_security_group(
    project_id,
    CreateSecurityGroupPayload(
        name="My-security-group",
        description="This is created via Python SDK",
        labels={"key": "value"},
    ),
)
security_group1_groupid = security_group1.id

gateway_a_network = client.create_network(
    project_id,
    CreateNetworkPayload(
        name="gateway_a_network",
    ),
)

gateway_b_network = client.create_network(
    project_id,
    CreateNetworkPayload(
        name="gateway_b_network",
    ),
)

gateway_a_nic1 = alpha_client.create_nic(
    project_id,
    gateway_a_network.network_id,
    CreateNICPayload(
        allowed_addresses=[x for x in admin_vps_routes],
        security_groups=[security_group1_groupid],
    ),
)

gateway_a_public_ip = alpha_client.create_public_ip(
    project_id, CreatePublicIPPayload(network_interface=gateway_a_nic1.id)
)

gateway_b_nic1 = alpha_client.create_nic(
    project_id,
    gateway_b_network.network_id,
    CreateNICPayload(
        allowed_addresses=[x for x in admin_vps_routes],
        security_groups=[security_group1_groupid],
    ),
)

gateway_b_public_ip = alpha_client.create_public_ip(
    project_id, CreatePublicIPPayload(network_interface=gateway_b_nic1.id)
)

gateway_a = alpha_client.create_server(
    project_id,
    CreateServerPayload(
        name="gateway-a",
        boot_volume=BootVolume(
            size=64,
            source=BootVolumeSource(
                id="db10714b-5d17-4a88-83ea-cb499530acc8",
                type="image",
            ),
        ),
        keypair_name="key",
        labels={"key": "value"},
        machine_type="t1.2",
        availability_zone="eu01-1",
    ),
)
time.sleep(180)  # wait for server to be created
alpha_client.add_nicto_server(project_id, gateway_a.id, gateway_a_nic1.id)


admin_area_routes = client.create_network_area_route(
    organization_id,
    demo_network_area_area_id,
    CreateNetworkAreaRoutePayload(ipv4=[Route(prefix=x, nexthop=gateway_a_nic1.ipv4) for x in admin_vps_routes]),
)


# Tenant Part (right side of the picture)

tenant_network = client.create_network(
    project_id,
    CreateNetworkPayload(
        name="tenant_network",
    ),
)

tenant_nic = alpha_client.create_nic(
    project_id,
    tenant_network.network_id,
    CreateNICPayload(
        security_groups=[security_group1_groupid],
    ),
)

tenant_public_ip = alpha_client.create_public_ip(project_id, CreatePublicIPPayload(network_interface=tenant_nic.id))


tenant = alpha_client.create_server(
    project_id,
    CreateServerPayload(
        name="tenant",
        boot_volume=BootVolume(
            size=64,
            source=BootVolumeSource(
                id="db10714b-5d17-4a88-83ea-cb499530acc8",
                type="image",
            ),
        ),
        keypair_name="key",
        labels={"key": "value"},
        machine_type="t1.2",
        networking=CreateServerPayloadNetworking(CreateServerNetworkingWithNics(nic_ids=[tenant_nic.id])),
        availability_zone="eu01-1",
    ),
)
time.sleep(180)  # wait for server to be created
alpha_client.add_nicto_server(project_id, tenant.id, tenant_nic.id)
