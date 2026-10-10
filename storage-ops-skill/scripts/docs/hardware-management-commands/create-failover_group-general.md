# create failover_group general


##### Function

The **create failover_group general** command is used to create a customized failover group.

##### Format

**create failover_group general** name=? \[ service_type=? \]

##### Parameters

| Parameter    | Description                                                   | Value                                                                                                              |
|--------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| name=?       | Name of a failover group.                                     | The value contains 1 to 255 characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |
| service_type | Failover group service type. The default service type is NAS. | \-                                                                                                                 |

##### Usage Guidelines

Run the "**create failover_group general** name=?" command to create a NAS service failover group with a specified name.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Create a failover group named "group1" with the default NAS service type.

```text
admin:/>create failover_group general name=group1
Command executed successfully.
```

Create a failover group named "group2" with the NAS service type.

```text
admin:/>create failover_group general name=group2 service_type=NAS
Command executed successfully.
```

##### System Response

None
