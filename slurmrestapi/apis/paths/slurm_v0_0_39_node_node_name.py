from slurmrestapi.paths.slurm_v0_0_39_node_node_name.get import ApiForget
from slurmrestapi.paths.slurm_v0_0_39_node_node_name.post import ApiForpost
from slurmrestapi.paths.slurm_v0_0_39_node_node_name.delete import ApiFordelete


class SlurmV0039NodeNodeName(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
