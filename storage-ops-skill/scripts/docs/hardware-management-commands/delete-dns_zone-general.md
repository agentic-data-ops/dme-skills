# delete dns_zone general


##### Function

The **delete dns_zone general** command is used to delete a specified zone.

##### Format

**delete dns_zone general** zone_name=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| zone_name=? | Zone name. | The value contains 1 to 255 characters and consists of labels separated by periods (.). A label contains 1 to 63 characters including letters (case-insensitive), digits, hyphens (-), and underscores (_), and must start and end with a letter or a digit.<br>To obtain the value, run the "show dns_zone general" command without parameters. |

##### Usage Guidelines

-   Run the "show dns_zone general" command to view the zone name.
-   Run the "**delete dns_zone general** zone_name=?" command to delete a specified zone.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Delete a specified zone.

```text
admin:/>delete dns_zone general zone_name=zone1.nas.com
DANGER: You are about to delete a DNS Zone. This operation will cause the failure in accessing services by using this Zone name.
Suggestion: Before performing this operation, confirm that you have selected the correct Zone name and will not use this Zone name to access services any more.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
