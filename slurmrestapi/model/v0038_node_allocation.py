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


class V0038NodeAllocation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            memory = schemas.IntSchema
            cpus = schemas.IntSchema
            
            
            class sockets(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        cores = schemas.DictSchema
                        __annotations__ = {
                            "cores": cores,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cores"]) -> MetaOapg.properties.cores: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["cores", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cores"]) -> typing.Union[MetaOapg.properties.cores, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cores", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    cores: typing.Union[MetaOapg.properties.cores, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sockets':
                    return super().__new__(
                        cls,
                        *_args,
                        cores=cores,
                        _configuration=_configuration,
                        **kwargs,
                    )
            nodename = schemas.StrSchema
            __annotations__ = {
                "memory": memory,
                "cpus": cpus,
                "sockets": sockets,
                "nodename": nodename,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memory"]) -> MetaOapg.properties.memory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpus"]) -> MetaOapg.properties.cpus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sockets"]) -> MetaOapg.properties.sockets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodename"]) -> MetaOapg.properties.nodename: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["memory", "cpus", "sockets", "nodename", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memory"]) -> typing.Union[MetaOapg.properties.memory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpus"]) -> typing.Union[MetaOapg.properties.cpus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sockets"]) -> typing.Union[MetaOapg.properties.sockets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodename"]) -> typing.Union[MetaOapg.properties.nodename, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["memory", "cpus", "sockets", "nodename", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        memory: typing.Union[MetaOapg.properties.memory, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cpus: typing.Union[MetaOapg.properties.cpus, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sockets: typing.Union[MetaOapg.properties.sockets, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        nodename: typing.Union[MetaOapg.properties.nodename, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V0038NodeAllocation':
        return super().__new__(
            cls,
            *_args,
            memory=memory,
            cpus=cpus,
            sockets=sockets,
            nodename=nodename,
            _configuration=_configuration,
            **kwargs,
        )
