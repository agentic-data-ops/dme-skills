# change fs_hyper_metro_domain general


##### Function

The **change fs_hyper_metro_domain general** command is used to modify HyperMetro domain information.

##### Format

**change fs_hyper_metro_domain general** domain_id=? { name=? \| description=? } \*

##### Parameters

| Parameter     | Description                         | Value                                                                                                                                                          |
|---------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| domain_id=?   | HyperMetro domain ID.               | To obtain the value, run the "show fs_hyper_metro_domain general" command.                                                                                     |
| name=?        | HyperMetro domain name.             | The value contains 1 to 31 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.), and must start with a digit or letter. |
| description=? | Description of a HyperMetro domain. | A string of 1 to 127 characters.                                                                                                                               |

##### Usage Guidelines

OceanStor Dorado 3000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Change the name of the HyperMetro domain whose ID is "1" to "domainA".

```text
admin:/>change fs_hyper_metro_domain general domain_id=1 name=domainA
Command executed successfully.
```

##### System Response

None
