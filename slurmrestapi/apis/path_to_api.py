import typing_extensions

from slurmrestapi.paths import PathValues
from slurmrestapi.apis.paths.slurm_v0_0_39_diag import SlurmV0039Diag
from slurmrestapi.apis.paths.slurm_v0_0_39_licenses import SlurmV0039Licenses
from slurmrestapi.apis.paths.slurm_v0_0_39_ping import SlurmV0039Ping
from slurmrestapi.apis.paths.slurm_v0_0_39_jobs import SlurmV0039Jobs
from slurmrestapi.apis.paths.slurm_v0_0_39_job_job_id import SlurmV0039JobJobId
from slurmrestapi.apis.paths.slurm_v0_0_39_job_submit import SlurmV0039JobSubmit
from slurmrestapi.apis.paths.slurm_v0_0_39_nodes import SlurmV0039Nodes
from slurmrestapi.apis.paths.slurm_v0_0_39_node_node_name import SlurmV0039NodeNodeName
from slurmrestapi.apis.paths.slurm_v0_0_39_partitions import SlurmV0039Partitions
from slurmrestapi.apis.paths.slurm_v0_0_39_partition_partition_name import SlurmV0039PartitionPartitionName
from slurmrestapi.apis.paths.slurm_v0_0_39_reservations import SlurmV0039Reservations
from slurmrestapi.apis.paths.slurm_v0_0_39_reservation_reservation_name import SlurmV0039ReservationReservationName
from slurmrestapi.apis.paths.openapi_yaml import OpenapiYaml
from slurmrestapi.apis.paths.openapi_json import OpenapiJson
from slurmrestapi.apis.paths.openapi import Openapi
from slurmrestapi.apis.paths.openapi_v3 import OpenapiV3
from slurmrestapi.apis.paths.slurmdb_v0_0_39_job_job_id import SlurmdbV0039JobJobId
from slurmrestapi.apis.paths.slurmdb_v0_0_39_config import SlurmdbV0039Config
from slurmrestapi.apis.paths.slurmdb_v0_0_39_tres import SlurmdbV0039Tres
from slurmrestapi.apis.paths.slurmdb_v0_0_39_qos_qos_name import SlurmdbV0039QosQosName
from slurmrestapi.apis.paths.slurmdb_v0_0_39_qos import SlurmdbV0039Qos
from slurmrestapi.apis.paths.slurmdb_v0_0_39_associations import SlurmdbV0039Associations
from slurmrestapi.apis.paths.slurmdb_v0_0_39_association import SlurmdbV0039Association
from slurmrestapi.apis.paths.slurmdb_v0_0_39_user_user_name import SlurmdbV0039UserUserName
from slurmrestapi.apis.paths.slurmdb_v0_0_39_users import SlurmdbV0039Users
from slurmrestapi.apis.paths.slurmdb_v0_0_39_cluster_cluster_name import SlurmdbV0039ClusterClusterName
from slurmrestapi.apis.paths.slurmdb_v0_0_39_clusters import SlurmdbV0039Clusters
from slurmrestapi.apis.paths.slurmdb_v0_0_39_wckey_wckey import SlurmdbV0039WckeyWckey
from slurmrestapi.apis.paths.slurmdb_v0_0_39_wckeys import SlurmdbV0039Wckeys
from slurmrestapi.apis.paths.slurmdb_v0_0_39_account_account_name import SlurmdbV0039AccountAccountName
from slurmrestapi.apis.paths.slurmdb_v0_0_39_accounts import SlurmdbV0039Accounts
from slurmrestapi.apis.paths.slurmdb_v0_0_39_jobs import SlurmdbV0039Jobs
from slurmrestapi.apis.paths.slurmdb_v0_0_39_diag import SlurmdbV0039Diag

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SLURM_V0_0_39_DIAG: SlurmV0039Diag,
        PathValues.SLURM_V0_0_39_LICENSES: SlurmV0039Licenses,
        PathValues.SLURM_V0_0_39_PING: SlurmV0039Ping,
        PathValues.SLURM_V0_0_39_JOBS: SlurmV0039Jobs,
        PathValues.SLURM_V0_0_39_JOB_JOB_ID: SlurmV0039JobJobId,
        PathValues.SLURM_V0_0_39_JOB_SUBMIT: SlurmV0039JobSubmit,
        PathValues.SLURM_V0_0_39_NODES: SlurmV0039Nodes,
        PathValues.SLURM_V0_0_39_NODE_NODE_NAME: SlurmV0039NodeNodeName,
        PathValues.SLURM_V0_0_39_PARTITIONS: SlurmV0039Partitions,
        PathValues.SLURM_V0_0_39_PARTITION_PARTITION_NAME: SlurmV0039PartitionPartitionName,
        PathValues.SLURM_V0_0_39_RESERVATIONS: SlurmV0039Reservations,
        PathValues.SLURM_V0_0_39_RESERVATION_RESERVATION_NAME: SlurmV0039ReservationReservationName,
        PathValues.OPENAPI_YAML: OpenapiYaml,
        PathValues.OPENAPI_JSON: OpenapiJson,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_V3: OpenapiV3,
        PathValues.SLURMDB_V0_0_39_JOB_JOB_ID: SlurmdbV0039JobJobId,
        PathValues.SLURMDB_V0_0_39_CONFIG: SlurmdbV0039Config,
        PathValues.SLURMDB_V0_0_39_TRES: SlurmdbV0039Tres,
        PathValues.SLURMDB_V0_0_39_QOS_QOS_NAME: SlurmdbV0039QosQosName,
        PathValues.SLURMDB_V0_0_39_QOS: SlurmdbV0039Qos,
        PathValues.SLURMDB_V0_0_39_ASSOCIATIONS: SlurmdbV0039Associations,
        PathValues.SLURMDB_V0_0_39_ASSOCIATION: SlurmdbV0039Association,
        PathValues.SLURMDB_V0_0_39_USER_USER_NAME: SlurmdbV0039UserUserName,
        PathValues.SLURMDB_V0_0_39_USERS: SlurmdbV0039Users,
        PathValues.SLURMDB_V0_0_39_CLUSTER_CLUSTER_NAME: SlurmdbV0039ClusterClusterName,
        PathValues.SLURMDB_V0_0_39_CLUSTERS: SlurmdbV0039Clusters,
        PathValues.SLURMDB_V0_0_39_WCKEY_WCKEY: SlurmdbV0039WckeyWckey,
        PathValues.SLURMDB_V0_0_39_WCKEYS: SlurmdbV0039Wckeys,
        PathValues.SLURMDB_V0_0_39_ACCOUNT_ACCOUNT_NAME: SlurmdbV0039AccountAccountName,
        PathValues.SLURMDB_V0_0_39_ACCOUNTS: SlurmdbV0039Accounts,
        PathValues.SLURMDB_V0_0_39_JOBS: SlurmdbV0039Jobs,
        PathValues.SLURMDB_V0_0_39_DIAG: SlurmdbV0039Diag,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SLURM_V0_0_39_DIAG: SlurmV0039Diag,
        PathValues.SLURM_V0_0_39_LICENSES: SlurmV0039Licenses,
        PathValues.SLURM_V0_0_39_PING: SlurmV0039Ping,
        PathValues.SLURM_V0_0_39_JOBS: SlurmV0039Jobs,
        PathValues.SLURM_V0_0_39_JOB_JOB_ID: SlurmV0039JobJobId,
        PathValues.SLURM_V0_0_39_JOB_SUBMIT: SlurmV0039JobSubmit,
        PathValues.SLURM_V0_0_39_NODES: SlurmV0039Nodes,
        PathValues.SLURM_V0_0_39_NODE_NODE_NAME: SlurmV0039NodeNodeName,
        PathValues.SLURM_V0_0_39_PARTITIONS: SlurmV0039Partitions,
        PathValues.SLURM_V0_0_39_PARTITION_PARTITION_NAME: SlurmV0039PartitionPartitionName,
        PathValues.SLURM_V0_0_39_RESERVATIONS: SlurmV0039Reservations,
        PathValues.SLURM_V0_0_39_RESERVATION_RESERVATION_NAME: SlurmV0039ReservationReservationName,
        PathValues.OPENAPI_YAML: OpenapiYaml,
        PathValues.OPENAPI_JSON: OpenapiJson,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_V3: OpenapiV3,
        PathValues.SLURMDB_V0_0_39_JOB_JOB_ID: SlurmdbV0039JobJobId,
        PathValues.SLURMDB_V0_0_39_CONFIG: SlurmdbV0039Config,
        PathValues.SLURMDB_V0_0_39_TRES: SlurmdbV0039Tres,
        PathValues.SLURMDB_V0_0_39_QOS_QOS_NAME: SlurmdbV0039QosQosName,
        PathValues.SLURMDB_V0_0_39_QOS: SlurmdbV0039Qos,
        PathValues.SLURMDB_V0_0_39_ASSOCIATIONS: SlurmdbV0039Associations,
        PathValues.SLURMDB_V0_0_39_ASSOCIATION: SlurmdbV0039Association,
        PathValues.SLURMDB_V0_0_39_USER_USER_NAME: SlurmdbV0039UserUserName,
        PathValues.SLURMDB_V0_0_39_USERS: SlurmdbV0039Users,
        PathValues.SLURMDB_V0_0_39_CLUSTER_CLUSTER_NAME: SlurmdbV0039ClusterClusterName,
        PathValues.SLURMDB_V0_0_39_CLUSTERS: SlurmdbV0039Clusters,
        PathValues.SLURMDB_V0_0_39_WCKEY_WCKEY: SlurmdbV0039WckeyWckey,
        PathValues.SLURMDB_V0_0_39_WCKEYS: SlurmdbV0039Wckeys,
        PathValues.SLURMDB_V0_0_39_ACCOUNT_ACCOUNT_NAME: SlurmdbV0039AccountAccountName,
        PathValues.SLURMDB_V0_0_39_ACCOUNTS: SlurmdbV0039Accounts,
        PathValues.SLURMDB_V0_0_39_JOBS: SlurmdbV0039Jobs,
        PathValues.SLURMDB_V0_0_39_DIAG: SlurmdbV0039Diag,
    }
)
