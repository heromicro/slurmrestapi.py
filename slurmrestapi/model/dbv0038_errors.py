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


class Dbv0038Errors(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Slurm errors
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['Dbv0038Error']:
            return Dbv0038Error

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['Dbv0038Error'], typing.List['Dbv0038Error']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Dbv0038Errors':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'Dbv0038Error':
        return super().__getitem__(i)

from slurmrestapi.model.dbv0038_error import Dbv0038Error
