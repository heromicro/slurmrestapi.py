# coding: utf-8

"""
    Slurm Rest API

    API to access and control Slurm.  # noqa: E501

    The version of the OpenAPI document: 0.0.37
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


class V0037JobSubmission(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "script",
        }
        
        class properties:
            script = schemas.StrSchema
        
            @staticmethod
            def job() -> typing.Type['V0037JobProperties']:
                return V0037JobProperties
            
            
            class jobs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V0037JobProperties']:
                        return V0037JobProperties
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['V0037JobProperties'], typing.List['V0037JobProperties']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'jobs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V0037JobProperties':
                    return super().__getitem__(i)
            __annotations__ = {
                "script": script,
                "job": job,
                "jobs": jobs,
            }

    
    script: MetaOapg.properties.script
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["script"]) -> MetaOapg.properties.script: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job"]) -> 'V0037JobProperties': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobs"]) -> MetaOapg.properties.jobs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["script", "job", "jobs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["script"]) -> MetaOapg.properties.script: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job"]) -> typing.Union['V0037JobProperties', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobs"]) -> typing.Union[MetaOapg.properties.jobs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["script", "job", "jobs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        script: typing.Union[MetaOapg.properties.script, str, ],
        job: typing.Union['V0037JobProperties', schemas.Unset] = schemas.unset,
        jobs: typing.Union[MetaOapg.properties.jobs, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V0037JobSubmission':
        return super().__new__(
            cls,
            *_args,
            script=script,
            job=job,
            jobs=jobs,
            _configuration=_configuration,
            **kwargs,
        )

from slurmrestapi.model.v0037_job_properties import V0037JobProperties
