# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from slurmrestapi.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    SLURM_V0_0_37_DIAG = "/slurm/v0.0.37/diag"
    SLURM_V0_0_37_PING = "/slurm/v0.0.37/ping"
    SLURM_V0_0_37_JOBS = "/slurm/v0.0.37/jobs"
    SLURM_V0_0_37_JOB_JOB_ID = "/slurm/v0.0.37/job/{job_id}"
    SLURM_V0_0_37_JOB_SUBMIT = "/slurm/v0.0.37/job/submit"
    SLURM_V0_0_37_NODES = "/slurm/v0.0.37/nodes"
    SLURM_V0_0_37_NODE_NODE_NAME = "/slurm/v0.0.37/node/{node_name}"
    SLURM_V0_0_37_PARTITIONS = "/slurm/v0.0.37/partitions"
    SLURM_V0_0_37_PARTITION_PARTITION_NAME = "/slurm/v0.0.37/partition/{partition_name}"
    SLURM_V0_0_37_RESERVATIONS = "/slurm/v0.0.37/reservations"
    SLURM_V0_0_37_RESERVATION_RESERVATION_NAME = "/slurm/v0.0.37/reservation/{reservation_name}"
    OPENAPI_YAML = "/openapi.yaml"
    OPENAPI_JSON = "/openapi.json"
    OPENAPI = "/openapi"
    OPENAPI_V3 = "/openapi/v3"
    SLURMDB_V0_0_37_JOB_JOB_ID = "/slurmdb/v0.0.37/job/{job_id}"
    SLURMDB_V0_0_37_CONFIG = "/slurmdb/v0.0.37/config"
    SLURMDB_V0_0_37_TRES = "/slurmdb/v0.0.37/tres"
    SLURMDB_V0_0_37_QOS_QOS_NAME = "/slurmdb/v0.0.37/qos/{qos_name}"
    SLURMDB_V0_0_37_QOS = "/slurmdb/v0.0.37/qos"
    SLURMDB_V0_0_37_ASSOCIATIONS = "/slurmdb/v0.0.37/associations"
    SLURMDB_V0_0_37_ASSOCIATION = "/slurmdb/v0.0.37/association"
    SLURMDB_V0_0_37_USER_USER_NAME = "/slurmdb/v0.0.37/user/{user_name}"
    SLURMDB_V0_0_37_USERS = "/slurmdb/v0.0.37/users"
    SLURMDB_V0_0_37_CLUSTER_CLUSTER_NAME = "/slurmdb/v0.0.37/cluster/{cluster_name}"
    SLURMDB_V0_0_37_CLUSTERS = "/slurmdb/v0.0.37/clusters"
    SLURMDB_V0_0_37_WCKEY_WCKEY = "/slurmdb/v0.0.37/wckey/{wckey}"
    SLURMDB_V0_0_37_WCKEYS = "/slurmdb/v0.0.37/wckeys"
    SLURMDB_V0_0_37_ACCOUNT_ACCOUNT_NAME = "/slurmdb/v0.0.37/account/{account_name}"
    SLURMDB_V0_0_37_ACCOUNTS = "/slurmdb/v0.0.37/accounts"
    SLURMDB_V0_0_37_JOBS = "/slurmdb/v0.0.37/jobs"
    SLURMDB_V0_0_37_DIAG = "/slurmdb/v0.0.37/diag"
