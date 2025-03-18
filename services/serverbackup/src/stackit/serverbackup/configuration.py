# coding: utf-8

"""
    STACKIT Server Backup Management API

    API endpoints for Server Backup Operations on STACKIT Servers.

    The version of the OpenAPI document: 2.0
    Contact: support@stackit.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

import os


class HostConfiguration:
    def __init__(
        self,
        region=None,
        server_index=None,
        server_variables=None,
        server_operation_index=None,
        server_operation_variables=None,
        ignore_operation_servers=False,
    ) -> None:
        print(
            "WARNING: STACKIT will move to a new way of specifying regions, where the region is provided\n",
            "as a function argument instead of being set in the client configuration.\n"
            "Once all services have migrated, the methods to specify the region in the client configuration "
            "will be removed.",
        )
        """Constructor
        """
        self._base_path = "https://server-backup.api.stackit.cloud"
        """Default Base url
        """
        self.server_index = 0 if server_index is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        if region:
            self.server_variables["region"] = "{}.".format(region)
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.ignore_operation_servers = ignore_operation_servers
        """Ignore operation servers
        """

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                "url": "https://server-backup.api.stackit.cloud",
                "description": "No description provided",
                "variables": {
                    "region": {
                        "description": "No description provided",
                        "default_value": "global",
                    }
                },
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :error: if a region is given for a global url
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers))
            )

        url = server["url"]

        # check if environment variable was provided for region
        # if nothing was set this is None
        region_env = os.environ.get("STACKIT_REGION")

        # go through variables and replace placeholders
        for variable_name, variable in server.get("variables", {}).items():
            # If a region is provided by the user for a global url
            # return an error (except for providing via environment variable).
            # The region is provided as a function argument instead of being set in the client configuration.
            if (
                variable_name == "region"
                and (variable["default_value"] == "global" or variable["default_value"] == "")
                and region_env is None
                and variables.get(variable_name) is not None
            ):
                raise ValueError(
                    "this API does not support setting a region in the the client configuration, "
                    "please check if the region can be specified as a function parameter"
                )
            used_value = variables.get(variable_name, variable["default_value"])

            if "enum_values" in variable and used_value not in variable["enum_values"]:
                given_value = variables[variable_name].replace(".", "")
                valid_values = [v.replace(".", "") for v in variable["enum_values"]]
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value '{1}'. Must be '{2}'.".format(
                        variable_name, given_value, valid_values
                    )
                )

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self):
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value):
        """Fix base path."""
        self._base_path = value
        self.server_index = None
