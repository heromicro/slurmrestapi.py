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


class V0039LicensesInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def meta() -> typing.Type['V0039Meta']:
                return V0039Meta
        
            @staticmethod
            def errors() -> typing.Type['V0039Errors']:
                return V0039Errors
        
            @staticmethod
            def warnings() -> typing.Type['V0039Warnings']:
                return V0039Warnings
        
            @staticmethod
            def licenses() -> typing.Type['V0039Licenses']:
                return V0039Licenses
            __annotations__ = {
                "meta": meta,
                "errors": errors,
                "warnings": warnings,
                "licenses": licenses,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'V0039Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'V0039Errors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warnings"]) -> 'V0039Warnings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licenses"]) -> 'V0039Licenses': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["meta", "errors", "warnings", "licenses", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['V0039Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union['V0039Errors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warnings"]) -> typing.Union['V0039Warnings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licenses"]) -> typing.Union['V0039Licenses', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["meta", "errors", "warnings", "licenses", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        meta: typing.Union['V0039Meta', schemas.Unset] = schemas.unset,
        errors: typing.Union['V0039Errors', schemas.Unset] = schemas.unset,
        warnings: typing.Union['V0039Warnings', schemas.Unset] = schemas.unset,
        licenses: typing.Union['V0039Licenses', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V0039LicensesInfo':
        return super().__new__(
            cls,
            *_args,
            meta=meta,
            errors=errors,
            warnings=warnings,
            licenses=licenses,
            _configuration=_configuration,
            **kwargs,
        )

from slurmrestapi.model.v0039_errors import V0039Errors
from slurmrestapi.model.v0039_licenses import V0039Licenses
from slurmrestapi.model.v0039_meta import V0039Meta
from slurmrestapi.model.v0039_warnings import V0039Warnings
