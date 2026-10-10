# change logical_port failover_group


##### Function

The **change logical_port failover_group** command is used to configure failover groups for one or more logical ports.

##### Format

**change logical_port failover_group** { failover_group_id=? \| failover_group_name=? } logical_port_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| logical_port_list=? | Name of a logical port. The value contains 1 to 255 characters, including digits, letters, periods (.), underscores (_), and hyphens (-). | To obtain the value, run the "show logical_port general" command.<br>When multiple logical ports are entered, separate the port names from each other using commas (,). |
| failover_group_id=? | ID of a failover group. | The value is an integer from 1 to 1024 or is the "default" character string. |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |

##### Usage Guidelines

-   The "logical_port_list" parameter supports one or more logical port names.
-   The "failover_group_id" parameter supports the ID (between 1 and 1024) of a customized failover group.
-   The "failover_group_id" parameter supports "default", which indicating the default failover group. Logical ports created on physical ports or bond ports use system failover groups, and those created on VLANs use VLAN failover groups.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Change the failover group of logical port "lif1".

```text
admin:/>change logical_port failover_group failover_group_id=1 logical_port_list=lif1
DANGER: You are about to change the failover group of the logical port.This operation may interrupt services running on the logical port because no port is available for the IP address floating of the logical port in the new failover group.
Suggestion: Before performing this operation, ensure that services are not interrupted when the IP address of the logical port floats in the new failover group.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change logical port lif1 failover group ID successfully.
```

Batch change the failover groups of logical ports "lif1", "lif2", and "lif3".

```text
admin:/>change logical_port failover_group failover_group_id=1 logical_port_list=lif1,lif2,lif3
DANGER: You are about to change the failover group of the logical port.This operation may interrupt services running on the logical port because no port is available for the IP address floating of the logical port in the new failover group.
Suggestion: Before performing this operation, ensure that services are not interrupted when the IP address of the logical port floats in the new failover group.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change logical port lif1 failover group ID successfully.
Change logical port lif2 failover group ID successfully.
Change logical port lif3 failover group ID successfully.
```

##### System Response

None
