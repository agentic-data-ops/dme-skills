# delete failover_group general


##### Function

The **delete failover_group general** command is used to delete a specified customized failover group.

##### Format

**delete failover_group general** { failover_group_id=? \| failover_group_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of a failover group. | The value is an integer between 1 and 1024.<br>To obtain the value, run the "show failover_group general" command without parameters. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |

##### Usage Guidelines

-   Run the "show failover_group general" command to view the failover group ID.
-   Run the "delete failover_group failover_group_id=?" command to delete a specified customized failover group. Only customized failover groups are supported.
-   Run the "delete failover_group failover_group_name=?" command to delete a specified customized failover group. Only customized failover groups are supported.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Delete a specified customized failover group.

```text
admin:/>delete failover_group general failover_group_id=1
DANGER:You are about to delete a customized failover group.
After this operation, logical ports that are originally associated with the failover group will be associated with the default failover group or VLAN failover group. Then, these logical ports may fail over to wrong ports, causing service interruption.
Suggestion: Before performing this operation, ensure that the failover of the logical ports that are originally associated with the failover group will not affect service operation.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete a specified customized failover group.

```text
admin:/>delete failover_group general failover_group_name=FG001
DANGER: You are about to delete a customized failover group.
After this operation, logical ports that are originally associated with the failover group will be associated with the default failover group or VLAN failover group. Then, these logical ports may fail over to wrong ports, causing service interruption.
Suggestion: Before performing this operation, ensure that the failover of the logical ports that are originally associated with the failover group will not affect service operation.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
