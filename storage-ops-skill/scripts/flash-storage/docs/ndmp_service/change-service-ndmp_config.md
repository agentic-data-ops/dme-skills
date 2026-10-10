# change service ndmp_config


##### Function

The **change service ndmp_config** command is used to modify NDMP configurations.

##### Format

**change service ndmp_config** { is_enabled=? \| port=? \| ip=? \| restore_quota=? \| ignore_ctime=? \| data_connect_mode=? \| fs_global_scope=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| is_enabled=? | Whether to enable NDMP. | The value can be "yes" or "no", where: <br>"yes": Enable NDMP.<br>"no": Disable NDMP. |
| port=? | Port number. | The value is an integer ranging from 10000 to 10032. |
| ip=? | Listening IP address. NOTE: This parameter is not supported in this version, and the execution result is invalid. | - |
| restore_quota=? | Quota restored to the file system. NOTE: This field is not supported in this version and the command output is invalid. | The value is an integer ranging from 0 to 100. |
| ignore_ctime=? | Whether to ignore the ctime during backup. NOTE: Hard links cannot be backed up after the ctime is ignored. | The value can be "yes" or "no", where: <br>"yes": Ignore the ctime.<br>"no": Do not ignore the ctime. |
| fs_global_scope=? | Whether to enable global visibility of vStore file systems. | The value can be 1 or 0. <br>on: enabled.<br>off: disabled. |
| data_connect_mode=? | The LIF port mode is used for data connections. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The value is an enumerated value ranging from 1 to 3. <br>1: The IP address of a vStore is preferred.<br>2: The management IP address is preferred.<br>3: Only vStore IP addresses are used. |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Modify the NDMP configuration.

```text

admin:/>change service ndmp_config port=10000 ip=192.168.0.1 ignore_ctime=no

WARNING:You are about to change the monitoring IP address or monitoring port.
1. After this operation, the NDMP service will be automatically restarted. As a result, the NDMP service of all the vStores will be interrupted.
2. After the configurations take effect, the NDMP service of some vStores will become unavailable.
Suggestion: After performing this operation, vStore administrators must enable all the monitoring IP addresses to ensure that vStores can access the NDMP service normally.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

Modify the NDMP configuration.

```text
admin:/>change service ndmp_config is_enabled=yes
Command executed successfully.
```

Disable the NDMP service.

```text
admin:/>change service ndmp_config is_enabled=no
WARNING:You are about to disable the NDMP service. This operation causes the NDMP service provided by the storage device unavailable.
Suggestion: Before performing this operation, ensure that the NDMP service is no longer needed.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Modify the NDMP configuration.

```text

admin:/>change service ndmp_config ip=192.168.0.1 port=10000

WARNING:You are about to change the monitoring IP address or monitoring port.
1. After this operation, the NDMP service will be automatically restarted. As a result, the NDMP service of all the vStores will be interrupted.
2. After the configurations take effect, the NDMP service of some vStores will become unavailable.
Suggestion: After performing this operation, vStore administrators must enable all the monitoring IP addresses to ensure that vStores can access the NDMP service normally.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

Modify the NDMP configuration.

```text
admin:/>change service ndmp_config data_connect_mode=1
Command executed successfully.
```

Modify the NDMP configuration.

```text
admin:/>change service ndmp_config ads_enable=yes
Command executed successfully.
```

Modify the NDMP configuration.

```text
admin:/>change service ndmp_config fs_global_scope=on
Command executed successfully.
```

##### System Response

None
