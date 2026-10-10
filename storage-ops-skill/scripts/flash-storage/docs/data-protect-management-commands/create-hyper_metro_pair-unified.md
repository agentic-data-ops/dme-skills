# create hyper_metro_pair unified


##### Function

The **create hyper_metro_pair unified** command is used to create a HyperMetro pair.

##### Format

**create hyper_metro_pair unified** domain_id=? lun_id=? secondary_lun_id=? \[ no_synchronize=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \| bandwidth=? \| isolation_switch=? \| isolation_threshold=? \]

**create hyper_metro_pair unified** domain_id=? lun_id_list=? secondary_lun_id_list=? \[ no_synchronize=? \] \[ recovery_policy=? \] \[ synchronization_rate=? \| bandwidth=? \| isolation_switch=? \| isolation_threshold=? \]

**create hyper_metro_pair unified** vstore_pair_id=? file_system_id=? secondary_file_system_id=? \[ synchronization_rate=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id=? | ID of the HyperMetro domain. | To obtain the value, run the "show hyper_metro_domain general" command without parameters. |
| lun_id=? | ID of the primary LUN. If "lun_id" is specified, "secondary_lun_id" must be specified. | To obtain the value, run the "show lun general" command without parameters. |
| secondary_lun_id=? | ID of the secondary LUN. | To obtain the value, run the "show remote_lun general array_type=replication remote_device_id=?" command. |
| lun_id_list=? | Primary LUN ID list. If "lun_id_list" is specified, "secondary_lun_id_list" must be specified. | You can run the "show lun general" command to obtain the IDs.<br>IDs of multiple LUNs are separated by commas (,), or ID ranges are represented by hyphens (-).<br>A maximum of 100 IDs can be entered. |
| secondary_lun_id_list=? | Indicates the secondary LUN ID list. | You can run the "show remote_lun general array_type=replication remote_device_id=?" command to obtain the IDs.<br>IDs of multiple LUNs are separated by commas (,), or ID ranges are represented by hyphens (-).<br>A maximum of 100 IDs can be entered. |
| no_synchronize=? | Whether synchronization is required after the pair is created (valid for LUN only). | The value can be "yes" or "no", where: <br>"yes": Synchronization is not required.<br>"no": Synchronization is required.<br> The default value is "no". |
| recovery_policy=? | Recovery policy. | The value can be "automatic" or "manual", where: <br>"automatic": automatic recovery policy. Data will be automatically synchronized after faults are rectified.<br>"manual": manual recovery policy.<br> Data needs to be manually synchronized after faults are rectified. The default value is "automatic". |
| synchronization_rate=? | Synchronization rate. | The value can be "Low", "Middle", "High", or "Highest", where: <br>"Low": low rate.<br>"Middle": medium rate.<br>"High": high rate.<br>"Highest": the highest rate.<br> The default value is "Middle". |
| bandwidth=? | Bandwidth. | The value ranges from 1 to 1024, expressed in MB/s. |
| isolation_threshold=? | Isolation threshold. | The value ranges from 10 ms to 30s. The default value is 200 ms. |
| isolation_switch=? | Isolation switch. | The value can be "open" or "close", where: <br>"open": ensures service continuity preferentially and applies to scenarios where host services require low storage latency. When the average write latency difference between local and remote resources of a HyperMetro pair is greater than the disconnection threshold, the system automatically disconnects the HyperMetro pair and the resource with lower write latency continues providing services.<br>"close": ensures service data reliability preferentially and applies to scenarios that have high requirements for data protection. Data on local and remote resources is consistent in real time. |
| file_system_id=? | ID of the primary file system. | To obtain the value, run the "show file_system general" command. |
| vstore_pair_id=? | vStore pair ID. | To obtain the value, run the "show vstore_pair general" command without parameters. |
| secondary_file_system_id=? | ID of the secondary file system. | You can run the "show file_system general" command in the remote cluster to obtain the value. |

##### Usage Guidelines

None

##### Example

Create a HyperMetro pair.

```text

admin:/>create hyper_metro_pair unified domain_id=fce33cafb1b80100 lun_id=0 secondary_lun_id=0
DANGER: You are about to create a HyperMetro pair. This operation will cause the data on the local resource to overwrite that on the remote resource. If the host type is Windows, enable automatic LUN SN synchronization on both storage systems before configuring HyperMetro. Otherwise, one HyperMetro LUN may be identified as two disks on the host application side. For details, see "What Can I Do If the Host Identifies One HyperMetro LUN as Two Disks?" in the "HyperMetro Feature Guide for Block" of the desired product model.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent data overwriting.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

Create a HyperMetro pair.

```text
admin:/>create hyper_metro_pair unified domain_id=1 lun_id=1 secondary_lun_id=2 synchronization_rate=Highest
DANGER: You are about to create a HyperMetro pair. This operation will cause the data on the local resource to overwrite that on the remote resource. If you perform synchronization at the "Highest" speed, check the performance of remote devices and whether the link bandwidth between local and remote arrays is sufficient. If you select the "Highest" synchronization speed, the host latency may increase, and HyperMetro pairs will be disconnected during synchronization. You are advised to select the "Highest" synchronization speed only during off-peak hours. If the host type is Windows, enable automatic LUN SN synchronization on both storage systems before configuring HyperMetro. Otherwise, one HyperMetro LUN may be identified as two disks on the host application side. For details, see "What Can I Do If the Host Identifies One HyperMetro LUN as Two Disks?" in the "HyperMetro Feature Guide for Block" of the desired product model.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent data overwriting.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a HyperMetro pair.

```text
admin:/>create hyper_metro_pair unified domain_id=1 lun_id=1 secondary_lun_id=2 no_synchronize=yes
DANGER: You are about to create a HyperMetro pair. This operation will cause the data on the local resource to overwrite that on the remote resource.
If you do not perform initial synchronization, ensure that the local and remote resources have the same data. Otherwise, data inconsistency occurs, resulting in service access exceptions. If the host type is Windows, enable automatic LUN SN synchronization on both storage systems before configuring HyperMetro. Otherwise, one HyperMetro LUN may be identified as two disks on the host application side. For details, see "What Can I Do If the Host Identifies One HyperMetro LUN as Two Disks?" in the "HyperMetro Feature Guide for Block" of the desired product model.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent data overwriting.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

Create a HyperMetro pair.

```text
admin:/>create hyper_metro_pair unified domain_id=1 lun_id=1 secondary_lun_id=2 synchronization_rate=Highest no_synchronize=yes
DANGER: You are about to create a HyperMetro pair. This operation will cause the data on the local resource to overwrite that on the remote resource. If you do not perform initial synchronization, ensure that the local and remote resources have the same data. Otherwise, data inconsistency occurs, resulting in service access exceptions. If you perform synchronization at the "Highest" speed, check the performance of remote devices and whether the link bandwidth between local and remote arrays is sufficient. If you select the "Highest" synchronization speed, the host latency may increase, and HyperMetro pairs will be disconnected during synchronization. You are advised to select the "Highest" synchronization speed only during off-peak hours. If the host type is Windows, enable automatic LUN SN synchronization on both storage systems before configuring HyperMetro. Otherwise, one HyperMetro LUN may be identified as two disks on the host application side. For details, see "What Can I Do If the Host Identifies One HyperMetro LUN as Two Disks?" in the "HyperMetro Feature Guide for Block" of the desired product model.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent data overwriting.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

Create multiple HyperMetro pairs.

```text
admin:/>create hyper_metro_pair unified domain_id=fce33cafb1b80100 lun_id_list=0,1,2,3 secondary_lun_id_list=7,4,6,9
DANGER: You are about to create a HyperMetro pair. This operation will cause the data on the local resource to overwrite that on the remote resource. If the host type is Windows, enable automatic LUN SN synchronization on both storage systems before configuring HyperMetro. Otherwise, one HyperMetro LUN may be identified as two disks on the host application side. For details, see "What Can I Do If the Host Identifies One HyperMetro LUN as Two Disks?" in the "HyperMetro Feature Guide for Block" of the desired product model.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent data overwriting.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a file system HyperMetro pair.

```text
admin:/>create hyper_metro_pair unified vstore_pair_id=1 file_system_id=1 secondary_file_system_id=1
DANGER: You are about to create a HyperMetro pair. This operation will cause the local resource data to overwrite the remote resource data.
Suggestion: Before performing this operation, ensure that the operation and parameters are correct to prevent data from being overwritten.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create multiple HyperMetro pairs.

```text
admin:/>create hyper_metro_pair unified domain_id=fce33cafb1b80100 lun_id_list=0-3 secondary_lun_id_list=7-10
DANGER: You are about to create a HyperMetro pair. This operation will cause the data on the local resource to overwrite that on the remote resource. If the host type is Windows, enable automatic LUN SN synchronization on both storage systems before configuring HyperMetro. Otherwise, one HyperMetro LUN may be identified as two disks on the host application side. For details, see "What Can I Do If the Host Identifies One HyperMetro LUN as Two Disks?" in the "HyperMetro Feature Guide for Block" of the desired product model.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent data overwriting.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
