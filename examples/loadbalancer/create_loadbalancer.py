import os

from stackit.loadbalancer.api.default_api import DefaultApi
from stackit.loadbalancer.models.create_load_balancer_payload import (
    CreateLoadBalancerPayload,
)
from stackit.loadbalancer.models.load_balancer_options import LoadBalancerOptions
from stackit.loadbalancer.models.listener import Listener
from stackit.loadbalancer.models.target_pool import TargetPool
from stackit.loadbalancer.models.network import Network
from stackit.loadbalancer.models.target import Target
from stackit.core.configuration import Configuration

# Note: Create a target server before
NETWORK_ID = "NETWORK_ID"
IP_ADDRESS = "x.x.x.x"
X_REQUEST_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
project_id = os.getenv("PROJECT_ID")

# Create a new API client, that uses default authentication and configuration
config = Configuration()
client = DefaultApi(config)


# Create new LoadBalancer
create_load_balancer_payload = CreateLoadBalancerPayload(
    name="example-instance",
    options=LoadBalancerOptions(
        privateNetworkOnly=True,
    ),
    networks=[
        Network(
            networkId=NETWORK_ID,
            role="ROLE_LISTENERS_AND_TARGETS",
        ),
    ],
    listeners=[
        Listener(
            displayName="example-listener",
            port=1,
            protocol="PROTOCOL_TCP",
            targetPool="example-target-pool",
        ),
    ],
    targetPools=[
        TargetPool(
            name="example-target-pool",
            targetPort=1,
            targets=[Target(displayName="example-target", ip=IP_ADDRESS)],
        )
    ],
)
response = client.create_load_balancer(project_id, X_REQUEST_ID, create_load_balancer_payload)
