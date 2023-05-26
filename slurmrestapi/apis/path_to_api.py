import typing_extensions

from slurmrestapi.paths import PathValues
from slurmrestapi.apis.paths.slurm_v0_0_38_diag import SlurmV0038Diag
from slurmrestapi.apis.paths.slurm_v0_0_38_licenses import SlurmV0038Licenses
from slurmrestapi.apis.paths.slurm_v0_0_38_ping import SlurmV0038Ping
from slurmrestapi.apis.paths.slurm_v0_0_38_jobs import SlurmV0038Jobs
from slurmrestapi.apis.paths.slurm_v0_0_38_job_job_id import SlurmV0038JobJobId
from slurmrestapi.apis.paths.slurm_v0_0_38_job_submit import SlurmV0038JobSubmit
from slurmrestapi.apis.paths.slurm_v0_0_38_nodes import SlurmV0038Nodes
from slurmrestapi.apis.paths.slurm_v0_0_38_node_node_name import SlurmV0038NodeNodeName
from slurmrestapi.apis.paths.slurm_v0_0_38_partitions import SlurmV0038Partitions
from slurmrestapi.apis.paths.slurm_v0_0_38_partition_partition_name import SlurmV0038PartitionPartitionName
from slurmrestapi.apis.paths.slurm_v0_0_38_reservations import SlurmV0038Reservations
from slurmrestapi.apis.paths.slurm_v0_0_38_reservation_reservation_name import SlurmV0038ReservationReservationName
from slurmrestapi.apis.paths.openapi_yaml import OpenapiYaml
from slurmrestapi.apis.paths.openapi_json import OpenapiJson
from slurmrestapi.apis.paths.openapi import Openapi
from slurmrestapi.apis.paths.openapi_v3 import OpenapiV3
from slurmrestapi.apis.paths.slurmdb_v0_0_38_job_job_id import SlurmdbV0038JobJobId
from slurmrestapi.apis.paths.slurmdb_v0_0_38_config import SlurmdbV0038Config
from slurmrestapi.apis.paths.slurmdb_v0_0_38_tres import SlurmdbV0038Tres
from slurmrestapi.apis.paths.slurmdb_v0_0_38_qos_qos_name import SlurmdbV0038QosQosName
from slurmrestapi.apis.paths.slurmdb_v0_0_38_qos import SlurmdbV0038Qos
from slurmrestapi.apis.paths.slurmdb_v0_0_38_associations import SlurmdbV0038Associations
from slurmrestapi.apis.paths.slurmdb_v0_0_38_association import SlurmdbV0038Association
from slurmrestapi.apis.paths.slurmdb_v0_0_38_user_user_name import SlurmdbV0038UserUserName
from slurmrestapi.apis.paths.slurmdb_v0_0_38_users import SlurmdbV0038Users
from slurmrestapi.apis.paths.slurmdb_v0_0_38_cluster_cluster_name import SlurmdbV0038ClusterClusterName
from slurmrestapi.apis.paths.slurmdb_v0_0_38_clusters import SlurmdbV0038Clusters
from slurmrestapi.apis.paths.slurmdb_v0_0_38_wckey_wckey import SlurmdbV0038WckeyWckey
from slurmrestapi.apis.paths.slurmdb_v0_0_38_wckeys import SlurmdbV0038Wckeys
from slurmrestapi.apis.paths.slurmdb_v0_0_38_account_account_name import SlurmdbV0038AccountAccountName
from slurmrestapi.apis.paths.slurmdb_v0_0_38_accounts import SlurmdbV0038Accounts
from slurmrestapi.apis.paths.slurmdb_v0_0_38_jobs import SlurmdbV0038Jobs
from slurmrestapi.apis.paths.slurmdb_v0_0_38_diag import SlurmdbV0038Diag

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SLURM_V0_0_38_DIAG: SlurmV0038Diag,
        PathValues.SLURM_V0_0_38_LICENSES: SlurmV0038Licenses,
        PathValues.SLURM_V0_0_38_PING: SlurmV0038Ping,
        PathValues.SLURM_V0_0_38_JOBS: SlurmV0038Jobs,
        PathValues.SLURM_V0_0_38_JOB_JOB_ID: SlurmV0038JobJobId,
        PathValues.SLURM_V0_0_38_JOB_SUBMIT: SlurmV0038JobSubmit,
        PathValues.SLURM_V0_0_38_NODES: SlurmV0038Nodes,
        PathValues.SLURM_V0_0_38_NODE_NODE_NAME: SlurmV0038NodeNodeName,
        PathValues.SLURM_V0_0_38_PARTITIONS: SlurmV0038Partitions,
        PathValues.SLURM_V0_0_38_PARTITION_PARTITION_NAME: SlurmV0038PartitionPartitionName,
        PathValues.SLURM_V0_0_38_RESERVATIONS: SlurmV0038Reservations,
        PathValues.SLURM_V0_0_38_RESERVATION_RESERVATION_NAME: SlurmV0038ReservationReservationName,
        PathValues.OPENAPI_YAML: OpenapiYaml,
        PathValues.OPENAPI_JSON: OpenapiJson,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_V3: OpenapiV3,
        PathValues.SLURMDB_V0_0_38_JOB_JOB_ID: SlurmdbV0038JobJobId,
        PathValues.SLURMDB_V0_0_38_CONFIG: SlurmdbV0038Config,
        PathValues.SLURMDB_V0_0_38_TRES: SlurmdbV0038Tres,
        PathValues.SLURMDB_V0_0_38_QOS_QOS_NAME: SlurmdbV0038QosQosName,
        PathValues.SLURMDB_V0_0_38_QOS: SlurmdbV0038Qos,
        PathValues.SLURMDB_V0_0_38_ASSOCIATIONS: SlurmdbV0038Associations,
        PathValues.SLURMDB_V0_0_38_ASSOCIATION: SlurmdbV0038Association,
        PathValues.SLURMDB_V0_0_38_USER_USER_NAME: SlurmdbV0038UserUserName,
        PathValues.SLURMDB_V0_0_38_USERS: SlurmdbV0038Users,
        PathValues.SLURMDB_V0_0_38_CLUSTER_CLUSTER_NAME: SlurmdbV0038ClusterClusterName,
        PathValues.SLURMDB_V0_0_38_CLUSTERS: SlurmdbV0038Clusters,
        PathValues.SLURMDB_V0_0_38_WCKEY_WCKEY: SlurmdbV0038WckeyWckey,
        PathValues.SLURMDB_V0_0_38_WCKEYS: SlurmdbV0038Wckeys,
        PathValues.SLURMDB_V0_0_38_ACCOUNT_ACCOUNT_NAME: SlurmdbV0038AccountAccountName,
        PathValues.SLURMDB_V0_0_38_ACCOUNTS: SlurmdbV0038Accounts,
        PathValues.SLURMDB_V0_0_38_JOBS: SlurmdbV0038Jobs,
        PathValues.SLURMDB_V0_0_38_DIAG: SlurmdbV0038Diag,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SLURM_V0_0_38_DIAG: SlurmV0038Diag,
        PathValues.SLURM_V0_0_38_LICENSES: SlurmV0038Licenses,
        PathValues.SLURM_V0_0_38_PING: SlurmV0038Ping,
        PathValues.SLURM_V0_0_38_JOBS: SlurmV0038Jobs,
        PathValues.SLURM_V0_0_38_JOB_JOB_ID: SlurmV0038JobJobId,
        PathValues.SLURM_V0_0_38_JOB_SUBMIT: SlurmV0038JobSubmit,
        PathValues.SLURM_V0_0_38_NODES: SlurmV0038Nodes,
        PathValues.SLURM_V0_0_38_NODE_NODE_NAME: SlurmV0038NodeNodeName,
        PathValues.SLURM_V0_0_38_PARTITIONS: SlurmV0038Partitions,
        PathValues.SLURM_V0_0_38_PARTITION_PARTITION_NAME: SlurmV0038PartitionPartitionName,
        PathValues.SLURM_V0_0_38_RESERVATIONS: SlurmV0038Reservations,
        PathValues.SLURM_V0_0_38_RESERVATION_RESERVATION_NAME: SlurmV0038ReservationReservationName,
        PathValues.OPENAPI_YAML: OpenapiYaml,
        PathValues.OPENAPI_JSON: OpenapiJson,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_V3: OpenapiV3,
        PathValues.SLURMDB_V0_0_38_JOB_JOB_ID: SlurmdbV0038JobJobId,
        PathValues.SLURMDB_V0_0_38_CONFIG: SlurmdbV0038Config,
        PathValues.SLURMDB_V0_0_38_TRES: SlurmdbV0038Tres,
        PathValues.SLURMDB_V0_0_38_QOS_QOS_NAME: SlurmdbV0038QosQosName,
        PathValues.SLURMDB_V0_0_38_QOS: SlurmdbV0038Qos,
        PathValues.SLURMDB_V0_0_38_ASSOCIATIONS: SlurmdbV0038Associations,
        PathValues.SLURMDB_V0_0_38_ASSOCIATION: SlurmdbV0038Association,
        PathValues.SLURMDB_V0_0_38_USER_USER_NAME: SlurmdbV0038UserUserName,
        PathValues.SLURMDB_V0_0_38_USERS: SlurmdbV0038Users,
        PathValues.SLURMDB_V0_0_38_CLUSTER_CLUSTER_NAME: SlurmdbV0038ClusterClusterName,
        PathValues.SLURMDB_V0_0_38_CLUSTERS: SlurmdbV0038Clusters,
        PathValues.SLURMDB_V0_0_38_WCKEY_WCKEY: SlurmdbV0038WckeyWckey,
        PathValues.SLURMDB_V0_0_38_WCKEYS: SlurmdbV0038Wckeys,
        PathValues.SLURMDB_V0_0_38_ACCOUNT_ACCOUNT_NAME: SlurmdbV0038AccountAccountName,
        PathValues.SLURMDB_V0_0_38_ACCOUNTS: SlurmdbV0038Accounts,
        PathValues.SLURMDB_V0_0_38_JOBS: SlurmdbV0038Jobs,
        PathValues.SLURMDB_V0_0_38_DIAG: SlurmdbV0038Diag,
    }
)
