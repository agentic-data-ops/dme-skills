# delete host_group


##### Function

The **delete host_group** command is used to delete a host group.

##### Format

**delete host_group** { host_group_id=? \| host_group_name=? }

##### Parameters

| Parameter         | Description                                   | Value                                               |
|-------------------|-----------------------------------------------|-----------------------------------------------------|
| host_group_id=?   | ID of a host group that you want to delete.   | To obtain the value, run "show host_group general". |
| host_group_name=? | Name of a host group that you want to delete. | To obtain the value, run "show host_group general". |

##### Usage Guidelines

None.

##### Example

Delete host group "1".

```text
admin:/>delete host_group host_group_id=1
WARNING: You are about to delete host group. This operation cannot be undone. This operation will delete the initiators of the hosts within the host group and the information about the host group from the system.
Suggestion: Before performing this operation, ensure that the selected host group is no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete host group "name1".

```text
admin:/>delete host_group host_group_name=name1
WARNING: You are about to delete host group. This operation cannot be undone. This operation will remove all hosts within the host group and the information about the host group from the system.
Suggestion: Before performing this operation, ensure that the selected host group is no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
