# slurmrestapi.model.v0038_job_properties.V0038JobProperties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[environment](#environment)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Dictionary of environment entries. | 
**account** | str,  | str,  | Charge resources used by this job to specified account. | [optional] 
**account_gather_frequency** | str,  | str,  | Define the job accounting and profiling sampling intervals. | [optional] 
**[argv](#argv)** | list, tuple,  | tuple,  | Arguments to the script. | [optional] 
**array** | str,  | str,  | Submit a job array, multiple jobs to be executed with identical parameters. The indexes specification identifies what array index values should be used. | [optional] 
**batch_features** | str,  | str,  | features required for batch script&#x27;s node | [optional] 
**begin_time** | decimal.Decimal, int,  | decimal.Decimal,  | Submit the batch script to the Slurm controller immediately, like normal, but tell the controller to defer the allocation of the job until the specified time. | [optional] value must be a 64 bit integer
**burst_buffer** | str,  | str,  | Burst buffer specification. | [optional] 
**cluster_constraint** | str,  | str,  | Specifies features that a federated cluster must have to have a sibling job submitted to it. | [optional] 
**comment** | str,  | str,  | An arbitrary comment. | [optional] 
**constraints** | str,  | str,  | node features required by job. | [optional] 
**container** | str,  | str,  | absolute path to OCI container bundle | [optional] 
**core_specification** | decimal.Decimal, int,  | decimal.Decimal,  | Count of specialized threads per node reserved by the job for system operations and not used by the application. | [optional] 
**cores_per_socket** | decimal.Decimal, int,  | decimal.Decimal,  | Restrict node selection to nodes with at least the specified number of cores per socket. | [optional] 
**cpu_binding** | str,  | str,  | Cpu binding | [optional] 
**cpu_binding_hint** | str,  | str,  | Cpu binding hint | [optional] 
**cpu_frequency** | str,  | str,  | Request that job steps initiated by srun commands inside this sbatch script be run at some requested frequency if possible, on the CPUs selected for the step on the compute node(s). | [optional] 
**cpus_per_gpu** | str,  | str,  | Number of CPUs requested per allocated GPU. | [optional] 
**cpus_per_task** | decimal.Decimal, int,  | decimal.Decimal,  | Advise the Slurm controller that ensuing job steps will require ncpus number of processors per task. | [optional] 
**current_working_directory** | str,  | str,  | Instruct Slurm to connect the batch script&#x27;s standard output directly to the file name. | [optional] 
**deadline** | str,  | str,  | Remove the job if no ending is possible before this deadline (start &gt; (deadline - time[-min])). | [optional] 
**delay_boot** | decimal.Decimal, int,  | decimal.Decimal,  | Do not reboot nodes in order to satisfied this job&#x27;s feature specification if the job has been eligible to run for less than this time period. | [optional] 
**dependency** | str,  | str,  | Defer the start of this job until the specified dependencies have been satisfied completed. | [optional] 
**distribution** | str,  | str,  | Specify alternate distribution methods for remote processes. | [optional] 
**exclusive** | str,  | str,  | The job allocation can share nodes just other users with the \&quot;user\&quot; option or with the \&quot;mcs\&quot; option). | [optional] must be one of ["user", "mcs", "true", "false", ] 
**get_user_environment** | bool,  | BoolClass,  | Load new login environment for user on job node. | [optional] 
**gres** | str,  | str,  | Specifies a comma delimited list of generic consumable resources. | [optional] 
**gres_flags** | str,  | str,  | Specify generic resource task binding options. | [optional] must be one of ["disable-binding", "enforce-binding", ] 
**gpu_binding** | str,  | str,  | Requested binding of tasks to GPU. | [optional] 
**gpu_frequency** | str,  | str,  | Requested GPU frequency. | [optional] 
**gpus** | str,  | str,  | GPUs per job. | [optional] 
**gpus_per_node** | str,  | str,  | GPUs per node. | [optional] 
**gpus_per_socket** | str,  | str,  | GPUs per socket. | [optional] 
**gpus_per_task** | str,  | str,  | GPUs per task. | [optional] 
**hold** | bool,  | BoolClass,  | Specify the job is to be submitted in a held state (priority of zero). | [optional] 
**kill_on_invalid_dependency** | bool,  | BoolClass,  | If a job has an invalid dependency, then Slurm is to terminate it. | [optional] 
**licenses** | str,  | str,  | Specification of licenses (or other resources available on all nodes of the cluster) which must be allocated to this job. | [optional] 
**mail_type** | str,  | str,  | Notify user by email when certain event types occur. | [optional] 
**mail_user** | str,  | str,  | User to receive email notification of state changes as defined by mail_type. | [optional] 
**mcs_label** | str,  | str,  | This parameter is a group among the groups of the user. | [optional] 
**memory_binding** | str,  | str,  | Bind tasks to memory. | [optional] 
**memory_per_cpu** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum real memory per cpu (MB). | [optional] 
**memory_per_gpu** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum memory required per allocated GPU. | [optional] 
**memory_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum real memory per node (MB). | [optional] 
**minimum_cpus_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum number of CPUs per node. | [optional] 
**minimum_nodes** | bool,  | BoolClass,  | If a range of node counts is given, prefer the smaller count. | [optional] 
**name** | str,  | str,  | Specify a name for the job allocation. | [optional] 
**nice** | decimal.Decimal, int,  | decimal.Decimal,  | Run the job with an adjusted scheduling priority within Slurm. | [optional] 
**no_kill** | bool,  | BoolClass,  | Do not automatically terminate a job if one of the nodes it has been allocated fails. | [optional] 
**[nodes](#nodes)** | list, tuple,  | tuple,  | Request that a minimum of minnodes nodes and a maximum node count. | [optional] 
**open_mode** | str,  | str,  | Open the output and error files using append or truncate mode as specified. | [optional] must be one of ["append", "truncate", ] if omitted the server will use the default value of "append"
**oversubscribe** | bool,  | BoolClass,  | The job allocation can over-subscribe resources with other running jobs. | [optional] if omitted the server will use the default value of False
**partition** | str,  | str,  | Request a specific partition for the resource allocation. | [optional] 
**prefer** | str,  | str,  | Comma delimited list of features for scheduler to prefer but not a strict requirement like a constraint. Value can be used for job submission but is only displayed for PENDING jobs. | [optional] 
**priority** | str,  | str,  | Request a specific job priority. | [optional] 
**qos** | str,  | str,  | Request a quality of service for the job. | [optional] 
**requeue** | bool,  | BoolClass,  | Specifies that the batch job should eligible to being requeue. | [optional] 
**reservation** | str,  | str,  | Allocate resources for the job from the named reservation. | [optional] 
**signal** | str,  | str,  | When a job is within sig_time seconds of its end time, send it the signal sig_num. | [optional] 
**sockets_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | Restrict node selection to nodes with at least the specified number of sockets. | [optional] 
**spread_job** | bool,  | BoolClass,  | Spread the job allocation over as many nodes as possible and attempt to evenly distribute tasks across the allocated nodes. | [optional] 
**standard_error** | str,  | str,  | Instruct Slurm to connect the batch script&#x27;s standard error directly to the file name. | [optional] 
**standard_input** | str,  | str,  | Instruct Slurm to connect the batch script&#x27;s standard input directly to the file name specified. | [optional] 
**standard_output** | str,  | str,  | Instruct Slurm to connect the batch script&#x27;s standard output directly to the file name. | [optional] 
**tasks** | decimal.Decimal, int,  | decimal.Decimal,  | Advises the Slurm controller that job steps run within the allocation will launch a maximum of number tasks and to provide for sufficient resources. | [optional] 
**tasks_per_core** | decimal.Decimal, int,  | decimal.Decimal,  | Request the maximum ntasks be invoked on each core. | [optional] 
**tasks_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | Request the maximum ntasks be invoked on each node. | [optional] 
**tasks_per_socket** | decimal.Decimal, int,  | decimal.Decimal,  | Request the maximum ntasks be invoked on each socket. | [optional] 
**thread_specification** | decimal.Decimal, int,  | decimal.Decimal,  | Count of specialized threads per node reserved by the job for system operations and not used by the application. | [optional] 
**threads_per_core** | decimal.Decimal, int,  | decimal.Decimal,  | Restrict node selection to nodes with at least the specified number of threads per core. | [optional] 
**time_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Step time limit in minutes. | [optional] 
**time_minimum** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum run time in minutes. | [optional] 
**wait_all_nodes** | bool,  | BoolClass,  | Do not begin execution until all nodes are ready for use. | [optional] 
**wckey** | str,  | str,  | Specify wckey to be used with job. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# environment

Dictionary of environment entries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Dictionary of environment entries. | 

# argv

Arguments to the script.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Arguments to the script. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# nodes

Request that a minimum of minnodes nodes and a maximum node count.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Request that a minimum of minnodes nodes and a maximum node count. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

