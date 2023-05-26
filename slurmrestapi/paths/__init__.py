# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slurmrestapi.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    SLURM_V0_0_38_DIAG = "/slurm/v0.0.38/diag"
    SLURM_V0_0_38_LICENSES = "/slurm/v0.0.38/licenses"
    SLURM_V0_0_38_PING = "/slurm/v0.0.38/ping"
    SLURM_V0_0_38_JOBS = "/slurm/v0.0.38/jobs"
    SLURM_V0_0_38_JOB_JOB_ID = "/slurm/v0.0.38/job/{job_id}"
    SLURM_V0_0_38_JOB_SUBMIT = "/slurm/v0.0.38/job/submit"
    SLURM_V0_0_38_NODES = "/slurm/v0.0.38/nodes"
    SLURM_V0_0_38_NODE_NODE_NAME = "/slurm/v0.0.38/node/{node_name}"
    SLURM_V0_0_38_PARTITIONS = "/slurm/v0.0.38/partitions"
    SLURM_V0_0_38_PARTITION_PARTITION_NAME = "/slurm/v0.0.38/partition/{partition_name}"
    SLURM_V0_0_38_RESERVATIONS = "/slurm/v0.0.38/reservations"
    SLURM_V0_0_38_RESERVATION_RESERVATION_NAME = "/slurm/v0.0.38/reservation/{reservation_name}"
    OPENAPI_YAML = "/openapi.yaml"
    OPENAPI_JSON = "/openapi.json"
    OPENAPI = "/openapi"
    OPENAPI_V3 = "/openapi/v3"
    SLURMDB_V0_0_38_JOB_JOB_ID = "/slurmdb/v0.0.38/job/{job_id}"
    SLURMDB_V0_0_38_CONFIG = "/slurmdb/v0.0.38/config"
    SLURMDB_V0_0_38_TRES = "/slurmdb/v0.0.38/tres"
    SLURMDB_V0_0_38_QOS_QOS_NAME = "/slurmdb/v0.0.38/qos/{qos_name}"
    SLURMDB_V0_0_38_QOS = "/slurmdb/v0.0.38/qos"
    SLURMDB_V0_0_38_ASSOCIATIONS = "/slurmdb/v0.0.38/associations"
    SLURMDB_V0_0_38_ASSOCIATION = "/slurmdb/v0.0.38/association"
    SLURMDB_V0_0_38_USER_USER_NAME = "/slurmdb/v0.0.38/user/{user_name}"
    SLURMDB_V0_0_38_USERS = "/slurmdb/v0.0.38/users"
    SLURMDB_V0_0_38_CLUSTER_CLUSTER_NAME = "/slurmdb/v0.0.38/cluster/{cluster_name}"
    SLURMDB_V0_0_38_CLUSTERS = "/slurmdb/v0.0.38/clusters"
    SLURMDB_V0_0_38_WCKEY_WCKEY = "/slurmdb/v0.0.38/wckey/{wckey}"
    SLURMDB_V0_0_38_WCKEYS = "/slurmdb/v0.0.38/wckeys"
    SLURMDB_V0_0_38_ACCOUNT_ACCOUNT_NAME = "/slurmdb/v0.0.38/account/{account_name}"
    SLURMDB_V0_0_38_ACCOUNTS = "/slurmdb/v0.0.38/accounts"
    SLURMDB_V0_0_38_JOBS = "/slurmdb/v0.0.38/jobs"
    SLURMDB_V0_0_38_DIAG = "/slurmdb/v0.0.38/diag"
