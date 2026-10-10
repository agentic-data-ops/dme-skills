# create dns_zone general


##### Function

The **create dns_zone general** command is used to create a zone for the built-in DNS server.

##### Format

**create dns_zone general** zone_name=? \[ home_site_wwn=? \]

##### Parameters

| Parameter       | Description                    | Value                                                                                                                                                                                                                                                         |
|-----------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| zone_name=?     | Name of a DNS zone.            | The value contains 1 to 255 characters and consists of labels separated by periods (.). A label contains 1 to 63 characters including letters (case-insensitive), digits, hyphens (-), and underscores (\_), and must start and end with a letter or a digit. |
| home_site_wwn=? | Home site WWN of the DNS Zone. | You can run the "show system general" command in the user view to obtain the value.                                                                                                                                                                           |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Create a DNS zone named "zone1.nas.com".

```text
admin:/>create dns_zone general zone_name=zone1.nas.com
Command executed successfully.
```

##### System Response

None
