# coding: utf-8

"""
    Slurm Rest API

    API to access and control Slurm.  # noqa: E501

    The version of the OpenAPI document: 0.0.39
    Contact: sales@schedmd.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from slurmrestapi import schemas  # noqa: F401


class Dbv0039AccountInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def meta() -> typing.Type['Dbv0039Meta']:
                return Dbv0039Meta
        
            @staticmethod
            def errors() -> typing.Type['Dbv0039Errors']:
                return Dbv0039Errors
        
            @staticmethod
            def warnings() -> typing.Type['Dbv0039Warnings']:
                return Dbv0039Warnings
        
            @staticmethod
            def accounts() -> typing.Type['V0039AccountList']:
                return V0039AccountList
            __annotations__ = {
                "meta": meta,
                "errors": errors,
                "warnings": warnings,
                "accounts": accounts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Dbv0039Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'Dbv0039Errors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warnings"]) -> 'Dbv0039Warnings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounts"]) -> 'V0039AccountList': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["meta", "errors", "warnings", "accounts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Dbv0039Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union['Dbv0039Errors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warnings"]) -> typing.Union['Dbv0039Warnings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounts"]) -> typing.Union['V0039AccountList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["meta", "errors", "warnings", "accounts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        meta: typing.Union['Dbv0039Meta', schemas.Unset] = schemas.unset,
        errors: typing.Union['Dbv0039Errors', schemas.Unset] = schemas.unset,
        warnings: typing.Union['Dbv0039Warnings', schemas.Unset] = schemas.unset,
        accounts: typing.Union['V0039AccountList', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Dbv0039AccountInfo':
        return super().__new__(
            cls,
            *_args,
            meta=meta,
            errors=errors,
            warnings=warnings,
            accounts=accounts,
            _configuration=_configuration,
            **kwargs,
        )

from slurmrestapi.model.dbv0039_errors import Dbv0039Errors
from slurmrestapi.model.dbv0039_meta import Dbv0039Meta
from slurmrestapi.model.dbv0039_warnings import Dbv0039Warnings
from slurmrestapi.model.v0039_account_list import V0039AccountList
