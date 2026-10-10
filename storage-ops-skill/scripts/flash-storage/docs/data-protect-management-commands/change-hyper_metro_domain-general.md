# change hyper_metro_domain general


##### Function

The **change hyper_metro_domain general** command is used to change the information about HyperMetro.

##### Format

**change hyper_metro_domain general** domain_id=? { name=? \| description=? \| is_arb_opt_switch=? } \*

##### Parameters

| Parameter     | Description                    | Value                                                                                                                                                            |
|---------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| domain_id=?   | ID of the HyperMetro domain.   | Run the "show hyper_metro_domain general" command to obtain the value.                                                                                           |
| name=?        | Name of the HyperMetro domain. | The value contains 1 to 31 ASCII characters, including digits, letters, underscores (\_), hyphens (-), and periods (.), can only start with a digit or a letter. |
| description=? | Description information.       | The value contains 1 to 127 letters.                                                                                                                             |

##### Usage Guidelines

None

##### Example

Change the domain name to "domainA" whose domain ID is "1".

```text
admin:/>change hyper_metro_domain general domain_id=1 name=domainA
Command executed successfully.
```

##### System Response

None
