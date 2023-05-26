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


class V0039Qos(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            
            
            class flags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def NOT_SET(cls):
                            return cls("NOT_SET")
                        
                        @schemas.classproperty
                        def ADD(cls):
                            return cls("ADD")
                        
                        @schemas.classproperty
                        def REMOVE(cls):
                            return cls("REMOVE")
                        
                        @schemas.classproperty
                        def PARTITION_MINIMUM_NODE(cls):
                            return cls("PARTITION_MINIMUM_NODE")
                        
                        @schemas.classproperty
                        def PARTITION_MAXIMUM_NODE(cls):
                            return cls("PARTITION_MAXIMUM_NODE")
                        
                        @schemas.classproperty
                        def PARTITION_TIME_LIMIT(cls):
                            return cls("PARTITION_TIME_LIMIT")
                        
                        @schemas.classproperty
                        def ENFORCE_USAGE_THRESHOLD(cls):
                            return cls("ENFORCE_USAGE_THRESHOLD")
                        
                        @schemas.classproperty
                        def NO_RESERVE(cls):
                            return cls("NO_RESERVE")
                        
                        @schemas.classproperty
                        def REQUIRED_RESERVATION(cls):
                            return cls("REQUIRED_RESERVATION")
                        
                        @schemas.classproperty
                        def DENY_LIMIT(cls):
                            return cls("DENY_LIMIT")
                        
                        @schemas.classproperty
                        def OVERRIDE_PARTITION_QOS(cls):
                            return cls("OVERRIDE_PARTITION_QOS")
                        
                        @schemas.classproperty
                        def NO_DECAY(cls):
                            return cls("NO_DECAY")
                        
                        @schemas.classproperty
                        def USAGE_FACTOR_SAFE(cls):
                            return cls("USAGE_FACTOR_SAFE")
            
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
            id = schemas.Int32Schema
            
            
            class limits(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class min(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class tres(
                                        schemas.DictSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            
                                            class properties:
                                                
                                                
                                                class per(
                                                    schemas.DictSchema
                                                ):
                                                
                                                
                                                    class MetaOapg:
                                                        
                                                        class properties:
                                                        
                                                            @staticmethod
                                                            def job() -> typing.Type['V0039TresList']:
                                                                return V0039TresList
                                                            __annotations__ = {
                                                                "job": job,
                                                            }
                                                    
                                                    @typing.overload
                                                    def __getitem__(self, name: typing_extensions.Literal["job"]) -> 'V0039TresList': ...
                                                    
                                                    @typing.overload
                                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                                    
                                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["job", ], str]):
                                                        # dict_instance[name] accessor
                                                        return super().__getitem__(name)
                                                    
                                                    
                                                    @typing.overload
                                                    def get_item_oapg(self, name: typing_extensions.Literal["job"]) -> typing.Union['V0039TresList', schemas.Unset]: ...
                                                    
                                                    @typing.overload
                                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                                    
                                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["job", ], str]):
                                                        return super().get_item_oapg(name)
                                                    
                                                
                                                    def __new__(
                                                        cls,
                                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                                        job: typing.Union['V0039TresList', schemas.Unset] = schemas.unset,
                                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                                    ) -> 'per':
                                                        return super().__new__(
                                                            cls,
                                                            *_args,
                                                            job=job,
                                                            _configuration=_configuration,
                                                            **kwargs,
                                                        )
                                                __annotations__ = {
                                                    "per": per,
                                                }
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["per"]) -> MetaOapg.properties.per: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                        
                                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["per", ], str]):
                                            # dict_instance[name] accessor
                                            return super().__getitem__(name)
                                        
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["per"]) -> typing.Union[MetaOapg.properties.per, schemas.Unset]: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                        
                                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["per", ], str]):
                                            return super().get_item_oapg(name)
                                        
                                    
                                        def __new__(
                                            cls,
                                            *_args: typing.Union[dict, frozendict.frozendict, ],
                                            per: typing.Union[MetaOapg.properties.per, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                        ) -> 'tres':
                                            return super().__new__(
                                                cls,
                                                *_args,
                                                per=per,
                                                _configuration=_configuration,
                                                **kwargs,
                                            )
                                    __annotations__ = {
                                        "tres": tres,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["tres"]) -> MetaOapg.properties.tres: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["tres", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["tres"]) -> typing.Union[MetaOapg.properties.tres, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tres", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                tres: typing.Union[MetaOapg.properties.tres, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'min':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    tres=tres,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "min": min,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["min", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> typing.Union[MetaOapg.properties.min, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["min", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    min: typing.Union[MetaOapg.properties.min, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'limits':
                    return super().__new__(
                        cls,
                        *_args,
                        min=min,
                        _configuration=_configuration,
                        **kwargs,
                    )
            name = schemas.StrSchema
            
            
            class preempt(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                    
                        @staticmethod
                        def exempt_time() -> typing.Type['V0039Uint32NoVal']:
                            return V0039Uint32NoVal
                        __annotations__ = {
                            "exempt_time": exempt_time,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["exempt_time"]) -> 'V0039Uint32NoVal': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["exempt_time", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["exempt_time"]) -> typing.Union['V0039Uint32NoVal', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["exempt_time", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    exempt_time: typing.Union['V0039Uint32NoVal', schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'preempt':
                    return super().__new__(
                        cls,
                        *_args,
                        exempt_time=exempt_time,
                        _configuration=_configuration,
                        **kwargs,
                    )
            priority = schemas.Int32Schema
        
            @staticmethod
            def usage_factor() -> typing.Type['V0039Float64NoVal']:
                return V0039Float64NoVal
        
            @staticmethod
            def usage_threshold() -> typing.Type['V0039Float64NoVal']:
                return V0039Float64NoVal
            __annotations__ = {
                "description": description,
                "flags": flags,
                "id": id,
                "limits": limits,
                "name": name,
                "preempt": preempt,
                "priority": priority,
                "usage_factor": usage_factor,
                "usage_threshold": usage_threshold,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flags"]) -> MetaOapg.properties.flags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limits"]) -> MetaOapg.properties.limits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preempt"]) -> MetaOapg.properties.preempt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usage_factor"]) -> 'V0039Float64NoVal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usage_threshold"]) -> 'V0039Float64NoVal': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "flags", "id", "limits", "name", "preempt", "priority", "usage_factor", "usage_threshold", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flags"]) -> typing.Union[MetaOapg.properties.flags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limits"]) -> typing.Union[MetaOapg.properties.limits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preempt"]) -> typing.Union[MetaOapg.properties.preempt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usage_factor"]) -> typing.Union['V0039Float64NoVal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usage_threshold"]) -> typing.Union['V0039Float64NoVal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "flags", "id", "limits", "name", "preempt", "priority", "usage_factor", "usage_threshold", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        flags: typing.Union[MetaOapg.properties.flags, list, tuple, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        limits: typing.Union[MetaOapg.properties.limits, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        preempt: typing.Union[MetaOapg.properties.preempt, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        usage_factor: typing.Union['V0039Float64NoVal', schemas.Unset] = schemas.unset,
        usage_threshold: typing.Union['V0039Float64NoVal', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V0039Qos':
        return super().__new__(
            cls,
            *_args,
            description=description,
            flags=flags,
            id=id,
            limits=limits,
            name=name,
            preempt=preempt,
            priority=priority,
            usage_factor=usage_factor,
            usage_threshold=usage_threshold,
            _configuration=_configuration,
            **kwargs,
        )

from slurmrestapi.model.v0039_float64_no_val import V0039Float64NoVal
from slurmrestapi.model.v0039_tres_list import V0039TresList
from slurmrestapi.model.v0039_uint32_no_val import V0039Uint32NoVal
