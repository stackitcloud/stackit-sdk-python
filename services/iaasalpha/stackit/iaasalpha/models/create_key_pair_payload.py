# coding: utf-8

"""
    IaaS-API

    This API allows you to create and modify IaaS resources.

    The version of the OpenAPI document: 1alpha1
    Contact: stackit-iaas@mail.schwarz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501 docstring might be too long

from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing_extensions import Annotated, Self


class CreateKeyPairPayload(BaseModel):
    """
    Object that represents the public key of an SSH keypair and its name.
    """

    fingerprint: Optional[Annotated[str, Field(min_length=47, strict=True, max_length=47)]] = Field(
        default=None, description="Object that represents an SSH keypair MD5 fingerprint."
    )
    labels: Optional[Dict[str, Any]] = Field(
        default=None, description="Object that represents the labels of an object."
    )
    name: Optional[Annotated[str, Field(strict=True, max_length=127)]] = Field(
        default=None,
        description="The name of an SSH keypair. Allowed characters are letters [a-zA-Z], digits [0-9] and the following special characters: [@._-].",
    )
    public_key: Annotated[str, Field(strict=True)] = Field(
        description="Object that represents a public SSH key.", alias="publicKey"
    )
    __properties: ClassVar[List[str]] = ["fingerprint", "labels", "name", "publicKey"]

    @field_validator("fingerprint")
    def fingerprint_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9A-Fa-f]{2}[:-]){15}([0-9A-Fa-f]{2})$", value):
            raise ValueError(r"must validate the regular expression /^([0-9A-Fa-f]{2}[:-]){15}([0-9A-Fa-f]{2})$/")
        return value

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[A-Za-z0-9@._-]*$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9@._-]*$/")
        return value

    @field_validator("public_key")
    def public_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(ssh-rsa|ssh-ed25519)\s+[A-Za-z0-9+\/]+[=]{0,3}(\s+.+)?\s*$", value):
            raise ValueError(
                r"must validate the regular expression /^(ssh-rsa|ssh-ed25519)\s+[A-Za-z0-9+\/]+[=]{0,3}(\s+.+)?\s*$/"
            )
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateKeyPairPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "fingerprint",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateKeyPairPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "fingerprint": obj.get("fingerprint"),
                "labels": obj.get("labels"),
                "name": obj.get("name"),
                "publicKey": obj.get("publicKey"),
            }
        )
        return _obj
