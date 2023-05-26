import typing_extensions

from slurmrestapi.paths import PathValues
from slurmrestapi.apis.paths.slurm_v0_0_37_diag import SlurmV0037Diag
from slurmrestapi.apis.paths.slurm_v0_0_37_ping import SlurmV0037Ping
from slurmrestapi.apis.paths.slurm_v0_0_37_jobs import SlurmV0037Jobs
from slurmrestapi.apis.paths.slurm_v0_0_37_job_job_id import SlurmV0037JobJobId
from slurmrestapi.apis.paths.slurm_v0_0_37_job_submit import SlurmV0037JobSubmit
from slurmrestapi.apis.paths.slurm_v0_0_37_nodes import SlurmV0037Nodes
from slurmrestapi.apis.paths.slurm_v0_0_37_node_node_name import SlurmV0037NodeNodeName
from slurmrestapi.apis.paths.slurm_v0_0_37_partitions import SlurmV0037Partitions
from slurmrestapi.apis.paths.slurm_v0_0_37_partition_partition_name import SlurmV0037PartitionPartitionName
from slurmrestapi.apis.paths.slurm_v0_0_37_reservations import SlurmV0037Reservations
from slurmrestapi.apis.paths.slurm_v0_0_37_reservation_reservation_name import SlurmV0037ReservationReservationName
from slurmrestapi.apis.paths.openapi_yaml import OpenapiYaml
from slurmrestapi.apis.paths.openapi_json import OpenapiJson
from slurmrestapi.apis.paths.openapi import Openapi
from slurmrestapi.apis.paths.openapi_v3 import OpenapiV3
from slurmrestapi.apis.paths.slurmdb_v0_0_37_job_job_id import SlurmdbV0037JobJobId
from slurmrestapi.apis.paths.slurmdb_v0_0_37_config import SlurmdbV0037Config
from slurmrestapi.apis.paths.slurmdb_v0_0_37_tres import SlurmdbV0037Tres
from slurmrestapi.apis.paths.slurmdb_v0_0_37_qos_qos_name import SlurmdbV0037QosQosName
from slurmrestapi.apis.paths.slurmdb_v0_0_37_qos import SlurmdbV0037Qos
from slurmrestapi.apis.paths.slurmdb_v0_0_37_associations import SlurmdbV0037Associations
from slurmrestapi.apis.paths.slurmdb_v0_0_37_association import SlurmdbV0037Association
from slurmrestapi.apis.paths.slurmdb_v0_0_37_user_user_name import SlurmdbV0037UserUserName
from slurmrestapi.apis.paths.slurmdb_v0_0_37_users import SlurmdbV0037Users
from slurmrestapi.apis.paths.slurmdb_v0_0_37_cluster_cluster_name import SlurmdbV0037ClusterClusterName
from slurmrestapi.apis.paths.slurmdb_v0_0_37_clusters import SlurmdbV0037Clusters
from slurmrestapi.apis.paths.slurmdb_v0_0_37_wckey_wckey import SlurmdbV0037WckeyWckey
from slurmrestapi.apis.paths.slurmdb_v0_0_37_wckeys import SlurmdbV0037Wckeys
from slurmrestapi.apis.paths.slurmdb_v0_0_37_account_account_name import SlurmdbV0037AccountAccountName
from slurmrestapi.apis.paths.slurmdb_v0_0_37_accounts import SlurmdbV0037Accounts
from slurmrestapi.apis.paths.slurmdb_v0_0_37_jobs import SlurmdbV0037Jobs
from slurmrestapi.apis.paths.slurmdb_v0_0_37_diag import SlurmdbV0037Diag

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SLURM_V0_0_37_DIAG: SlurmV0037Diag,
        PathValues.SLURM_V0_0_37_PING: SlurmV0037Ping,
        PathValues.SLURM_V0_0_37_JOBS: SlurmV0037Jobs,
        PathValues.SLURM_V0_0_37_JOB_JOB_ID: SlurmV0037JobJobId,
        PathValues.SLURM_V0_0_37_JOB_SUBMIT: SlurmV0037JobSubmit,
        PathValues.SLURM_V0_0_37_NODES: SlurmV0037Nodes,
        PathValues.SLURM_V0_0_37_NODE_NODE_NAME: SlurmV0037NodeNodeName,
        PathValues.SLURM_V0_0_37_PARTITIONS: SlurmV0037Partitions,
        PathValues.SLURM_V0_0_37_PARTITION_PARTITION_NAME: SlurmV0037PartitionPartitionName,
        PathValues.SLURM_V0_0_37_RESERVATIONS: SlurmV0037Reservations,
        PathValues.SLURM_V0_0_37_RESERVATION_RESERVATION_NAME: SlurmV0037ReservationReservationName,
        PathValues.OPENAPI_YAML: OpenapiYaml,
        PathValues.OPENAPI_JSON: OpenapiJson,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_V3: OpenapiV3,
        PathValues.SLURMDB_V0_0_37_JOB_JOB_ID: SlurmdbV0037JobJobId,
        PathValues.SLURMDB_V0_0_37_CONFIG: SlurmdbV0037Config,
        PathValues.SLURMDB_V0_0_37_TRES: SlurmdbV0037Tres,
        PathValues.SLURMDB_V0_0_37_QOS_QOS_NAME: SlurmdbV0037QosQosName,
        PathValues.SLURMDB_V0_0_37_QOS: SlurmdbV0037Qos,
        PathValues.SLURMDB_V0_0_37_ASSOCIATIONS: SlurmdbV0037Associations,
        PathValues.SLURMDB_V0_0_37_ASSOCIATION: SlurmdbV0037Association,
        PathValues.SLURMDB_V0_0_37_USER_USER_NAME: SlurmdbV0037UserUserName,
        PathValues.SLURMDB_V0_0_37_USERS: SlurmdbV0037Users,
        PathValues.SLURMDB_V0_0_37_CLUSTER_CLUSTER_NAME: SlurmdbV0037ClusterClusterName,
        PathValues.SLURMDB_V0_0_37_CLUSTERS: SlurmdbV0037Clusters,
        PathValues.SLURMDB_V0_0_37_WCKEY_WCKEY: SlurmdbV0037WckeyWckey,
        PathValues.SLURMDB_V0_0_37_WCKEYS: SlurmdbV0037Wckeys,
        PathValues.SLURMDB_V0_0_37_ACCOUNT_ACCOUNT_NAME: SlurmdbV0037AccountAccountName,
        PathValues.SLURMDB_V0_0_37_ACCOUNTS: SlurmdbV0037Accounts,
        PathValues.SLURMDB_V0_0_37_JOBS: SlurmdbV0037Jobs,
        PathValues.SLURMDB_V0_0_37_DIAG: SlurmdbV0037Diag,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SLURM_V0_0_37_DIAG: SlurmV0037Diag,
        PathValues.SLURM_V0_0_37_PING: SlurmV0037Ping,
        PathValues.SLURM_V0_0_37_JOBS: SlurmV0037Jobs,
        PathValues.SLURM_V0_0_37_JOB_JOB_ID: SlurmV0037JobJobId,
        PathValues.SLURM_V0_0_37_JOB_SUBMIT: SlurmV0037JobSubmit,
        PathValues.SLURM_V0_0_37_NODES: SlurmV0037Nodes,
        PathValues.SLURM_V0_0_37_NODE_NODE_NAME: SlurmV0037NodeNodeName,
        PathValues.SLURM_V0_0_37_PARTITIONS: SlurmV0037Partitions,
        PathValues.SLURM_V0_0_37_PARTITION_PARTITION_NAME: SlurmV0037PartitionPartitionName,
        PathValues.SLURM_V0_0_37_RESERVATIONS: SlurmV0037Reservations,
        PathValues.SLURM_V0_0_37_RESERVATION_RESERVATION_NAME: SlurmV0037ReservationReservationName,
        PathValues.OPENAPI_YAML: OpenapiYaml,
        PathValues.OPENAPI_JSON: OpenapiJson,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_V3: OpenapiV3,
        PathValues.SLURMDB_V0_0_37_JOB_JOB_ID: SlurmdbV0037JobJobId,
        PathValues.SLURMDB_V0_0_37_CONFIG: SlurmdbV0037Config,
        PathValues.SLURMDB_V0_0_37_TRES: SlurmdbV0037Tres,
        PathValues.SLURMDB_V0_0_37_QOS_QOS_NAME: SlurmdbV0037QosQosName,
        PathValues.SLURMDB_V0_0_37_QOS: SlurmdbV0037Qos,
        PathValues.SLURMDB_V0_0_37_ASSOCIATIONS: SlurmdbV0037Associations,
        PathValues.SLURMDB_V0_0_37_ASSOCIATION: SlurmdbV0037Association,
        PathValues.SLURMDB_V0_0_37_USER_USER_NAME: SlurmdbV0037UserUserName,
        PathValues.SLURMDB_V0_0_37_USERS: SlurmdbV0037Users,
        PathValues.SLURMDB_V0_0_37_CLUSTER_CLUSTER_NAME: SlurmdbV0037ClusterClusterName,
        PathValues.SLURMDB_V0_0_37_CLUSTERS: SlurmdbV0037Clusters,
        PathValues.SLURMDB_V0_0_37_WCKEY_WCKEY: SlurmdbV0037WckeyWckey,
        PathValues.SLURMDB_V0_0_37_WCKEYS: SlurmdbV0037Wckeys,
        PathValues.SLURMDB_V0_0_37_ACCOUNT_ACCOUNT_NAME: SlurmdbV0037AccountAccountName,
        PathValues.SLURMDB_V0_0_37_ACCOUNTS: SlurmdbV0037Accounts,
        PathValues.SLURMDB_V0_0_37_JOBS: SlurmdbV0037Jobs,
        PathValues.SLURMDB_V0_0_37_DIAG: SlurmdbV0037Diag,
    }
)
