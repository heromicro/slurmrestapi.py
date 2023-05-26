from slurmrestapi.paths.slurmdb_v0_0_38_association.get import ApiForget
from slurmrestapi.paths.slurmdb_v0_0_38_association.delete import ApiFordelete


class SlurmdbV0038Association(
    ApiForget,
    ApiFordelete,
):
    pass
