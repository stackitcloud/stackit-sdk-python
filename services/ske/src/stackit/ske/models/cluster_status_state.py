# coding: utf-8

"""
    SKE-API

    The SKE API provides endpoints to create, update, delete clusters within STACKIT portal projects and to trigger further cluster management tasks.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
from enum import Enum

from typing_extensions import Self


class ClusterStatusState(str, Enum):
    """
    ClusterStatusState
    """

    """
    allowed enum values
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    STATE_HEALTHY = "STATE_HEALTHY"
    STATE_CREATING = "STATE_CREATING"
    STATE_DELETING = "STATE_DELETING"
    STATE_UNHEALTHY = "STATE_UNHEALTHY"
    STATE_RECONCILING = "STATE_RECONCILING"
    STATE_HIBERNATED = "STATE_HIBERNATED"
    STATE_HIBERNATING = "STATE_HIBERNATING"
    STATE_WAKINGUP = "STATE_WAKINGUP"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterStatusState from a JSON string"""
        return cls(json.loads(json_str))
