# coding: utf-8

"""
    Slurm Rest API

    API to access and control Slurm.  # noqa: E501

    The version of the OpenAPI document: 0.0.38
    Contact: sales@schedmd.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from slurmrestapi import schemas  # noqa: F401


class V0038Node(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            architecture = schemas.StrSchema
            burstbuffer_network_address = schemas.StrSchema
            boards = schemas.IntSchema
            boot_time = schemas.Int64Schema
            cores = schemas.IntSchema
            cpu_binding = schemas.IntSchema
            cpu_load = schemas.Int64Schema
            free_memory = schemas.IntSchema
            cpus = schemas.IntSchema
            features = schemas.StrSchema
            active_features = schemas.StrSchema
            gres = schemas.StrSchema
            gres_drained = schemas.StrSchema
            gres_used = schemas.StrSchema
            mcs_label = schemas.StrSchema
            name = schemas.StrSchema
            next_state_after_reboot = schemas.StrSchema
            
            
            class next_state_after_reboot_flags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'next_state_after_reboot_flags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            address = schemas.StrSchema
            hostname = schemas.StrSchema
            state = schemas.StrSchema
            
            
            class state_flags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'state_flags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            operating_system = schemas.StrSchema
            owner = schemas.StrSchema
            
            
            class partitions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'partitions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            port = schemas.IntSchema
            real_memory = schemas.IntSchema
            reason = schemas.StrSchema
            reason_changed_at = schemas.IntSchema
            reason_set_by_user = schemas.StrSchema
            slurmd_start_time = schemas.Int64Schema
            sockets = schemas.IntSchema
            threads = schemas.IntSchema
            temporary_disk = schemas.IntSchema
            weight = schemas.IntSchema
            tres = schemas.StrSchema
            tres_used = schemas.StrSchema
            tres_weighted = schemas.Float64Schema
            slurmd_version = schemas.StrSchema
            alloc_cpus = schemas.Int64Schema
            idle_cpus = schemas.Int64Schema
            alloc_memory = schemas.Int64Schema
            __annotations__ = {
                "architecture": architecture,
                "burstbuffer_network_address": burstbuffer_network_address,
                "boards": boards,
                "boot_time": boot_time,
                "cores": cores,
                "cpu_binding": cpu_binding,
                "cpu_load": cpu_load,
                "free_memory": free_memory,
                "cpus": cpus,
                "features": features,
                "active_features": active_features,
                "gres": gres,
                "gres_drained": gres_drained,
                "gres_used": gres_used,
                "mcs_label": mcs_label,
                "name": name,
                "next_state_after_reboot": next_state_after_reboot,
                "next_state_after_reboot_flags": next_state_after_reboot_flags,
                "address": address,
                "hostname": hostname,
                "state": state,
                "state_flags": state_flags,
                "operating_system": operating_system,
                "owner": owner,
                "partitions": partitions,
                "port": port,
                "real_memory": real_memory,
                "reason": reason,
                "reason_changed_at": reason_changed_at,
                "reason_set_by_user": reason_set_by_user,
                "slurmd_start_time": slurmd_start_time,
                "sockets": sockets,
                "threads": threads,
                "temporary_disk": temporary_disk,
                "weight": weight,
                "tres": tres,
                "tres_used": tres_used,
                "tres_weighted": tres_weighted,
                "slurmd_version": slurmd_version,
                "alloc_cpus": alloc_cpus,
                "idle_cpus": idle_cpus,
                "alloc_memory": alloc_memory,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["architecture"]) -> MetaOapg.properties.architecture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["burstbuffer_network_address"]) -> MetaOapg.properties.burstbuffer_network_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boards"]) -> MetaOapg.properties.boards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boot_time"]) -> MetaOapg.properties.boot_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cores"]) -> MetaOapg.properties.cores: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_binding"]) -> MetaOapg.properties.cpu_binding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_load"]) -> MetaOapg.properties.cpu_load: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["free_memory"]) -> MetaOapg.properties.free_memory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpus"]) -> MetaOapg.properties.cpus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["features"]) -> MetaOapg.properties.features: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_features"]) -> MetaOapg.properties.active_features: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gres"]) -> MetaOapg.properties.gres: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gres_drained"]) -> MetaOapg.properties.gres_drained: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gres_used"]) -> MetaOapg.properties.gres_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mcs_label"]) -> MetaOapg.properties.mcs_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_state_after_reboot"]) -> MetaOapg.properties.next_state_after_reboot: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_state_after_reboot_flags"]) -> MetaOapg.properties.next_state_after_reboot_flags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state_flags"]) -> MetaOapg.properties.state_flags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operating_system"]) -> MetaOapg.properties.operating_system: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partitions"]) -> MetaOapg.properties.partitions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["real_memory"]) -> MetaOapg.properties.real_memory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason_changed_at"]) -> MetaOapg.properties.reason_changed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason_set_by_user"]) -> MetaOapg.properties.reason_set_by_user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slurmd_start_time"]) -> MetaOapg.properties.slurmd_start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sockets"]) -> MetaOapg.properties.sockets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["threads"]) -> MetaOapg.properties.threads: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temporary_disk"]) -> MetaOapg.properties.temporary_disk: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weight"]) -> MetaOapg.properties.weight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tres"]) -> MetaOapg.properties.tres: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tres_used"]) -> MetaOapg.properties.tres_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tres_weighted"]) -> MetaOapg.properties.tres_weighted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slurmd_version"]) -> MetaOapg.properties.slurmd_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alloc_cpus"]) -> MetaOapg.properties.alloc_cpus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idle_cpus"]) -> MetaOapg.properties.idle_cpus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alloc_memory"]) -> MetaOapg.properties.alloc_memory: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["architecture", "burstbuffer_network_address", "boards", "boot_time", "cores", "cpu_binding", "cpu_load", "free_memory", "cpus", "features", "active_features", "gres", "gres_drained", "gres_used", "mcs_label", "name", "next_state_after_reboot", "next_state_after_reboot_flags", "address", "hostname", "state", "state_flags", "operating_system", "owner", "partitions", "port", "real_memory", "reason", "reason_changed_at", "reason_set_by_user", "slurmd_start_time", "sockets", "threads", "temporary_disk", "weight", "tres", "tres_used", "tres_weighted", "slurmd_version", "alloc_cpus", "idle_cpus", "alloc_memory", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["architecture"]) -> typing.Union[MetaOapg.properties.architecture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["burstbuffer_network_address"]) -> typing.Union[MetaOapg.properties.burstbuffer_network_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["boards"]) -> typing.Union[MetaOapg.properties.boards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["boot_time"]) -> typing.Union[MetaOapg.properties.boot_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cores"]) -> typing.Union[MetaOapg.properties.cores, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_binding"]) -> typing.Union[MetaOapg.properties.cpu_binding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_load"]) -> typing.Union[MetaOapg.properties.cpu_load, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["free_memory"]) -> typing.Union[MetaOapg.properties.free_memory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpus"]) -> typing.Union[MetaOapg.properties.cpus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["features"]) -> typing.Union[MetaOapg.properties.features, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_features"]) -> typing.Union[MetaOapg.properties.active_features, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gres"]) -> typing.Union[MetaOapg.properties.gres, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gres_drained"]) -> typing.Union[MetaOapg.properties.gres_drained, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gres_used"]) -> typing.Union[MetaOapg.properties.gres_used, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mcs_label"]) -> typing.Union[MetaOapg.properties.mcs_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_state_after_reboot"]) -> typing.Union[MetaOapg.properties.next_state_after_reboot, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_state_after_reboot_flags"]) -> typing.Union[MetaOapg.properties.next_state_after_reboot_flags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state_flags"]) -> typing.Union[MetaOapg.properties.state_flags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operating_system"]) -> typing.Union[MetaOapg.properties.operating_system, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partitions"]) -> typing.Union[MetaOapg.properties.partitions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["real_memory"]) -> typing.Union[MetaOapg.properties.real_memory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason_changed_at"]) -> typing.Union[MetaOapg.properties.reason_changed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason_set_by_user"]) -> typing.Union[MetaOapg.properties.reason_set_by_user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slurmd_start_time"]) -> typing.Union[MetaOapg.properties.slurmd_start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sockets"]) -> typing.Union[MetaOapg.properties.sockets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["threads"]) -> typing.Union[MetaOapg.properties.threads, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temporary_disk"]) -> typing.Union[MetaOapg.properties.temporary_disk, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weight"]) -> typing.Union[MetaOapg.properties.weight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tres"]) -> typing.Union[MetaOapg.properties.tres, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tres_used"]) -> typing.Union[MetaOapg.properties.tres_used, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tres_weighted"]) -> typing.Union[MetaOapg.properties.tres_weighted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slurmd_version"]) -> typing.Union[MetaOapg.properties.slurmd_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alloc_cpus"]) -> typing.Union[MetaOapg.properties.alloc_cpus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idle_cpus"]) -> typing.Union[MetaOapg.properties.idle_cpus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alloc_memory"]) -> typing.Union[MetaOapg.properties.alloc_memory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["architecture", "burstbuffer_network_address", "boards", "boot_time", "cores", "cpu_binding", "cpu_load", "free_memory", "cpus", "features", "active_features", "gres", "gres_drained", "gres_used", "mcs_label", "name", "next_state_after_reboot", "next_state_after_reboot_flags", "address", "hostname", "state", "state_flags", "operating_system", "owner", "partitions", "port", "real_memory", "reason", "reason_changed_at", "reason_set_by_user", "slurmd_start_time", "sockets", "threads", "temporary_disk", "weight", "tres", "tres_used", "tres_weighted", "slurmd_version", "alloc_cpus", "idle_cpus", "alloc_memory", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        architecture: typing.Union[MetaOapg.properties.architecture, str, schemas.Unset] = schemas.unset,
        burstbuffer_network_address: typing.Union[MetaOapg.properties.burstbuffer_network_address, str, schemas.Unset] = schemas.unset,
        boards: typing.Union[MetaOapg.properties.boards, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        boot_time: typing.Union[MetaOapg.properties.boot_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cores: typing.Union[MetaOapg.properties.cores, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cpu_binding: typing.Union[MetaOapg.properties.cpu_binding, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cpu_load: typing.Union[MetaOapg.properties.cpu_load, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        free_memory: typing.Union[MetaOapg.properties.free_memory, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cpus: typing.Union[MetaOapg.properties.cpus, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        features: typing.Union[MetaOapg.properties.features, str, schemas.Unset] = schemas.unset,
        active_features: typing.Union[MetaOapg.properties.active_features, str, schemas.Unset] = schemas.unset,
        gres: typing.Union[MetaOapg.properties.gres, str, schemas.Unset] = schemas.unset,
        gres_drained: typing.Union[MetaOapg.properties.gres_drained, str, schemas.Unset] = schemas.unset,
        gres_used: typing.Union[MetaOapg.properties.gres_used, str, schemas.Unset] = schemas.unset,
        mcs_label: typing.Union[MetaOapg.properties.mcs_label, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        next_state_after_reboot: typing.Union[MetaOapg.properties.next_state_after_reboot, str, schemas.Unset] = schemas.unset,
        next_state_after_reboot_flags: typing.Union[MetaOapg.properties.next_state_after_reboot_flags, list, tuple, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        state_flags: typing.Union[MetaOapg.properties.state_flags, list, tuple, schemas.Unset] = schemas.unset,
        operating_system: typing.Union[MetaOapg.properties.operating_system, str, schemas.Unset] = schemas.unset,
        owner: typing.Union[MetaOapg.properties.owner, str, schemas.Unset] = schemas.unset,
        partitions: typing.Union[MetaOapg.properties.partitions, list, tuple, schemas.Unset] = schemas.unset,
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        real_memory: typing.Union[MetaOapg.properties.real_memory, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        reason_changed_at: typing.Union[MetaOapg.properties.reason_changed_at, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reason_set_by_user: typing.Union[MetaOapg.properties.reason_set_by_user, str, schemas.Unset] = schemas.unset,
        slurmd_start_time: typing.Union[MetaOapg.properties.slurmd_start_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sockets: typing.Union[MetaOapg.properties.sockets, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        threads: typing.Union[MetaOapg.properties.threads, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        temporary_disk: typing.Union[MetaOapg.properties.temporary_disk, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        weight: typing.Union[MetaOapg.properties.weight, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tres: typing.Union[MetaOapg.properties.tres, str, schemas.Unset] = schemas.unset,
        tres_used: typing.Union[MetaOapg.properties.tres_used, str, schemas.Unset] = schemas.unset,
        tres_weighted: typing.Union[MetaOapg.properties.tres_weighted, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        slurmd_version: typing.Union[MetaOapg.properties.slurmd_version, str, schemas.Unset] = schemas.unset,
        alloc_cpus: typing.Union[MetaOapg.properties.alloc_cpus, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        idle_cpus: typing.Union[MetaOapg.properties.idle_cpus, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        alloc_memory: typing.Union[MetaOapg.properties.alloc_memory, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V0038Node':
        return super().__new__(
            cls,
            *_args,
            architecture=architecture,
            burstbuffer_network_address=burstbuffer_network_address,
            boards=boards,
            boot_time=boot_time,
            cores=cores,
            cpu_binding=cpu_binding,
            cpu_load=cpu_load,
            free_memory=free_memory,
            cpus=cpus,
            features=features,
            active_features=active_features,
            gres=gres,
            gres_drained=gres_drained,
            gres_used=gres_used,
            mcs_label=mcs_label,
            name=name,
            next_state_after_reboot=next_state_after_reboot,
            next_state_after_reboot_flags=next_state_after_reboot_flags,
            address=address,
            hostname=hostname,
            state=state,
            state_flags=state_flags,
            operating_system=operating_system,
            owner=owner,
            partitions=partitions,
            port=port,
            real_memory=real_memory,
            reason=reason,
            reason_changed_at=reason_changed_at,
            reason_set_by_user=reason_set_by_user,
            slurmd_start_time=slurmd_start_time,
            sockets=sockets,
            threads=threads,
            temporary_disk=temporary_disk,
            weight=weight,
            tres=tres,
            tres_used=tres_used,
            tres_weighted=tres_weighted,
            slurmd_version=slurmd_version,
            alloc_cpus=alloc_cpus,
            idle_cpus=idle_cpus,
            alloc_memory=alloc_memory,
            _configuration=_configuration,
            **kwargs,
        )
