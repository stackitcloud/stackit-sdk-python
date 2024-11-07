from enum import Enum
from typing import Any, Tuple, Union

from stackit.core.wait import Wait, WaitConfig

from stackit.iaas.api.default_api import DefaultApi
from stackit.iaas.models.network_area import NetworkArea
from stackit.iaas.models.network import Network
from stackit.iaas.models.volume import Volume
from stackit.iaas.exceptions import ApiException, NotFoundException


class _States(str, Enum):
    CreateSuccess = "CREATED"
    VolumeAvailableStatus = "AVAILABLE"
    DeleteSuccess = "DELETED"
    ErrorStatus = "ERROR"
    ServerActiveStatus = "ACTIVE"
    ServerResizingStatus = "RESIZING"

    RequestCreateAction = "CREATE"
    RequestUpdateAction = "UPDATE"
    RequestDeleteAction = "DELETE"
    RequestCreatedStatus = "CREATED"
    RequestUpdatedStatus = "UPDATED"
    RequestDeletedStatus = "DELETED"
    RequestFailedStatus = "FAILED"



def wait_for_create_network_area(
    api_client: DefaultApi,
    organization_id: str,
    area_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> NetworkArea:

    def get_network_area_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, organization_id, area_id

        try:
            response = api_client.get_network_area(organization_id, area_id)
            if response.zone.id != area_id:
                return False, ValueError("ID of area in return not equal to ID of requested area."), None, None
            elif response.zone.state == _States.CreateSuccess:
                return True, None, None, response            
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_network_area_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_update_network_area(
    api_client: DefaultApi,
    organization_id: str,
    area_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> NetworkArea:

    def get_network_area_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, organization_id, area_id

        try:
            response = api_client.get_network_area(organization_id, area_id)
            if response.zone.id != area_id:
                return False, ValueError("ID of area in return not equal to ID of requested area."), None, None
            elif response.zone.state == _States.CreateSuccess:
                return True, None, None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_network_area_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_delete_network_area(
    api_client: DefaultApi,
    organization_id: str,
    area_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> None:

    def get_network_area_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, organization_id, area_id

        try:
            _ = api_client.get_network_area(organization_id, area_id)            
            return False, None, None, None
        except NotFoundException:
            return True, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_network_area_execute_state,
        config=wait_config,
    )
    return wait.wait()

##########################################################


def wait_for_create_network(
    api_client: DefaultApi,
    project_id: str,
    network_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> Network:

    def get_network_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, network_id

        try:
            response = api_client.get_network(project_id, network_id)
            if response.zone.id != network_id:
                return False, ValueError("ID of network in return not equal to ID of requested network."), None, None
            elif response.zone.state == _States.CreateSuccess:
                return True, None, None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_network_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_update_network(
    api_client: DefaultApi,
    project_id: str,
    network_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> Network:

    def get_network_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, network_id

        try:
            response = api_client.get_network(project_id, network_id)
            if response.zone.id != network_id:
                return False, ValueError("ID of network in return not equal to ID of requested network."), None, None
            elif response.zone.state == _States.CreateSuccess:
                return True, None, None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_network_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_delete_network(
    api_client: DefaultApi,
    project_id: str,
    area_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> None:

    def get_network_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, area_id

        try:
            _ = api_client.get_network(project_id, area_id)
            return False, None, None, None
        except NotFoundException:
            return True, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_network_execute_state,
        config=wait_config,
    )
    return wait.wait()

##########################################################


def wait_for_create_volume(
    api_client: DefaultApi,
    project_id: str,
    volume_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> Volume:

    def get_volume_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, volume_id

        try:
            response = api_client.get_volume(project_id, volume_id)
            if response.zone.id != volume_id:
                return False, ValueError("ID of volume in return not equal to ID of requested volume."), None, None
            elif response.zone.state == _States.ErrorStatus:
                return False, ValueError("Create failed for volume with id %s" % volume_id), None, None
            elif response.zone.state == _States.VolumeAvailableStatus:
                return True, None, None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_volume_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_update_volume(
    api_client: DefaultApi,
    project_id: str,
    volume_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> Volume:

    def get_volume_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, volume_id

        try:
            response = api_client.get_volume(project_id, volume_id)
            if response.zone.id != volume_id:
                return False, ValueError("ID of volume_id in return not equal to ID of requested volume_id."), None, None
            elif response.zone.state == _States.ErrorStatus:
                return False, ValueError("Create failed for volume with id %s" % volume_id), None, None
            elif response.zone.state == _States.VolumeAvailableStatus:
                return True, None, None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_volume_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_delete_volume(
    api_client: DefaultApi,
    project_id: str,
    volume_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> Union[None,Volume]:

    def get_volume_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, volume_id

        try:
            response = api_client.get_volume(project_id, volume_id)
            if response.volume and response.volume.id == volume_id and response.volume.statusw == _States.DeleteSuccess:
                return True, None, None, response
            return False, None, None, None
        except NotFoundException:
            return True, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_volume_execute_state,
        config=wait_config,
    )
    return wait.wait()

##########################################################
