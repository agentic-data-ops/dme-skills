# change service nfs_config


##### Function

The **change service nfs_config** command is used to modify the NFS common configuration.

##### Format

**change service nfs_config** { communication_thread_number=? \| work_thread_number=? \| max_block_size=? \| { permit_listen_ip=? \| deny_listen_ip=? } \| { permit_client=? \| deny_client=? } \| communication_thread_priority=? \| silent_time=? \| fileid_length=? \| transcode_switch=? \| nsm_query_dns_switch=? \| v3_automount_switch=? \| v4_automount_switch=? \| v41_automount_switch=? \| extended_groups_switch=? \| extended_groups_limit=? \| slow_io_percent=? \| nobody_uid=? \| { default_win_user=? \| clear_default_win_user=? } \| flow_control_switch=? \| flow_control_percent=? \| flow_control_timedelay=? \| ignore_nt_acl_for_root=? \| g_v4_acl_preserve=? \| g_ntfs_unix_security_ops=? \| touch_check_with_acl=? \| nfsv41_status=? \| chown_mode=? \| map_v4_everyone_ace_to_other_modebits=? } \*

**change service nfs_config** { v3_automount_switch=? \| v4_automount_switch=? \| v41_automount_switch=? \| extended_groups_switch=? \| extended_groups_limit=? \| nobody_uid=? \| { default_win_user=? \| clear_default_win_user=? } \| ignore_nt_acl_for_root=? \| g_v4_acl_preserve=? \| g_ntfs_unix_security_ops=? \| touch_check_with_acl=? \| chown_mode=? \| map_v4_everyone_ace_to_other_modebits=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| communication_thread_number=? | Number of NFS-based communication threads. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value ranges from 1 to 128. |
| work_thread_number=? | Number of NFS-based working threads. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value ranges from 1 to 128. |
| max_block_size=? | NFS MTU. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value ranges from 1024 to 1048576. |
| permit_listen_ip=? | Whitelist of NFS listening IP addresses. NOTE: This parameter is not supported by the current version. The execution result is invalid. | A maximum of 31 IP addresses can be entered. Separate IP addresses with a comma (,). An asterisk (*) indicates all IP addresses. |
| deny_listen_ip=? | Blacklist of NFS listening IP addresses. NOTE: This parameter is not supported by the current version. The execution result is invalid. | A maximum of 31 IP addresses can be entered. Separate IP addresses with a comma (,). An asterisk (*) indicates all IP addresses. |
| permit_client=? | Whitelist of NFS clients. NOTE: This parameter is not supported by the current version. The execution result is invalid. | You can enter an asterisk (*) to add all clients to the whitelist. |
| deny_client=? | Blacklist of NFS clients. NOTE: This parameter is not supported by the current version. The execution result is invalid. | A maximum of 31 IP addresses can be entered. Separate IP addresses with a comma (,). |
| communication_thread_priority=? | Priority of NFS-based communication threads. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be: <br>"highest": highest priority.<br>"high": high priority.<br>"middle": medium priority.<br>"normal": normal priority. |
| transcode_switch=? | Whether to enable or disable NFS transcoding. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "enable" or "disable", where: <br>"enable": enables the NFS transcoding function.<br>"disable": disables the NFS transcoding function. |
| silent_time=? | NFS silent period. | The value ranges from 5 to 1200, in seconds. If NFSv4.1 is enabled, silent_time should not be less than lease_period (30-90). |
| fileid_length=? | NFS file ID length. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "32" or "64", where: <br>"32": enables the storage array to support clients with 32-bit file IDs.<br>"64": enables the storage array to support clients with 64-bit file IDs. |
| nsm_query_dns_switch=? | Whether to enable or disable the function of NSM to query DNS host names. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "enable" or "disable", where: <br>"enable": enables the function of NSM to query DNS host names.<br>"disable": disables the function of NSM to query DNS host names. |
| v3_automount_switch=? | Whether to enable or disable the function of automatically mounting directories for NFSv3 (vStore). NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "enable" or "disable", where: <br>"enable": enables the function of automatically mounting directories for NFSv3.<br>"disable": disables the function of automatically mounting directories for NFSv3. |
| v4_automount_switch=? | Whether to enable or disable the function of automatically mounting directories for NFSv4 (vStore). NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "enable" or "disable", where: <br>"enable": enables the function of automatically mounting directories for NFSv4.<br>"disable": disables the function of automatically mounting directories for NFSv4. |
| v41_automount_switch=? | Whether to enable or disable the function of automatically mounting directories for NFSv4.1 (vStore). NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "enable" or "disable", where: <br>"enable": enables the function of automatically mounting directories for NFSv4.1.<br>"disable": disables the function of automatically mounting directories for NFSv4.1. |
| extended_groups_switch=? | Whether to enable the extended user group (vStore). | The value can be "enable" or "disable", where: <br>"enable": enables the extended group function.<br>"disable": disables the extended group function. |
| extended_groups_limit=? | Number of extended user groups (vStore). | The value ranges from 16 to 1024. |
| slow_io_percent=? | Percentage of slow I/O requests. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 1 to 100. |
| nobody_uid=? | ID of the nobody user. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 0 to 4294967295. |
| default_win_user=? | Default Windows user of the NFS user mapping. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is a string of 1 to 255 characters. The value cannot be "/[]:;|=,+*?<>@, spaces, or control characters, and cannot end with a period (.). The name of an AD domain user must be entered in the format of domain name\\domain user name. This parameter is valid only when the user mapping is enabled. |
| clear_default_win_user=? | Deletes the default Windows user of the NFS user mapping. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is "yes". |
| flow_control_switch=? | Switch of NFS I/O flow control. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "enable" or "disable", where: <br>"enable": enables the NFS I/O flow control switch.<br>"disable": disables the NFS I/O flow control switch. |
| flow_control_percent=? | Percentage of the number of NFS slow I/O requests to the total number of requests in flow control. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 10 to 100. |
| flow_control_timedelay=? | Delay threshold of NFS I/O flow control. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 1 to 360000. |
| ignore_nt_acl_for_root=? | Whether to ignore the NT ACL check for NFS user "root". | The value can be "enable" or "disable", where: <br>"enable": ignores the NT ACL set on files or directories for NFS user "root".<br>"disable": maps NFS user "root" to a Windows user and checks the NT ACL set on files or directories. |
| g_v4_acl_preserve=? | vStore-level NFS ACL protection policy. | The value can be "enable", "disable", or "use_nfs_share_permission", where: <br>"enable": In UNIX security mode, the NFSv4 ACL is preserved during the NFS client permission modification.<br>"disable": In UNIX security mode, the NFSv4 ACL is deleted during the NFS client permission modification.<br>"use_nfs_share_permission": In UNIX security mode, use the configuration of the NFS share permissions.<br> The default value is "use_nfs_share_permission". |
| g_ntfs_unix_security_ops=? | NTFS UNIX security option. | The value can be "fail", "ignore", or "use_nfs_share_permission" where: <br>"fail": In NTFS security mode, if the ACL exists, modifying the permission on the NFS client is not allowed.<br>"ignore": In NTFS security mode, if the ACL exists, modifying the permission on the NFS client is ignored.<br>"use_nfs_share_permission": In NTFS security mode, use the configuration of the NFS share permissions.<br> The default value is "use_nfs_share_permission". |
| touch_check_with_acl | Whether to use ACL authentication when you modify the time of a file or directory by running the "touch" command on a Linux client. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "enable" or "disable", where: <br>"enable": uses ACL authentication.<br>"disable": does not use ACL authentication. |
| nfsv41_status=? | Running status of the NFSv4.1 service. | The value can be "enable" or "disable", where: <br>"enable": enables the NFSv4.1 sharing service.<br>"disable": disables the NFSv4.1 sharing service. |
| chown_mode=? | Change ownership (owner or group) mode. | The value can be "restricted", "unrestricted", or "use_nfs_share_permission", where: <br>"restricted": Only the root user can change the owner of a file or directory.<br>"unrestricted": The root user, owner, or a non-owner who has the write permission in the ACL can change the ownership of a file or directory.<br>"use_nfs_share_permission": NFS share permission configuration is used. |
| map_v4_everyone_ace_to_other_modebits=? | Mapping between NFSv4 Everyone@ACE and mode bits during conversion between NFSv4 ACLs and mode bits. | The value can be adjusted_mapping or direct_mapping: <br>"adjusted_mapping": During the conversion from NFSv4 ACL to mode bits, according to the RFC, the permission of Everyone@ACE is mapped to the owner, group, and other mode bits. To ensure consistency between the ACL-to-mode and mode-to-ACL conversions, the owner and group mode bits relative to other mode bits are also considered during the mode-to-ACL conversion.<br>"direct_mapping": During the conversion from NFSv4 ACL to mode bits, the permission of Everyone@ ACE is mapped only to other mode bits. During the mode-to-ACL conversion, regardless of the relative nature of the owner and group mode bits with other mode bits, the other mode bits are mapped directly to Everyone@ACE. |

##### Usage Guidelines

None

##### Example

Query the NFS common configuration before modification.

```text
admin:/>show service nfs_config
Communication Thread Number   : 100
Work Thread Number       : 100
Max Block Size         : 10240
Listen IP            : deny 192.168.1.1
Client List           : deny 192.168.1.1
Communication Thread Priority : normal
Transcode Switch Status    : Enabled
Silent Time(s)         : 60
Fileid Length(bit)       : 64
Nsm Query Dns Switch Status : Enabled
NFSv3 Automount Switch      : Disabled
NFSv4 Automount Switch      : Disabled
NFSv4.1 Automount Switch    : Disabled
Extended Groups Switch        : Disabled
Extended Groups Limit         : 32
Slow I/O Percent(%)           : 50
Nobody ID                     : 65534
Default Windows User          : --
Flow Control Switch           : Disabled
Flow Control Percent(%)       : 50
Flow Control Timedelay(ms)    : 200
Ignore NT ACL For Root        : Enabled
Global v4 Acl Preserve        : use_nfs_share_permission
Global Ntfs Unix Security Ops : use_nfs_share_permission
Touch check with ACL          : Enabled
Nfsv41 Service Status         : Disabled
Chown Mode                    : use_nfs_share_permission
Map V4 Everyone Ace To Other Modebits : Adjusted Mappping
```

Change the number of NFS-based communication threads.

```text
admin:/>change service nfs_config communication_thread_number=100
Command executed successfully.
```

Change the maximum number of working threads allowed in sharing.

```text
admin:/>change service nfs_config work_thread_number=100
Command executed successfully.
```

Change the MTU.

```text
admin:/>change service nfs_config max_block_size=10240
Command executed successfully.
```

Modify the blacklist of listening IP addresses.

```text
admin:/>change service nfs_config permit_listen_ip=*
Command executed successfully.
```

Modify the blacklist of client IP addresses.

```text
admin:/>change service nfs_config permit_client=*
Command executed successfully.
```

Change the priority of the NFS-based communication threads.

```text
admin:/>change service nfs_config communication_thread_priority=high
Command executed successfully.
```

Change the NFS silent time.

```text

admin:/>change service nfs_config silent_time=80
WARNING: You are about to change the default NFS silent period. The value ranges from 5 to 1200, in seconds(5-1200). If NFSv4.1 is enabled, silent_time should not be less than lease_period. (range of lease_period is 30 to 90).

Suggestion: Before performing this operation, ensure that this operation is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

Enable NFS to support clients with 32-bit file IDs.

```text
admin:/>change service nfs_config fileid_length=32
WARNING: This operation will change the type of NFS clients (with 32-bit or 64-bit file ID) supported by the storage array. After this operation, the NFS client services may be interrupted.
Suggestion: Before performing this operation, ensure that this operation is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable or disable NFS transcoding.

```text
admin:/>change service nfs_config transcode_switch=disable
Command executed successfully.
```

Enable or disable the function of NSM to query DNS host names.

```text
admin:/>change service nfs_config nsm_query_dns_switch=disable
Command executed successfully.
```

Enable or disable the function of automatically mounting directories for NFSv3.

```text
admin:/>change service nfs_config v3_automount_switch=enable
WARNING: You are about to enable or disable the function of automatically mounting directories for NFS. This operation may cause service interruption. If services are interrupted, mount shares again.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable or disable the function of automatically mounting directories for NFSv4.

```text
admin:/>change service nfs_config v4_automount_switch=enable
WARNING: You are about to enable or disable the function of automatically mounting directories for NFS. This operation may cause service interruption. If services are interrupted, mount shares again.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable or disable the function of automatically mounting directories for NFSv4.1.

```text
admin:/>change service nfs_config v41_automount_switch=enable
WARNING: You are about to enable or disable the function of automatically mounting directories for NFS. This operation may cause service interruption. If services are interrupted, mount shares again.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable or disable the extended group function.

```text
admin:/>change service nfs_config extended_groups_switch=disable
Command executed successfully.
```

Change the number of extended groups.

```text
admin:/>change service nfs_config extended_groups_limit=64
Error: The extended group function is not enabled.
Suggestion: Enable the extended group function and then try again.
```

Change the default Windows user of the NFS user mapping.

```text
admin:/>change service nfs_config default_win_user=win_user
WARNING: You are about to change the default Windows user of the NFS user mapping. If the versions of storage systems at the two active-active ends are different, after the working site switchover, users without the mapping relationship cannot access the NFS share service.
Suggestion: If the versions of storage systems at the two active-active ends are different, configure the user mapping before performing this operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable or disable the NFS I/O flow control switch.

```text
admin:/>change service nfs_config flow_control_switch=enable
Command executed successfully.
```

Change the percentage of NFS slow I/O requests in flow control.

```text
admin:/>change service nfs_config flow_control_percent=20
Command executed successfully.
```

Change the delay threshold of NFS I/O flow control.

```text
admin:/>change service nfs_config flow_control_timedelay=100
Command executed successfully.
```

Query the NFS common configuration after modification.

```text
admin:/>show service nfs_config
Communication Thread Number  : 100
Work Thread Number       : 100
Max Block Size         : 10240
Listen IP            : permit *
Client List           : permit *
Communication Thread Priority : high
Transcode Switch Status    : Disabled
Silent Time(s)         : 80
Fileid Length(bit)       : 32
Nsm Query Dns Switch Status : Disabled
NFSv3 Automount Switch      : Enabled
NFSv4 Automount Switch      : Enabled
NFSv4.1 Automount Switch    : Enabled
Extended Groups Switch      : Disabled
Extended Groups Limit       : 32
Nobody UID                  : 65534
Default Windows User        : win_user
Flow Control Switch         : Enabled
Flow Control Percent(%)     : 20
Flow Control Timedelay(ms)  : 100
Ignore NT ACL For Root      : Enabled
Global v4 Acl Preserve        : use_nfs_share_permission
Global Ntfs Unix Security Ops : use_nfs_share_permission
Touch check with ACL          : Enabled
Nfsv41 Service Status         : Enabled
Chown Mode                    : use_nfs_share_permission
Map V4 Everyone Ace To Other Modebits : Adjusted Mappping
```

Enable or disable the function of automatically mounting directories for NFSv3 in a vStore.

```text
admin@vstore1:/>change service nfs_config v3_automount_switch=enable
WARNING: You are about to enable or disable the function of automatically mounting directories for NFS. This operation may cause service interruption. If services are interrupted, mount shares again.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable or disable the function of automatically mounting directories for NFSv4 in a vStore.

```text
admin@vstore1:/>change service nfs_config v4_automount_switch=enable
WARNING: You are about to enable or disable the function of automatically mounting directories for NFS. This operation may cause service interruption. If services are interrupted, mount shares again.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable or disable the function of automatically mounting directories for NFSv4.1 in a vStore.

```text
admin@vstore1:/>change service nfs_config v41_automount_switch=enable
WARNING: You are about to enable or disable the function of automatically mounting directories for NFS. This operation may cause service interruption. If services are interrupted, mount shares again.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query NFS configurations in a vStore after modification.

```text
admin@vstore1:/>show service nfs_config
NFSv3 Automount Switch : Enabled
NFSv4 Automount Switch : Enabled
NFSv4.1 Automount Switch : Enabled
Extended Groups Switch : Disabled
Extended Groups Limit : 32
Nobody UID : 65534
Default Windows User : --
Ignore NT ACL For Root : Enabled
Global v4 Acl Preserve : use_nfs_share_permission
Chown Mode             : use_nfs_share_permission
Map V4 Everyone Ace To Other Modebits : Adjusted Mappping
```

Enable or disable the extended group function in a vStore.

```text
admin@vstore1:/>change service nfs_config extended_groups_switch=enable
WARNING: You are about to enable the extended group function. This operation may degrade the NFS service performance.
Suggestion: Confirm that you want to perform this operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the number of extended groups in a vStore.

```text
admin@vstore1:/>change service nfs_config extended_groups_limit=64
Command executed successfully.
```

Set the ID of the nobody user.

```text
admin:/>change service nfs_config nobody_id=65534
Command executed successfully.
```

Sets the percentage of slow I/O requests.

```text
admin:/>change service nfs_config slow_io_percent=60
Command executed successfully.
```

Change the running status of the NFSv4.1 service.

```text
admin:/>change service nfs_config nfsv41_status=enable
DANGER: You are about to enable or disable NFSv4.1. This operation may interrupt services.
Suggestion: Confirm that you want to perform this operation based on the service type.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
