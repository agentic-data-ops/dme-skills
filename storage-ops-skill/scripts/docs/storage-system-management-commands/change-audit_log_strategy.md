# change audit_log_strategy


##### Function

The **change audit_log_strategy** command is used to modify the audit log strategy.

##### Format

**change audit_log_strategy** \[ { vstore_id=? \| vstore_name=? } \] \[ enable=? \] \[ single_file_size=? \] \[ { reserve_file_num=? \| occupied_capacity=? } \] \[ cifs_login_logout=? \] \[ guarantee_mode=? \] \[ file_access=? \] \[ audit_policy_change=? \]

**change audit_log_strategy** \[ enable=? \] \[ single_file_size=? \] \[ { reserve_file_num=? \| occupied_capacity=? } \] \[ cifs_login_logout=? \] \[ guarantee_mode=? \] \[ file_access=? \] \[ audit_policy_change=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |
| vstore_name=? | vStore name. | The value is a string of 1 to 256 characters. You can run the "show vstore" command without parameters to obtain the value. |
| enable=? | Switch of starting and stopping audit log collection. | The value can be "On" or "Off", where: <br>"Off": disabled.<br>"On": enabled. |
| cifs_login_logout=? | Whether to log CIFS login and logout events. | The value can be "On" or "Off", where: <br>"Off": CIFS login and logout operations are not recorded in logs.<br>"On": CIFS login and logout operations are recorded in logs. |
| single_file_size=? | Size of a single audit log. | The unit is MB. The value ranges from 10 to 100. |
| reserve_file_num=? | Number of reserved audit logs. | The value is expressed in thousands of logs and ranges from 1 to 1200. |
| occupied_capacity=? | Occupied capacity of the audit log file system. | The value includes the capacity value and unit (GB). The value must be greater than or equal to 5 GB. |
| guarantee_mode=? | Whether to enable audit log guarantee mode. | The value can be "Guarantee" or "Not-guarantee", where: <br>"Not-guarantee": The system does not guarantee that all auditable file access events are audit logged.<br>"Guarantee": The system guarantees that all auditable file access events are audit logged. |
| file_access=? | Whether to log file access events. | The value can be "On" or "Off", where: <br>"Off": Do not log file access events.<br>"On": Log file access events. |
| audit_policy_change=? | Whether to log the changes to the audit policy. | The value can be "On" or "Off", where: <br>"Off": Do not log the changes to the audit policy.<br>"On": Log the changes to the audit policy. |

##### Usage Guidelines

-   Parameter "enable" is mutually exclusive with other parameters.
-   If the automatic deletion switch of audit logs is enabled, logs will be deleted based on parameter "reserve_file_num" or "occupied_capacity".
-   Plan the capacity of the audit log file system. If the capacity cannot meet the requirements of parameter "reserve_file_num", services may be interrupted.

##### Example

Disable the audit log switch for the vStore whose ID is 1.

```text
admin:/>change audit_log_strategy vstore_id=1 enable=Off
WARNING: You are about to disable the audit log function. This operation will uninstall the audit log file system, which contains important audit logs. The audit logs must be handled properly. Exercise caution when performing this operation.
Suggestion: Note the following:
1. Before performing this operation, stop sharing the audit log file system.
2. After performing this operation, clear or migrate data in the audit log file system.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Set the number of reserved audit logs to 10,000 for the vStore whose ID is "1".

```text
admin:/>change audit_log_strategy vstore_id=1 reserve_file_num=10
WARNING: You are about to change the threshold of the audit log automatic deletion function. If the capacity specified by this parameter is greater than the capacity of the audit log file system, audit logs may fail to be recorded and services may be interrupted.
Suggestion: Before performing this operation, ensure that the file system will have sufficient capacity.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Set the audit log policy of the vStore whose ID is "1" to "Guarantee".

```text
admin@vs1:/>change audit_log_strategy guarantee_mode=Guarantee
DANGER: You are about to configure the audit log strategy as the guarantee mode. The guarantee mode will give priority to the audit function, causing risks of performance deterioration or service interruption.
Suggestion: Before performing this operation, ensure that the preceding risks are acceptable.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
```

Set the audit log policy of the vStore whose ID is "1" to "Not-guarantee".

```text
admin@vs1:/>change audit_log_strategy guarantee_mode=Not-guarantee
WARNING: You are about to configure the audit log strategy as the non-guarantee mode. The non guarantee mode will give priority to service running. As a result, audit log record omissions may occur, causing security risks.
Suggestion: Before performing this operation, ensure that the preceding risks are acceptable.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
