# coding: utf-8

"""
    Slurm Rest API

    API to access and control Slurm.  # noqa: E501

    The version of the OpenAPI document: 0.0.38
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


class V0038PartitionsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def meta() -> typing.Type['V0038Meta']:
                return V0038Meta
            
            
            class errors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V0038Error']:
                        return V0038Error
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['V0038Error'], typing.List['V0038Error']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'errors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V0038Error':
                    return super().__getitem__(i)
            
            
            class partitions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V0038Partition']:
                        return V0038Partition
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['V0038Partition'], typing.List['V0038Partition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'partitions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V0038Partition':
                    return super().__getitem__(i)
            __annotations__ = {
                "meta": meta,
                "errors": errors,
                "partitions": partitions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'V0038Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partitions"]) -> MetaOapg.properties.partitions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["meta", "errors", "partitions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['V0038Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union[MetaOapg.properties.errors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partitions"]) -> typing.Union[MetaOapg.properties.partitions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["meta", "errors", "partitions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        meta: typing.Union['V0038Meta', schemas.Unset] = schemas.unset,
        errors: typing.Union[MetaOapg.properties.errors, list, tuple, schemas.Unset] = schemas.unset,
        partitions: typing.Union[MetaOapg.properties.partitions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V0038PartitionsResponse':
        return super().__new__(
            cls,
            *_args,
            meta=meta,
            errors=errors,
            partitions=partitions,
            _configuration=_configuration,
            **kwargs,
        )

from slurmrestapi.model.v0038_error import V0038Error
from slurmrestapi.model.v0038_meta import V0038Meta
from slurmrestapi.model.v0038_partition import V0038Partition
