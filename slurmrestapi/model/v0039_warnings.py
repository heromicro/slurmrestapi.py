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


class V0039Warnings(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Slurm warnings
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['V0039Warning']:
            return V0039Warning

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['V0039Warning'], typing.List['V0039Warning']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'V0039Warnings':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'V0039Warning':
        return super().__getitem__(i)

from slurmrestapi.model.v0039_warning import V0039Warning
