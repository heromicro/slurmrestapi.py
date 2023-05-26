# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slurmrestapi.paths.slurmdb_v0_0_38_jobs import Api

from slurmrestapi.paths import PathValues

path = PathValues.SLURMDB_V0_0_38_JOBS