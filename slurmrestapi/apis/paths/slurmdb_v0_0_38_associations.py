from slurmrestapi.paths.slurmdb_v0_0_38_associations.get import ApiForget
from slurmrestapi.paths.slurmdb_v0_0_38_associations.post import ApiForpost
from slurmrestapi.paths.slurmdb_v0_0_38_associations.delete import ApiFordelete


class SlurmdbV0038Associations(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
