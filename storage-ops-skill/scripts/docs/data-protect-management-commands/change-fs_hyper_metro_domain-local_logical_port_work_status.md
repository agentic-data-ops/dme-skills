# change fs_hyper_metro_domain local_logical_port_work_status


##### Function

The **change fs_hyper_metro_domain local_logical_port_work_status** command is used to change the working status of all local logical ports in a HyperMetro domain cluster.

##### Format

**change fs_hyper_metro_domain local_logical_port_work_status** domain_id=? work_status=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id=? | File system HyperMetro domain ID. | You can run the "show fs_hyper_metro_domain general" command to obtain the value. |
| work_status=? | Working status of the logical port in the local file system HyperMetro domain. | The value can be "working" or "standby", where: <br>"working": enabled.<br>"standby": disabled. |

##### Usage Guidelines

None

##### Example

Change the working status of the local logical port in the HyperMetro domain whose ID is "1" to "standby".

```text
admin:/>change fs_hyper_metro_domain local_logical_port_work_status domain_id=1 work_status=standby
DANGER:
You are about to disable all logical ports on the local end of the file system HyperMetro domain. This operation may cause service interruption or service exceptions.
Suggestion: Before performing this operation, ensure that this operation is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the working status of the local logical port in HyperMetro domain "1" to "working".

```text
admin:/>change fs_hyper_metro_domain local_logical_port_work_status domain_id=1 work_status=working
DANGER:
You are about to enable all logical ports on the local end of the file system HyperMetro domain. Ensure that remote logical ports of the file system HyperMetro domain are disabled. Otherwise, this operation may cause IP address conflicts or data loss.
Suggestion: Before performing this operation, ensure that all remote logical ports of the file system HyperMetro domain are disabled. If the remote logical ports cannot be disabled, for example, the remote storage array is faulty, disconnect the remote site from the host.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
