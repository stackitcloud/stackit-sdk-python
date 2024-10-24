# coding: utf-8

# flake8: noqa
"""
    Resource Manager API

    API v2 to manage resource containers - organizations, folders, projects incl. labels  ### Resource Management STACKIT resource management handles the terms _Organization_, _Folder_, _Project_, _Label_, and the hierarchical structure between them. Technically, organizations,  folders, and projects are _Resource Containers_ to which a _Label_ can be attached to. The STACKIT _Resource Manager_ provides CRUD endpoints to query and to modify the state.  ### Organizations STACKIT organizations are the base element to create and to use cloud-resources. An organization is bound to one customer account. Organizations have a lifecycle. - Organizations are always the root node in resource hierarchy and do not have a parent  ### Projects STACKIT projects are needed to use cloud-resources. Projects serve as wrapper for underlying technical structures and processes. Projects have a lifecycle. Projects compared to folders may have different policies. - Projects are optional, but mandatory for cloud-resource usage - A project can be created having either an organization, or a folder as parent - A project must not have a project as parent - Project names under the same parent must not be unique - Root organization cannot be changed  ### Label STACKIT labels are key-value pairs including a resource container reference. Labels can be defined and attached freely to resource containers by which resources can be organized and queried. - Policy-based, immutable labels may exists

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long


# import models into model package
from stackit.resourcemanager.models.create_project_payload import CreateProjectPayload
from stackit.resourcemanager.models.error_response import ErrorResponse
from stackit.resourcemanager.models.folder_response import FolderResponse
from stackit.resourcemanager.models.get_project_response import GetProjectResponse
from stackit.resourcemanager.models.lifecycle_state import LifecycleState
from stackit.resourcemanager.models.list_organization_containers_response import (
    ListOrganizationContainersResponse,
)
from stackit.resourcemanager.models.list_organizations_response import (
    ListOrganizationsResponse,
)
from stackit.resourcemanager.models.list_organizations_response_items_inner import (
    ListOrganizationsResponseItemsInner,
)
from stackit.resourcemanager.models.list_projects_response import ListProjectsResponse
from stackit.resourcemanager.models.member import Member
from stackit.resourcemanager.models.organization_response import OrganizationResponse
from stackit.resourcemanager.models.parent import Parent
from stackit.resourcemanager.models.parent_list_inner import ParentListInner
from stackit.resourcemanager.models.partial_update_project_payload import (
    PartialUpdateProjectPayload,
)
from stackit.resourcemanager.models.project import Project
