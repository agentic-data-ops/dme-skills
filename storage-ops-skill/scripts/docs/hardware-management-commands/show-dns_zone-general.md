# show dns_zone general


##### Function

The **show dns_zone general** command is used to query zone information about the built-in DNS server.

##### Format

**show dns_zone general**

##### Parameters

None

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the zone configured for the built-in DNS server.

```text
admin:/>show dns_zone general
Zone ID  Zone Name      vStore ID  Home Site WWN
-------  -------------  ---------  -------------
0        zone1.nas.com  --         XXXX
1        zone2.nas.com  --         XXXX
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                                         |
|---------------|---------------------------------------------------------------------------------|
| Zone ID       | ID of the zone configured for the built-in DNS server.                          |
| Zone Name     | Name of the zone configured for the built-in DNS server.                        |
| vStore ID     | ID of the vStore where the zone configured for the built-in DNS server belongs. |
| Home Site WWN | WWN of the home site configured for the built-in DNS server.                    |
