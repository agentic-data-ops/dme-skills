# show bond_port_count


##### Function

The **show bond_port_count** command is used to check the number of bond ports.

##### Format

**show bond_port_count** { failover_group_id=? \| failover_group_name=? }

##### Parameters

| Parameter             | Description               | Value                                                                                                              |
|-----------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------|
| failover_group_id=?   | ID of the failover group. | The value is an integer between 0 and 8191.                                                                        |
| failover_group_name=? | Name of a failover group. | The value contains 1 to 255 characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

You can use the **show bond_port_count** command to check the number of bond ports.

##### Example

To check the number of bond ports, run the following command:

```text
admin:/>show bond_port_count
Bond Port Number : 2

```

Query the number of bond ports in the failover group with name "System-defined".

```text
admin:/>show bond_port_count failover_group_name=System-defined
Bond Port Number : 1
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                             |
|------------------|-------------------------------------|
| Bond Port Number | Indicates the number of bond ports. |
