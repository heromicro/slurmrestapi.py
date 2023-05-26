from slurmrestapi.paths.slurmdb_v0_0_39_association.get import ApiForget
from slurmrestapi.paths.slurmdb_v0_0_39_association.delete import ApiFordelete


class SlurmdbV0039Association(
    ApiForget,
    ApiFordelete,
):
    pass
