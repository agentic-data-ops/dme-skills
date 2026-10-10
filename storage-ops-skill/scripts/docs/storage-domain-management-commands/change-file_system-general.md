# change file_system general


##### Function

The **change file_system general** command is used to modify file system parameters such as the name, capacity, block size, and owning controller.

##### Format

**change file_system general** \[ file_system_id=? \| file_system_name=? \] { name=? \| capacity=? \| owner_controller=? \| io_priority=? \| capacity_threshold=? \| timing_snapshot_max_number=? \| snapshot_reserve=? \| split_speed=? \| alloc_type=? \| space_self_adjusting_mode=? \| autosize_enable=? \| auto_shrink_threshold_percent=? \| auto_grow_threshold_percent=? \| min_autosize=? \| max_autosize=? \| autosize_increment=? \| space_recycle_mode=? \| ssd_capacity_upper_limit_of_user_data=? \| initial_distribute_policy=? \| prefetch_policy=? \| long_filename_enabled=? \| security_style=? \[ prefetch_multiple=? \] \[ prefetch_value=? \] } \* \[ description=? \| clear_description=? \] \[ support_32bit_inode=? \] \[ unix_permissions=? \] \[ fs_layer_distribution_algorithm=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | New name of the file system. | The value consists of 1 to 255 ASCII characters including numbers, letters, underscores (_), hyphen (-) and dot (.).<br>To batch create file systems (when "number=?" is specified), the names will be automatically generated. A four-digit number starting from 0000 will be added to a specified name. For example, if the specified name is "FS", the names of the newly created file systems are "FS0000", "FS0001", and so on.<br> NOTE: The specified "name=?" cannot exceed 251 characters. |
| description | File system description. | The value contains 1 to 255 characters. |
| capacity=? | File system capacity. | The value can be "capacity+unit". The unit can be MB, GB, TB, or Blocks.<br>The value ranges from 1 GB to 32,768 TB.<br>One block equals 512 bytes. |
| file_system_id=? | File system ID. | The value is an integer between 0 and 65535. |
| file_system_name=? | Current name of the file system. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| owner_controller=? | Owning controller of the file system. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is in the format of "XA", "XB", "XC", or "XD", where "X" indicates an integer from 0 to 3, for example, "0A" or "1C". |
| io_priority=? | I/O priority of the file system. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "Low", "Middle", or "High", where: <br>"Low": low priority.<br>"Middle": medium priority.<br>"High": high priority. |
| block_size=? | Size of a file system block. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value can be "4KB", "8KB", "16KB", "32KB" or "64KB". The default value is "16KB". |
| application_scenario=? | File system application scenario. NOTE: This parameter is not supported in this version, and the execution result is invalid. | This parameter cannot be used together with "block_size".<br>The parameter value can be "database" or "virtual_machine". |
| capacity_threshold=? | Capacity alarm threshold of the file system. When the consumed capacity in the file system exceeds the threshold, alarms will be reported. | The value is a percentage (an integer).<br>The value ranges from 50 to 99. |
| timing_snapshot_max_number=? | Maximum number of timing snapshots. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value ranges from 1 to 2048. |
| snapshot_reserve=? | Proportion of the space reserved for snapshots. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is a percentage. The percentage must be an integer.<br>The value ranges from 0 to 50. |
| split_speed=? | Split speed. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "Low", "Medium", "High", or "Highest", where: <br>"Low": low speed.<br>"Medium": medium speed.<br>"High": high speed.<br>"Highest": highest speed.<br> The default value is "Medium". |
| space_self_adjusting_mode=? | Sets the automatic capacity adjustment mode. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "off", "grow", or "grow_shrink", where: <br>"off": disables the automatic capacity adjustment function.<br>"grow": enables the automatic capacity adjustment function. Only automatic expansion is supported.<br>"grow_shrink": enables the automatic capacity adjustment function. Automatic expansion and reduction are supported.<br> The default value is "off". |
| autosize_enable=? | Switch of automatic capacity adjustment. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"no": does not enable automatic capacity adjustment.<br>"yes": enables automatic capacity adjustment.<br> The default value is "yes". |
| auto_shrink_threshold_percent=? | Percentage threshold that triggers the automatic reduction. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is a percentage (an integer).<br>The value ranges from 1 to 99.<br> The default value is "50". |
| auto_grow_threshold_percent=? | Percentage threshold that triggers the automatic expansion. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is a percentage (an integer).<br>The value ranges from 1 to 99.<br> The default value is "85". |
| min_autosize=? | Lower limit of the automatic reduction. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "capacity+unit". The unit can be MB, GB, TB, or Blocks.<br>The value ranges from 1 GB to 16384 TB.<br>One block equals 512 bytes. |
| autosize_increment=? | Capacity change of a single expansion/reduction. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is "capacity+unit". The unit can be MB or GB.<br>The value ranges from 64 MB to 100 GB.<br> The default value is 1 GB. |
| max_autosize=? | Upper limit of the automatic expansion. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "capacity+unit". The unit can be MB, GB, TB, or Blocks.<br>The value ranges from 1 GB to 16384 TB.<br>One block equals 512 bytes. |
| space_recycle_mode=? | Capacity recycle mode. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "autosize_first" or "delete_snap_first", where: <br>"autosize_first": Automatic expansion is preferred.<br>"delete_snap_first": Automatic snapshot deletion is preferred.<br> The default value is "autosize_first". |
| alloc_type | File system type. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "thick" or "thin". |
| clear_description | Clears the description. | The value can be: "Enable": clears the description. |
| ssd_capacity_upper_limit_of_user_data | SSD capacity upper limit of user data. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "capacity+unit". The unit can be MB, GB, TB, or Blocks.<br>The value ranges from 1 GB to the total capacity of the file system.<br>One block equals 512 bytes. |
| initial_distribute_policy=? | Initial space allocation policy. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "automatic", "extreme_performance", "performance", or "capacity", where: <br>"automatic": The system allocates space to the file system based on the available space on each storage tier.<br>"extreme_performance": The space is first allocated from the high-performance tier.<br>"performance": The space is first allocated from the performance tier.<br>"capacity": The space is first allocated from the capacity tier. |
| long_filename_enabled=? | Whether to enable the long file name function. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: <br>"yes": enables the long file name function.<br>"no": disables the long file name function. |
| prefetch_policy | Cache prefetch policy. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "none", "constant", "variable", or "intelligent", where: <br>"none": non-prefetch.<br>"constant": constant prefetch.<br>"variable": variable prefetch.<br>"intelligent": intelligent prefetch.<br> The default value is "intelligent". |
| prefetch_value | Cache prefetch value. This parameter is unavailable when parameter "prefetch_policy=?" is set to "none". This parameter is mandatory when parameter "prefetch_policy=?" is set to "constant" or "intelligent". NOTE: This parameter is not supported by the current version. The execution result is invalid. | When the value of "prefetch_policy=?" is "constant", this parameter ranges from 0 to 1024, expressed in KB. When the value is "intelligent", this parameter ranges from 1024 to 16384, expressed in KB. The default value is 4096. |
| prefetch_multiple | Cache prefetch multiple. This parameter is required when "prefetch_policy=?" is set to "variable". NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value ranges from 0 to 1024. |
| security_style=? | Security style supported by a file system. | The value can be "NTFS", or "UNIX", where: <br>"NTFS": NTFS security style.<br>"UNIX": UNIX security style. |
| unix_permissions=? | UNIX permissions of the file system root directory. | The value consists of three digits, where: <br>The first digit refers to the permissions of the owner.<br>The second digit refers to the permissions of the user group to which the file belongs.<br>The last digit refers to the permissions of everyone else.<br> The digits are from 0 to 7, where: <br>"0": No permission.<br>"1": Execute permission.<br>"2": Write permission.<br>"3": Write and execute permissions.<br>"4": Read permission.<br>"5": Read and execute permissions.<br>"6": Read and write permissions.<br>"7": All permissions (read, write, and execute). |
| fs_layer_distribution_algorithm=? | Data distribution algorithm of the file system. | "Performance Mode": performance mode. Directories and files are allocated to the access controller preferentially, to improve access performance of directories and files.<br>"Capacity Balance Mode": capacity balancing mode. Directories and files are evenly allocated to each controller by capacity.<br>"Directory Balance Mode": directory balancing mode. Directories are evenly allocated to each controller by quantity.<br>"Directory Shuffle Mode": directory polling mode. Directories are allocated to each controller based on the creation sequence. |

##### Usage Guidelines

Before running this command, ensure that the selected file system is exactly the one you want to modify its settings.

##### Example

Modify the file system configuration as follows: Capacity alarm threshold: 50% File system name: fs003 Owning controller: 0B I/O priority: medium Reserved space for snapshots: 20% Maximum number of timing snapshots: 20.

```text
admin:/>change file_system general file_system_id=0 capacity_threshold=50 name=fs003 owner_controller=0B io_priority=Middle snapshot_reserve=20 timing_snapshot_max_number=20
WARNING: You are about to change the priority or the cache prefetch policy of file system.
This operation may affect the file system performance.
Suggestion:Before performing this operation, ensure that the preceding risk is acceptable and the correct file system is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the prefetch policy of file system "1" to "none".

```text
admin:/>change file_system general file_system_id=1 prefetch_policy=none
WARNING: You are about to change the priority or the cache prefetch policy of file system. This operation may affect the file system performance.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable and the correct file system is selected.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the security mode of file system "1" to "NTFS".

```text
admin:/>change file_system general file_system_id=1 security_style=NTFS
WARNING: You are about to set the file system security style to NTFS. This operation may affect file system operations.
Suggestion: If NTFS is selected, you are advised to set the mapping mode to support only user mapping in the current system and configure the default Windows user in the NFS service. The Windows user must be an existing local resource user or AD domain user.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the security mode of file system "1" to "UNIX".

```text
admin:/>change file_system general file_system_id=1 security_style=UNIX
WARNING: You are about to set the file system security style to UNIX. This operation may affect file system operations.
Suggestion: If UNIX is selected, you are advised to set the mapping mode to support only user mapping in the current system and configure the default UNIX user in the CIFS service. The UNIX user must be an existing local resource user or NIS or LDAP domain user.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the switch of supporting 32-bit inodes of file system "1" to "yes".

```text
developer:/>change file_system general file_system_id=1 support_32bit_inode=yes
DANGER: You are about to enable/disable the support for 32-bit inodes. After this operation, the client cache will be invalid. Suggestion: Before performing this operation, ensure that the host is not reading data from or writing data to the file system, and unmount the file system share. After this operation is complete, mount the share again.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
