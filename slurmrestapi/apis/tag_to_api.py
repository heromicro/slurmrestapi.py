import typing_extensions

from slurmrestapi.apis.tags import TagValues
from slurmrestapi.apis.tags.slurm_api import SlurmApi
from slurmrestapi.apis.tags.openapi_api import OpenapiApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SLURM: SlurmApi,
        TagValues.OPENAPI: OpenapiApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SLURM: SlurmApi,
        TagValues.OPENAPI: OpenapiApi,
    }
)
