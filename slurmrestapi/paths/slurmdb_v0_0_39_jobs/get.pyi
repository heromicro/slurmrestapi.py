# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from slurmrestapi import api_client, exceptions
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

from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_job_info import Dbv0039JobInfo

# Query params
UsersSchema = schemas.StrSchema
SubmitTimeSchema = schemas.StrSchema
StartTimeSchema = schemas.StrSchema
EndTimeSchema = schemas.StrSchema
AccountSchema = schemas.StrSchema
AssociationSchema = schemas.StrSchema
ClusterSchema = schemas.StrSchema
ConstraintsSchema = schemas.StrSchema
CpusMaxSchema = schemas.StrSchema
CpusMinSchema = schemas.StrSchema


class SkipStepsSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
    
    @schemas.classproperty
    def FALSE(cls):
        return cls("false")


class DisableWaitForResultSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
    
    @schemas.classproperty
    def FALSE(cls):
        return cls("false")
ExitCodeSchema = schemas.StrSchema
FormatSchema = schemas.StrSchema
GroupSchema = schemas.StrSchema
JobNameSchema = schemas.StrSchema
NodesMaxSchema = schemas.StrSchema
NodesMinSchema = schemas.StrSchema
PartitionSchema = schemas.StrSchema
QosSchema = schemas.StrSchema
ReasonSchema = schemas.StrSchema
ReservationSchema = schemas.StrSchema
StateSchema = schemas.StrSchema
StepSchema = schemas.StrSchema
NodeSchema = schemas.StrSchema
WckeySchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'users': typing.Union[UsersSchema, str, ],
        'submit_time': typing.Union[SubmitTimeSchema, str, ],
        'start_time': typing.Union[StartTimeSchema, str, ],
        'end_time': typing.Union[EndTimeSchema, str, ],
        'account': typing.Union[AccountSchema, str, ],
        'association': typing.Union[AssociationSchema, str, ],
        'cluster': typing.Union[ClusterSchema, str, ],
        'constraints': typing.Union[ConstraintsSchema, str, ],
        'cpus_max': typing.Union[CpusMaxSchema, str, ],
        'cpus_min': typing.Union[CpusMinSchema, str, ],
        'skip_steps': typing.Union[SkipStepsSchema, str, ],
        'disable_wait_for_result': typing.Union[DisableWaitForResultSchema, str, ],
        'exit_code': typing.Union[ExitCodeSchema, str, ],
        'format': typing.Union[FormatSchema, str, ],
        'group': typing.Union[GroupSchema, str, ],
        'job_name': typing.Union[JobNameSchema, str, ],
        'nodes_max': typing.Union[NodesMaxSchema, str, ],
        'nodes_min': typing.Union[NodesMinSchema, str, ],
        'partition': typing.Union[PartitionSchema, str, ],
        'qos': typing.Union[QosSchema, str, ],
        'reason': typing.Union[ReasonSchema, str, ],
        'reservation': typing.Union[ReservationSchema, str, ],
        'state': typing.Union[StateSchema, str, ],
        'step': typing.Union[StepSchema, str, ],
        'node': typing.Union[NodeSchema, str, ],
        'wckey': typing.Union[WckeySchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_users = api_client.QueryParameter(
    name="users",
    style=api_client.ParameterStyle.FORM,
    schema=UsersSchema,
)
request_query_submit_time = api_client.QueryParameter(
    name="submit_time",
    style=api_client.ParameterStyle.FORM,
    schema=SubmitTimeSchema,
)
request_query_start_time = api_client.QueryParameter(
    name="start_time",
    style=api_client.ParameterStyle.FORM,
    schema=StartTimeSchema,
)
request_query_end_time = api_client.QueryParameter(
    name="end_time",
    style=api_client.ParameterStyle.FORM,
    schema=EndTimeSchema,
)
request_query_account = api_client.QueryParameter(
    name="account",
    style=api_client.ParameterStyle.FORM,
    schema=AccountSchema,
)
request_query_association = api_client.QueryParameter(
    name="association",
    style=api_client.ParameterStyle.FORM,
    schema=AssociationSchema,
)
request_query_cluster = api_client.QueryParameter(
    name="cluster",
    style=api_client.ParameterStyle.FORM,
    schema=ClusterSchema,
)
request_query_constraints = api_client.QueryParameter(
    name="constraints",
    style=api_client.ParameterStyle.FORM,
    schema=ConstraintsSchema,
)
request_query_cpus_max = api_client.QueryParameter(
    name="cpus_max",
    style=api_client.ParameterStyle.FORM,
    schema=CpusMaxSchema,
)
request_query_cpus_min = api_client.QueryParameter(
    name="cpus_min",
    style=api_client.ParameterStyle.FORM,
    schema=CpusMinSchema,
)
request_query_skip_steps = api_client.QueryParameter(
    name="skip_steps",
    style=api_client.ParameterStyle.FORM,
    schema=SkipStepsSchema,
)
request_query_disable_wait_for_result = api_client.QueryParameter(
    name="disable_wait_for_result",
    style=api_client.ParameterStyle.FORM,
    schema=DisableWaitForResultSchema,
)
request_query_exit_code = api_client.QueryParameter(
    name="exit_code",
    style=api_client.ParameterStyle.FORM,
    schema=ExitCodeSchema,
)
request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
)
request_query_group = api_client.QueryParameter(
    name="group",
    style=api_client.ParameterStyle.FORM,
    schema=GroupSchema,
)
request_query_job_name = api_client.QueryParameter(
    name="job_name",
    style=api_client.ParameterStyle.FORM,
    schema=JobNameSchema,
)
request_query_nodes_max = api_client.QueryParameter(
    name="nodes_max",
    style=api_client.ParameterStyle.FORM,
    schema=NodesMaxSchema,
)
request_query_nodes_min = api_client.QueryParameter(
    name="nodes_min",
    style=api_client.ParameterStyle.FORM,
    schema=NodesMinSchema,
)
request_query_partition = api_client.QueryParameter(
    name="partition",
    style=api_client.ParameterStyle.FORM,
    schema=PartitionSchema,
)
request_query_qos = api_client.QueryParameter(
    name="qos",
    style=api_client.ParameterStyle.FORM,
    schema=QosSchema,
)
request_query_reason = api_client.QueryParameter(
    name="reason",
    style=api_client.ParameterStyle.FORM,
    schema=ReasonSchema,
)
request_query_reservation = api_client.QueryParameter(
    name="reservation",
    style=api_client.ParameterStyle.FORM,
    schema=ReservationSchema,
)
request_query_state = api_client.QueryParameter(
    name="state",
    style=api_client.ParameterStyle.FORM,
    schema=StateSchema,
)
request_query_step = api_client.QueryParameter(
    name="step",
    style=api_client.ParameterStyle.FORM,
    schema=StepSchema,
)
request_query_node = api_client.QueryParameter(
    name="node",
    style=api_client.ParameterStyle.FORM,
    schema=NodeSchema,
)
request_query_wckey = api_client.QueryParameter(
    name="wckey",
    style=api_client.ParameterStyle.FORM,
    schema=WckeySchema,
)
SchemaFor200ResponseBodyApplicationJson = Dbv0039JobInfo
SchemaFor200ResponseBodyApplicationXYaml = Dbv0039JobInfo


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyApplicationXYaml,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/x-yaml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXYaml),
    },
)
SchemaFor0ResponseBodyApplicationJson = Status
SchemaFor0ResponseBodyApplicationXYaml = Status


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor0ResponseBodyApplicationJson,
        SchemaFor0ResponseBodyApplicationXYaml,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
        'application/x-yaml': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationXYaml),
    },
)
_all_accept_content_types = (
    'application/json',
    'application/x-yaml',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _slurmdb_v0039_get_jobs_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def _slurmdb_v0039_get_jobs_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _slurmdb_v0039_get_jobs_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _slurmdb_v0039_get_jobs_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Get job list
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_users,
            request_query_submit_time,
            request_query_start_time,
            request_query_end_time,
            request_query_account,
            request_query_association,
            request_query_cluster,
            request_query_constraints,
            request_query_cpus_max,
            request_query_cpus_min,
            request_query_skip_steps,
            request_query_disable_wait_for_result,
            request_query_exit_code,
            request_query_format,
            request_query_group,
            request_query_job_name,
            request_query_nodes_max,
            request_query_nodes_min,
            request_query_partition,
            request_query_qos,
            request_query_reason,
            request_query_reservation,
            request_query_state,
            request_query_step,
            request_query_node,
            request_query_wckey,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                default_response = _status_code_to_response.get('default')
                if default_response:
                    api_response = default_response.deserialize(response, self.api_client.configuration)
                else:
                    api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class SlurmdbV0039GetJobs(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def slurmdb_v0039_get_jobs(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def slurmdb_v0039_get_jobs(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def slurmdb_v0039_get_jobs(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def slurmdb_v0039_get_jobs(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._slurmdb_v0039_get_jobs_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._slurmdb_v0039_get_jobs_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


