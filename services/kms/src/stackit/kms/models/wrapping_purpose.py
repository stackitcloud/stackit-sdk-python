# coding: utf-8

"""
    STACKIT Key Management Service API

    This API provides endpoints for managing keys and key rings. 

    The version of the OpenAPI document: 1beta.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
from enum import Enum

from typing_extensions import Self


class WrappingPurpose(str, Enum):
    """
    The wrapping purpose for the wrapping key.
    """

    """
    allowed enum values
    """
    WRAP_SYMMETRIC_KEY = "wrap_symmetric_key"
    WRAP_ASYMMETRIC_KEY = "wrap_asymmetric_key"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WrappingPurpose from a JSON string"""
        return cls(json.loads(json_str))
