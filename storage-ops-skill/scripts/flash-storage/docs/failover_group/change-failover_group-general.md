# change failover_group general


##### Function

The **change failover_group general** command is used to configure a customized failover group.

##### Format

**change failover_group general** { failover_group_id=? \| failover_group_name=? } name=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| failover_group_id=? | ID of a failover group. | The value is an integer from 1 to 1024.<br>To obtain the value, run the "show failover_group general" command without parameters. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| name=? | New name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |

##### Usage Guidelines

-   The "failover_group_id" parameter supports only the ID of a customized failover group.
-   The "failover_group_name" parameter supports only the name of a customized failover group.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Change the name of a customized failover group.

```text
admin:/>change failover_group general failover_group_id=1 name=group1
Command executed successfully.
```

Change the name of a customized failover group.

```text
admin:/>change failover_group general failover_group_name=FG001 name=group1
Command executed successfully.
```

##### System Response

None
