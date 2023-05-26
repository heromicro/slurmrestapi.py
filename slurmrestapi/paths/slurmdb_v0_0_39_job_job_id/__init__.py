# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slurmrestapi.paths.slurmdb_v0_0_39_job_job_id import Api

from slurmrestapi.paths import PathValues

path = PathValues.SLURMDB_V0_0_39_JOB_JOB_ID