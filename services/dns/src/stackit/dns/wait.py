from enum import Enum
from typing import Any, Tuple, Union

from stackit.core.wait import Wait, WaitConfig

from stackit.dns.api.default_api import DefaultApi
from stackit.dns.exceptions import ApiException
from stackit.dns.models.record_set_response import RecordSetResponse
from stackit.dns.models.zone_response import ZoneResponse


class _States(str, Enum):
    CreateSuccess = "CREATE_SUCCEEDED"
    CreateFail = "CREATE_FAILED"
    UpdateSuccess = "UPDATE_SUCCEEDED"
    UpdateFail = "UPDATE_FAILED"
    DeleteSuccess = "DELETE_SUCCEEDED"
    DeleteFail = "DELETE_FAILED"


def wait_for_create_zone(
    api_client: DefaultApi,
    project_id: str,
    zone_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> ZoneResponse:

    def get_zone_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, zone_id

        try:
            response = api_client.get_zone(project_id, zone_id)
            if response.zone.id != zone_id:
                return False, ValueError("ID of zone in return not equal to ID of requested zone."), None, None
            elif response.zone.state == _States.CreateSuccess:
                return True, None, None, response
            elif response.zone.state == _States.CreateFail:
                return True, Exception("Create failed for zone with ID %s" % zone_id), None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_zone_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_partial_update_zone(
    api_client: DefaultApi,
    project_id: str,
    zone_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> ZoneResponse:

    def get_zone_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, zone_id

        try:
            response = api_client.get_zone(project_id, zone_id)
            if response.zone.id != zone_id:
                return False, ValueError("ID of zone in return not equal to ID of requested zone."), None, None
            elif response.zone.state == _States.UpdateSuccess:
                return True, None, None, response
            elif response.zone.state == _States.UpdateFail:
                return True, Exception("Update failed for zone with ID %s" % zone_id), None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_zone_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_delete_zone(
    api_client: DefaultApi,
    project_id: str,
    zone_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> ZoneResponse:

    def get_zone_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, zone_id

        try:
            response = api_client.get_zone(project_id, zone_id)
            if response.zone.id != zone_id:
                return False, ValueError("ID of zone in return not equal to ID of requested zone."), None, None
            elif response.zone.state == _States.DeleteSuccess:
                return True, None, None, response
            elif response.zone.state == _States.DeleteFail:
                return True, Exception("Delete failed for zone with ID %s" % zone_id), None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_zone_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_create_recordset(
    api_client: DefaultApi,
    project_id: str,
    zone_id: str,
    rr_set_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> RecordSetResponse:

    def get_rr_set_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, zone_id, rr_set_id

        try:
            response = api_client.get_record_set(project_id, zone_id, rr_set_id)
            if response.rrset.id != rr_set_id:
                return False, ValueError("ID of rrset in return not equal to ID of requested rrset."), None, None
            elif response.rrset.state == _States.CreateSuccess:
                return True, None, None, response
            elif response.rrset.state == _States.CreateFail:
                return True, Exception("Create failed for rrset with ID %s" % rr_set_id), None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_rr_set_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_partial_update_recordset(
    api_client: DefaultApi,
    project_id: str,
    zone_id: str,
    rr_set_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> RecordSetResponse:

    def get_rr_set_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, zone_id, rr_set_id

        try:
            response = api_client.get_record_set(project_id, zone_id, rr_set_id)
            if response.rrset.id != rr_set_id:
                return False, ValueError("ID of rrset in return not equal to ID of requested rrset."), None, None
            elif response.rrset.state == _States.UpdateSuccess:
                return True, None, None, response
            elif response.rrset.state == _States.UpdateFail:
                return True, Exception("Update failed for rrset with ID %s" % rr_set_id), None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_rr_set_execute_state,
        config=wait_config,
    )
    return wait.wait()


def wait_for_delete_recordset(
    api_client: DefaultApi,
    project_id: str,
    zone_id: str,
    rr_set_id: str,
    wait_config: Union[WaitConfig, None] = None,
) -> RecordSetResponse:

    def get_rr_set_execute_state() -> Tuple[bool, Union[Exception, None], Union[int, None], Any]:

        nonlocal api_client, project_id, zone_id, rr_set_id

        try:
            response = api_client.get_record_set(project_id, zone_id, rr_set_id)
            if response.rrset.id != rr_set_id:
                return False, ValueError("ID of rrset in return not equal to ID of requested rrset."), None, None
            elif response.rrset.state == _States.DeleteSuccess:
                return True, None, None, response
            elif response.rrset.state == _States.DeleteFail:
                return True, Exception("Delete failed for rrset with ID %s" % rr_set_id), None, response
            else:
                return False, None, None, None
        except ApiException as e:
            return False, e, e.status, None
        except Exception as e:
            return False, e, None, None

    wait = Wait(
        get_rr_set_execute_state,
        config=wait_config,
    )
    return wait.wait()
