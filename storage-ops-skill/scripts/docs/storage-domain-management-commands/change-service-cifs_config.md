# change service cifs_config


##### Function

The **change service cifs_config** command is used to change the CIFS common configuration.

##### Format

**change service cifs_config** { communication_thread_number=? \| work_thread_number=? \| max_block_size=? \| { permit_listen_ip=? \| deny_listen_ip=? } \| { permit_client=? \| deny_client=? \| communication_thread_priority=? } \| support_smb3_protocol=? \| open_percent=? \| slow_io_percent=? \| { default_unix_user=? \| clear_default_unix_user=? } \| flow_control_switch=? \| flow_control_percent=? \| flow_control_timedelay=? \| { antivirus_server_ip=? \| clear_antivirus_server_ip=? } } \*

**change service cifs_config** { default_unix_user=? \| clear_default_unix_user=? \| { antivirus_server_ip=? \| clear_antivirus_server_ip=? } } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| communication_thread_number=? | Number of CIFS-based communication threads. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 1 to 128. |
| work_thread_number=? | Number of CIFS-based working threads. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 1 to 128. |
| max_block_size=? | CIFS MTU. | The value must be an integer from 65,536 to 1,048,576. |
| permit_listen_ip=? | Whitelist of CIFS listening IP addresses. NOTE: This parameter is not supported by the current version. The execution result is invalid. | A maximum of 31 IP addresses can be entered. Separate IP addresses with a comma (,). Enter an asterisk (*) to add all IP addresses to the whitelist. |
| deny_listen_ip=? | Blacklist of CIFS listening IP addresses. NOTE: This parameter is not supported by the current version. The execution result is invalid. | A maximum of 31 IP addresses can be entered. Separate IP addresses with a comma (,). Enter an asterisk (*) to add all IP addresses to the blacklist. |
| permit_client=? | Whitelist of CIFS clients. NOTE: This parameter is not supported by the current version. The execution result is invalid. | Enter an asterisk (*) to add all clients to the whitelist. |
| deny_client=? | Blacklist of CIFS clients. NOTE: This parameter is not supported by the current version. The execution result is invalid. | A maximum of 31 IP addresses can be entered. Separate IP addresses with a comma (,). |
| communication_thread_priority=? | Priority of CIFS-based communication threads. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "highest", "high", "middle", or "normal". |
| support_smb3_protocol=? | Switch of the SMB3 protocol. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no". |
| open_percent=? | Percentage of the maximum times that a file can be opened. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 1 to 100. |
| slow_io_percent=? | Percentage of slow I/O requests. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 1 to 100. |
| default_unix_user=? | Default UNIX user of the CIFS user mapping. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is a string of 1 to 255 characters. The value cannot be "/[]:;|=,+*?<>@, spaces, or control characters, and cannot end with a period (.). This parameter is valid only when the user mapping is enabled. |
| clear_default_unix_user=? | Deletes the default UNIX user of the CIFS user mapping. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is "yes". |
| flow_control_switch=? | Switch of CIFS I/O flow control. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "enable" or "disable", where: 1:"enable": enables the CIFS I/O flow control switch. 0:"disable": disables the CIFS I/O flow control switch. |
| flow_control_percent=? | Percentage of the number of CIFS slow I/O requests to the total number of requests in flow control. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 10 to 100. |
| flow_control_timedelay=? | Delay threshold of CIFS I/O flow control. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value must be an integer from 1 to 360000. |
| antivirus_server_ip=? | IP address of the CIFS share antivirus server. The value must be a valid IP address. Use commas (,) to separate multiple IP addresses. | The value must be a valid IP address. |
| clear_antivirus_server_ip=? | Deletes the IP address of the antivirus server. | The value is "yes". |

##### Usage Guidelines

-   "deny_listen_ip" and "permit_listen_ip" are mutually exclusive.
-   "permit_client" and "deny_client" are mutually exclusive.
-   "antivirus_server_ip" and "clear_antivirus_server_ip" are mutually exclusive.

##### Example

View the CIFS common configuration before configuration modification.

```text
admin:/>show service cifs_config
Communication Thread Number   : 12
Work Thread Number            : 12
Max Block Size(byte)          : 131072
Listen IP                     : permit *
Client List                   : permit *
Communication Thread Priority : normal
Support SMB3 Protocol         : yes
Open Percent(%)               : 50
Slow I/O Percent(%)           : 50
Default UNIX User             : --
Flow Control Switch           : Disabled
Flow Control Percent(%)       : 50
Flow Control Timedelay(ms)    : 200
Antivirus Server IP           : --
```

Change the maximum number of working threads supported by shares.

```text
admin:/>change service cifs_config work_thread_number=4
Command executed successfully
```

Change the MTU.

```text
admin:/>change service cifs_config max_block_size=130048
Command executed successfully
```

Modify the blacklist of listening IP addresses.

```text
admin:/>change service cifs_config deny_listen_ip=192.168.1.1
Command executed successfully.
```

Modify the blacklist of client IP addresses.

```text
admin:/>change service cifs_config deny_client=192.168.1.1
Command executed successfully
```

Change the number of CIFS-based communication threads.

```text
admin:/>change service cifs_config communication_thread_number=6
Command executed successfully
```

Change the priority of the CIFS-based communication threads.

```text
admin:/>change service cifs_config communication_thread_priority=high
Command executed successfully.
```

Change the status of the SMB3 protocol switch.

```text
admin:/>change service cifs_config support_smb3_protocol=yes
Command executed successfully.
```

Change the percentage of the maximum times that a file can be opened.

```text
admin:/>change service cifs_config open_percent=60
Command executed successfully.
```

Change the IP address of the CIFS share antivirus server.

```text
admin:/>change service cifs_config antivirus_server_ip=192.168.1.2
Command executed successfully.
```

Set the percentage of slow I/O requests.

```text
admin:/>change service cifs_config slow_io_percent=60
Command executed successfully.
```

Modify the default UNIX user mapped to the CIFS user.

```text
admin:/>change service default_unix_user=unix_user
WARNING: You are about to change the default UNIX user of the CIFS user mapping. If the versions of storage systems at the two active-active ends are different, after the working site switchover, users without the mapping relationship cannot access the CIFS share service.
Suggestion: If the versions of storage systems at the two active-active ends are different, configure the user mapping before performing this operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Modify the CIFS I/O traffic control switch.

```text
admin:/>change service cifs_config flow_control_switch=enable
Command executed successfully.
```

Change the percentage of slow CIFS I/O requests in traffic control.

```text
admin:/>change service cifs_config flow_control_percent=20
Command executed successfully.
```

Change the latency threshold for CIFS I/O traffic control.

```text
admin:/>change service cifs_config flow_control_timedelay=100
Command executed successfully.
```

View the modified common configuration information about CIFS.

```text
admin:/>show service cifs_config
Communication Thread Number   : 6
Work Thread Number            : 4
Max Block Size(byte)          : 130048
Listen IP                     : deny 192.168.1.1
Client List                   : deny 192.168.1.1
Communication Thread Priority : high
Support SMB3 Protocol         : yes
Open Percent(%)               : 60
Slow I/O Percent(%)           : 50
Default UNIX User             : unix_user
Flow Control Switch           : Enabled
Flow Control Percent(%)       : 20
Flow Control Timedelay(ms)    : 100
Antivirus Server IP           : 192.168.1.2
```

View the common configuration information about CIFS of the vStore before the modification.

```text
admin@vstore1:/>show service cifs_config
Default UNIX User             : --
Antivirus Server IP           : --
```

Modify the default UNIX user mapped to the CIFS user of the vStore.

```text
admin@vstore1:/>change service default_unix_user=unix_user
WARNING: You are about to change the default UNIX user of the CIFS user mapping. If the versions of storage systems at the two active-active ends are different, after the working site switchover, users without the mapping relationship cannot access the CIFS share service.
Suggestion: If the versions of storage systems at the two active-active ends are different, configure the user mapping before performing this operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

View the modified common configuration information about CIFS of the vStore.

```text
admin@vstore1:/>show service cifs_config
Default UNIX User             : unix_user
Antivirus Server IP           : --
```

##### System Response

None
