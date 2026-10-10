# delete host


##### Function

The **delete host** command is used to **delete host**s.

##### Format

**delete host** { host_id=? \| host_name=? }

##### Parameters

| Parameter   | Description     | Value                                         |
|-------------|-----------------|-----------------------------------------------|
| host_id=?   | ID of a host.   | To obtain the value, run "show host general". |
| host_name=? | Name of a host. | To obtain the value, run "show host general". |

##### Usage Guidelines

-   Running this command deletes a host from the storage system.
-   Before running this command, ensure that the selected host is exactly the one you want to delete.
-   Before running this command, ensure that the selected host is not in any mapping view. Otherwise, the command execution will fail.
-   Before running this command, ensure that no initiator has been added to the selected host. Otherwise, the command execution will fail.

##### Example

Delete host "1".

```text
admin:/>delete host host_id=1
WARNING: You are about to delete the host. This operation cannot be undone. This operation will delete the initiators of the host and the information about the host from the system.
Suggestion: Before performing this operation, ensure that the selected host is no longer necessary.
Have you read warning message carefully?(y/n)Y
Are you sure you really want to perform the operation?(y/n)Y
Command executed successfully.
```

Delete host "name1".

```text
admin:/>delete host host_name=name1
WARNING: You are about to delete host. This operation cannot be undone. This operation will delete the initiators of the host and the information about the host from the system.
Suggestion: Before performing this operation, ensure that the selected host is no longer necessary.
Have you read warning message carefully?(y/n)Y
Are you sure you really want to perform the operation?(y/n)Y
Command executed successfully.
```

##### System Response

None
