# change logical_port failback


##### Function

The **change logical_port failback** command is used to fail back a logical port.

##### Format

**change logical_port failback** logical_port_name=?

##### Parameters

| Parameter           | Description                                                                                                                           | Value                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| logical_port_name=? | Logical port name. The value contains 1 to 255 characters, including digits, letters, periods (.), underscores (\_), and hyphens (-). | To obtain the value, run "show logical_port general". |

##### Usage Guidelines

-   Before performing this operation, determine whether the modification is necessary.
-   The command only supports logical port that is NAS protocol type.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Fail back logical port "lif1".

```text
admin:/>change logical_port failback logical_port_name=lif1
DANGER: You are about to perform logical port failback. This operation may interrupt services or cause service exceptions.
Suggestion: Before performing this operation, determine whether the operation is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
