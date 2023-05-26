from slurmrestapi.paths.slurmdb_v0_0_39_associations.get import ApiForget
from slurmrestapi.paths.slurmdb_v0_0_39_associations.post import ApiForpost
from slurmrestapi.paths.slurmdb_v0_0_39_associations.delete import ApiFordelete


class SlurmdbV0039Associations(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
