# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slurmrestapi.paths.openapi_v3 import Api

from slurmrestapi.paths import PathValues

path = PathValues.OPENAPI_V3