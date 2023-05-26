from slurmrestapi.paths.slurmdb_v0_0_37_association.get import ApiForget
from slurmrestapi.paths.slurmdb_v0_0_37_association.delete import ApiFordelete


class SlurmdbV0037Association(
    ApiForget,
    ApiFordelete,
):
    pass
