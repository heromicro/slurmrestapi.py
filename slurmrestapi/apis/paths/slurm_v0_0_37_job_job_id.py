from slurmrestapi.paths.slurm_v0_0_37_job_job_id.get import ApiForget
from slurmrestapi.paths.slurm_v0_0_37_job_job_id.post import ApiForpost
from slurmrestapi.paths.slurm_v0_0_37_job_job_id.delete import ApiFordelete


class SlurmV0037JobJobId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
