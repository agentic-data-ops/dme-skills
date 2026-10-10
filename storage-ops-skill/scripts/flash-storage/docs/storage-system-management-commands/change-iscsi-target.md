# change iscsi target


##### Function

The **change iscsi target** command is used to modify information about the iSCSI link between two disk arrays.

##### Format

**change iscsi target** iscsi_id=? \[ port=? \| remote_ip=? \| recovery_policy=? \| chap_enabled=? \| chap_user=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| iscsi_id=? | ID of an iSCSI link. | To obtain the value, run "show iscsi target" without parameters. |
| port=? | TCP port ID of a remote device. | The value ranges from 1 to 65,535. The default value is "3260". |
| remote_ip=? | IP address of a remote device. | - |
| recovery_policy=? | Link recovery policy. | The value can be "automatic" or "manual", where: <br>"automatic": automatic recovery<br>"manual": manual recovery |
| chap_enabled=? | CHAP authentication status. | The value can be "yes" or "no", where: <br>"yes": CHAP authentication is enabled.<br>"no": CHAP authentication is disabled. |
| chap_user=? | CHAP user name. | The value contains 4 to 223 characters (32 < ASCII code < 127) and must start with a letter or a digit. |

##### Usage Guidelines

When the remote target changes, you can run this command to modify information about the iSCSI link between two disk arrays to set up an iSCSI link to the new target.

##### Example

Change the TCP port ID of the remote target of iSCSI link 1 to 23456.

```text
admin:/>change iscsi target iscsi_id=1 port=23456
DANGER: You are going to change the target. This operation will cause the running services relevant to the target to be interrupted.
Suggestion: Before you perform this operation, ensure that no services exist or all services relevant to the target are stopped.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
