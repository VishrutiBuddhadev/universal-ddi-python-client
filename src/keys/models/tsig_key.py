# coding: utf-8

"""
    DDI Keys API

    The DDI Keys application is a BloxOne DDI service for managing TSIG keys and GSS-TSIG (Kerberos) keys which are used by other BloxOne DDI applications. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class TSIGKey(BaseModel):
    """
    A __TSIGKey__ object (_keys/tsig_) represents a TSIG key.
    """ # noqa: E501
    algorithm: Optional[StrictStr] = Field(
        default=None,
        description=
        "The TSIG key algorithm.  Valid values are: * _hmac_sha1_ * _hmac_sha224_ * _hmac_sha256_ * _hmac_sha384_ * _hmac_sha512_  Defaults to _hmac_sha256_."
    )
    comment: Optional[StrictStr] = Field(
        default=None,
        description=
        "The description for the TSIG key. May contain 0 to 1024 characters. Can include UTF-8."
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Time when the object has been created.")
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    name: StrictStr = Field(
        description="The TSIG key name in the absolute domain name format.")
    protocol_name: Optional[StrictStr] = Field(
        default=None,
        description=
        "The TSIG key name supplied during a create/update operation that is converted to canonical form in punycode."
    )
    secret: Optional[StrictStr] = Field(
        default=None,
        description="The TSIG key secret as a Base64 encoded string.")
    tags: Optional[Dict[str, Any]] = Field(
        default=None, description="The tags for the TSIG key in JSON format.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description=
        "Time when the object has been updated. Equals to _created_at_ if not updated after creation."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "algorithm", "comment", "created_at", "id", "name", "protocol_name",
        "secret", "tags", "updated_at"
    ]

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
        """Create an instance of TSIGKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "id",
            "protocol_name",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TSIGKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "algorithm": obj.get("algorithm"),
            "comment": obj.get("comment"),
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "protocol_name": obj.get("protocol_name"),
            "secret": obj.get("secret"),
            "tags": obj.get("tags"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
