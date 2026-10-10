# change dns_zone general


##### Function

The **change dns_zone general** command is used to modify the name a DNS zone.

##### Format

**change dns_zone general** zone_name=? new_name=?

##### Parameters

| Parameter   | Description                                                                                                                                                                                            | Value                                                                                                                                                                                                                                                         |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| zone_name=? | Name of a DNS zone. This parameter is not supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value contains 1 to 255 characters and consists of labels separated by periods (.). A label contains 1 to 63 characters including letters (case-insensitive), digits, hyphens (-), and underscores (\_), and must start and end with a letter or a digit. |
| new_name    | New name of the DNS zone.                                                                                                                                                                              | The value contains 1 to 255 characters and consists of labels separated by periods (.). A label contains 1 to 63 characters including letters (case-insensitive), digits, hyphens (-), and underscores (\_), and must start and end with a letter or a digit. |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Change the name of a DNS zone.

```text
admin:/>change dns_zone general zone_name=zone1.nas.com new_name=zone2.nas.com
DANGER: You are about to modify properties of a DNS Zone. This operation may cause you to fail to access services by using the Zone name before modification.
Suggestion: Before performing this operation, confirm that the modification is necessary.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
