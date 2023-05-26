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


class V0038Errors(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Slurm errors
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['V0038Error']:
            return V0038Error

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['V0038Error'], typing.List['V0038Error']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'V0038Errors':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'V0038Error':
        return super().__getitem__(i)

from slurmrestapi.model.v0038_error import V0038Error
