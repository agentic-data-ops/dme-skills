# delete logical_port general


##### Function

The **delete logical_port general** command is used to delete the specific logical port.

##### Format

**delete logical_port general** logical_port_name=?

##### Parameters

| Parameter           | Description        | Value                                                                                   |
|---------------------|--------------------|-----------------------------------------------------------------------------------------|
| logical_port_name=? | Logical port name. | Run the "show logical_port general" command without any parameters to obtain the value. |

##### Usage Guidelines

-   To show the logical port name, run "show logical_port general".
-   To delete the specific logical port, run "**delete logical_port general** logical_port_name=?".

##### Example

Delete the specified logical port by name.

```text
admin:/>delete logical_port general logical_port_name=test
DANGER: You are about to delete logical port. This operation will interrupt the management services or data access services carried by the port.
Suggestion: Before performing this operation, ensure that you have correctly selected the logical port and the logical port is no longer required.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
