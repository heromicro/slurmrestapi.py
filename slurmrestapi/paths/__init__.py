# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slurmrestapi.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    SLURM_V0_0_39_DIAG = "/slurm/v0.0.39/diag"
    SLURM_V0_0_39_LICENSES = "/slurm/v0.0.39/licenses"
    SLURM_V0_0_39_PING = "/slurm/v0.0.39/ping"
    SLURM_V0_0_39_JOBS = "/slurm/v0.0.39/jobs"
    SLURM_V0_0_39_JOB_JOB_ID = "/slurm/v0.0.39/job/{job_id}"
    SLURM_V0_0_39_JOB_SUBMIT = "/slurm/v0.0.39/job/submit"
    SLURM_V0_0_39_NODES = "/slurm/v0.0.39/nodes"
    SLURM_V0_0_39_NODE_NODE_NAME = "/slurm/v0.0.39/node/{node_name}"
    SLURM_V0_0_39_PARTITIONS = "/slurm/v0.0.39/partitions"
    SLURM_V0_0_39_PARTITION_PARTITION_NAME = "/slurm/v0.0.39/partition/{partition_name}"
    SLURM_V0_0_39_RESERVATIONS = "/slurm/v0.0.39/reservations"
    SLURM_V0_0_39_RESERVATION_RESERVATION_NAME = "/slurm/v0.0.39/reservation/{reservation_name}"
    OPENAPI_YAML = "/openapi.yaml"
    OPENAPI_JSON = "/openapi.json"
    OPENAPI = "/openapi"
    OPENAPI_V3 = "/openapi/v3"
    SLURMDB_V0_0_39_JOB_JOB_ID = "/slurmdb/v0.0.39/job/{job_id}"
    SLURMDB_V0_0_39_CONFIG = "/slurmdb/v0.0.39/config"
    SLURMDB_V0_0_39_TRES = "/slurmdb/v0.0.39/tres"
    SLURMDB_V0_0_39_QOS_QOS_NAME = "/slurmdb/v0.0.39/qos/{qos_name}"
    SLURMDB_V0_0_39_QOS = "/slurmdb/v0.0.39/qos"
    SLURMDB_V0_0_39_ASSOCIATIONS = "/slurmdb/v0.0.39/associations"
    SLURMDB_V0_0_39_ASSOCIATION = "/slurmdb/v0.0.39/association"
    SLURMDB_V0_0_39_USER_USER_NAME = "/slurmdb/v0.0.39/user/{user_name}"
    SLURMDB_V0_0_39_USERS = "/slurmdb/v0.0.39/users"
    SLURMDB_V0_0_39_CLUSTER_CLUSTER_NAME = "/slurmdb/v0.0.39/cluster/{cluster_name}"
    SLURMDB_V0_0_39_CLUSTERS = "/slurmdb/v0.0.39/clusters"
    SLURMDB_V0_0_39_WCKEY_WCKEY = "/slurmdb/v0.0.39/wckey/{wckey}"
    SLURMDB_V0_0_39_WCKEYS = "/slurmdb/v0.0.39/wckeys"
    SLURMDB_V0_0_39_ACCOUNT_ACCOUNT_NAME = "/slurmdb/v0.0.39/account/{account_name}"
    SLURMDB_V0_0_39_ACCOUNTS = "/slurmdb/v0.0.39/accounts"
    SLURMDB_V0_0_39_JOBS = "/slurmdb/v0.0.39/jobs"
    SLURMDB_V0_0_39_DIAG = "/slurmdb/v0.0.39/diag"
