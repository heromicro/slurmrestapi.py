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


class V0039Step(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class time(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class user(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    microseconds = schemas.Int32Schema
                                    __annotations__ = {
                                        "microseconds": microseconds,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["microseconds"]) -> MetaOapg.properties.microseconds: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["microseconds", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["microseconds"]) -> typing.Union[MetaOapg.properties.microseconds, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["microseconds", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                microseconds: typing.Union[MetaOapg.properties.microseconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'user':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    microseconds=microseconds,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "user": user,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["user", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    user: typing.Union[MetaOapg.properties.user, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'time':
                    return super().__new__(
                        cls,
                        *_args,
                        user=user,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def exit_code() -> typing.Type['V0039JobExitCode']:
                return V0039JobExitCode
            
            
            class nodes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                    
                        @staticmethod
                        def _list() -> typing.Type['V0039Hostlist']:
                            return V0039Hostlist
                        __annotations__ = {
                            "list": _list,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["list"]) -> 'V0039Hostlist': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["list", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["list"]) -> typing.Union['V0039Hostlist', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["list", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'nodes':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class tasks(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        count = schemas.Int32Schema
                        __annotations__ = {
                            "count": count,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["count", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["count", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'tasks':
                    return super().__new__(
                        cls,
                        *_args,
                        count=count,
                        _configuration=_configuration,
                        **kwargs,
                    )
            pid = schemas.StrSchema
            
            
            class CPU(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        governor = schemas.StrSchema
                        __annotations__ = {
                            "governor": governor,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["governor"]) -> MetaOapg.properties.governor: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["governor", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["governor"]) -> typing.Union[MetaOapg.properties.governor, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["governor", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    governor: typing.Union[MetaOapg.properties.governor, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'CPU':
                    return super().__new__(
                        cls,
                        *_args,
                        governor=governor,
                        _configuration=_configuration,
                        **kwargs,
                    )
            kill_request_user = schemas.StrSchema
            state = schemas.StrSchema
            
            
            class statistics(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class energy(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                
                                    @staticmethod
                                    def consumed() -> typing.Type['V0039Uint64NoVal']:
                                        return V0039Uint64NoVal
                                    __annotations__ = {
                                        "consumed": consumed,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["consumed"]) -> 'V0039Uint64NoVal': ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["consumed", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["consumed"]) -> typing.Union['V0039Uint64NoVal', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["consumed", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                consumed: typing.Union['V0039Uint64NoVal', schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'energy':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    consumed=consumed,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "energy": energy,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["energy"]) -> MetaOapg.properties.energy: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["energy", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["energy"]) -> typing.Union[MetaOapg.properties.energy, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["energy", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    energy: typing.Union[MetaOapg.properties.energy, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'statistics':
                    return super().__new__(
                        cls,
                        *_args,
                        energy=energy,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class step(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        name = schemas.StrSchema
                        __annotations__ = {
                            "name": name,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'step':
                    return super().__new__(
                        cls,
                        *_args,
                        name=name,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class task(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        distribution = schemas.StrSchema
                        __annotations__ = {
                            "distribution": distribution,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["distribution"]) -> MetaOapg.properties.distribution: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["distribution", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["distribution"]) -> typing.Union[MetaOapg.properties.distribution, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["distribution", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    distribution: typing.Union[MetaOapg.properties.distribution, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'task':
                    return super().__new__(
                        cls,
                        *_args,
                        distribution=distribution,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class tres(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                    
                        @staticmethod
                        def allocated() -> typing.Type['V0039TresList']:
                            return V0039TresList
                        __annotations__ = {
                            "allocated": allocated,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["allocated"]) -> 'V0039TresList': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["allocated", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["allocated"]) -> typing.Union['V0039TresList', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allocated", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    allocated: typing.Union['V0039TresList', schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'tres':
                    return super().__new__(
                        cls,
                        *_args,
                        allocated=allocated,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "time": time,
                "exit_code": exit_code,
                "nodes": nodes,
                "tasks": tasks,
                "pid": pid,
                "CPU": CPU,
                "kill_request_user": kill_request_user,
                "state": state,
                "statistics": statistics,
                "step": step,
                "task": task,
                "tres": tres,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time"]) -> MetaOapg.properties.time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exit_code"]) -> 'V0039JobExitCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodes"]) -> MetaOapg.properties.nodes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tasks"]) -> MetaOapg.properties.tasks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pid"]) -> MetaOapg.properties.pid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CPU"]) -> MetaOapg.properties.CPU: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kill_request_user"]) -> MetaOapg.properties.kill_request_user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statistics"]) -> MetaOapg.properties.statistics: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["step"]) -> MetaOapg.properties.step: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task"]) -> MetaOapg.properties.task: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tres"]) -> MetaOapg.properties.tres: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["time", "exit_code", "nodes", "tasks", "pid", "CPU", "kill_request_user", "state", "statistics", "step", "task", "tres", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time"]) -> typing.Union[MetaOapg.properties.time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exit_code"]) -> typing.Union['V0039JobExitCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodes"]) -> typing.Union[MetaOapg.properties.nodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tasks"]) -> typing.Union[MetaOapg.properties.tasks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pid"]) -> typing.Union[MetaOapg.properties.pid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CPU"]) -> typing.Union[MetaOapg.properties.CPU, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kill_request_user"]) -> typing.Union[MetaOapg.properties.kill_request_user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statistics"]) -> typing.Union[MetaOapg.properties.statistics, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["step"]) -> typing.Union[MetaOapg.properties.step, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task"]) -> typing.Union[MetaOapg.properties.task, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tres"]) -> typing.Union[MetaOapg.properties.tres, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["time", "exit_code", "nodes", "tasks", "pid", "CPU", "kill_request_user", "state", "statistics", "step", "task", "tres", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        time: typing.Union[MetaOapg.properties.time, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        exit_code: typing.Union['V0039JobExitCode', schemas.Unset] = schemas.unset,
        nodes: typing.Union[MetaOapg.properties.nodes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        tasks: typing.Union[MetaOapg.properties.tasks, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        pid: typing.Union[MetaOapg.properties.pid, str, schemas.Unset] = schemas.unset,
        CPU: typing.Union[MetaOapg.properties.CPU, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        kill_request_user: typing.Union[MetaOapg.properties.kill_request_user, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        statistics: typing.Union[MetaOapg.properties.statistics, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        step: typing.Union[MetaOapg.properties.step, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        task: typing.Union[MetaOapg.properties.task, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        tres: typing.Union[MetaOapg.properties.tres, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V0039Step':
        return super().__new__(
            cls,
            *_args,
            time=time,
            exit_code=exit_code,
            nodes=nodes,
            tasks=tasks,
            pid=pid,
            CPU=CPU,
            kill_request_user=kill_request_user,
            state=state,
            statistics=statistics,
            step=step,
            task=task,
            tres=tres,
            _configuration=_configuration,
            **kwargs,
        )

from slurmrestapi.model.v0039_hostlist import V0039Hostlist
from slurmrestapi.model.v0039_job_exit_code import V0039JobExitCode
from slurmrestapi.model.v0039_tres_list import V0039TresList
from slurmrestapi.model.v0039_uint64_no_val import V0039Uint64NoVal
