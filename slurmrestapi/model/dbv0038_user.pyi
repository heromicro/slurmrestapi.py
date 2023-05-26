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


class Dbv0038User(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    User description
    """


    class MetaOapg:
        
        class properties:
            administrator_level = schemas.StrSchema
            
            
            class associations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Dbv0038AssociationShortInfo']:
                        return Dbv0038AssociationShortInfo
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Dbv0038AssociationShortInfo'], typing.List['Dbv0038AssociationShortInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'associations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Dbv0038AssociationShortInfo':
                    return super().__getitem__(i)
            
            
            class coordinators(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Dbv0038CoordinatorInfo']:
                        return Dbv0038CoordinatorInfo
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Dbv0038CoordinatorInfo'], typing.List['Dbv0038CoordinatorInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'coordinators':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Dbv0038CoordinatorInfo':
                    return super().__getitem__(i)
            
            
            class default(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        account = schemas.StrSchema
                        wckey = schemas.StrSchema
                        __annotations__ = {
                            "account": account,
                            "wckey": wckey,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["account"]) -> MetaOapg.properties.account: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["wckey"]) -> MetaOapg.properties.wckey: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["account", "wckey", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["account"]) -> typing.Union[MetaOapg.properties.account, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["wckey"]) -> typing.Union[MetaOapg.properties.wckey, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account", "wckey", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    account: typing.Union[MetaOapg.properties.account, str, schemas.Unset] = schemas.unset,
                    wckey: typing.Union[MetaOapg.properties.wckey, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'default':
                    return super().__new__(
                        cls,
                        *_args,
                        account=account,
                        wckey=wckey,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class flags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'flags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            name = schemas.StrSchema
            __annotations__ = {
                "administrator_level": administrator_level,
                "associations": associations,
                "coordinators": coordinators,
                "default": default,
                "flags": flags,
                "name": name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["administrator_level"]) -> MetaOapg.properties.administrator_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associations"]) -> MetaOapg.properties.associations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coordinators"]) -> MetaOapg.properties.coordinators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default"]) -> MetaOapg.properties.default: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flags"]) -> MetaOapg.properties.flags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["administrator_level", "associations", "coordinators", "default", "flags", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["administrator_level"]) -> typing.Union[MetaOapg.properties.administrator_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associations"]) -> typing.Union[MetaOapg.properties.associations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coordinators"]) -> typing.Union[MetaOapg.properties.coordinators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default"]) -> typing.Union[MetaOapg.properties.default, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flags"]) -> typing.Union[MetaOapg.properties.flags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["administrator_level", "associations", "coordinators", "default", "flags", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        administrator_level: typing.Union[MetaOapg.properties.administrator_level, str, schemas.Unset] = schemas.unset,
        associations: typing.Union[MetaOapg.properties.associations, list, tuple, schemas.Unset] = schemas.unset,
        coordinators: typing.Union[MetaOapg.properties.coordinators, list, tuple, schemas.Unset] = schemas.unset,
        default: typing.Union[MetaOapg.properties.default, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        flags: typing.Union[MetaOapg.properties.flags, list, tuple, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Dbv0038User':
        return super().__new__(
            cls,
            *_args,
            administrator_level=administrator_level,
            associations=associations,
            coordinators=coordinators,
            default=default,
            flags=flags,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from slurmrestapi.model.dbv0038_association_short_info import Dbv0038AssociationShortInfo
from slurmrestapi.model.dbv0038_coordinator_info import Dbv0038CoordinatorInfo
