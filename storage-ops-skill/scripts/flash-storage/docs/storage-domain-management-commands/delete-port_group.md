# delete port_group


##### Function

The **delete port_group** command is used to delete a port group.

##### Format

**delete port_group** { port_group_id=? \| port_group_name=? }

##### Parameters

| Parameter         | Description                                   | Value                                               |
|-------------------|-----------------------------------------------|-----------------------------------------------------|
| port_group_id=?   | ID of a port group that you want to delete.   | To obtain the value, run "show port_group general". |
| port_group_name=? | Name of a port group that you want to delete. | To obtain the value, run "show port_group general". |

##### Usage Guidelines

Remove all ports from a port group before deleting it. Otherwise, you cannot delete the port group.

##### Example

Delete port group "1".

```text
admin:/>delete port_group port_group_id=1
WARNING: You are about to delete port group. This operation cannot be undone. This operation will remove all ports within the port group and delete the port group information from the system.
Suggestion: Before performing this operation, ensure that the selected port group is no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete port group "portgroup1".

```text
admin:/>delete port_group port_group_name=portgroup1
WARNING: You are about to delete port group. This operation cannot be undone. This operation will remove all ports within the port group and delete the port group information from the system.
Suggestion: Before performing this operation, ensure that the selected port group is no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
