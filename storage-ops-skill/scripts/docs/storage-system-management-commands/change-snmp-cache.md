# change snmp cache


##### Function

The **change snmp cache** command is used to change the interval of updating the cache data of an SNMP cache object.

##### Format

**change snmp cache** update_time=?

##### Parameters

| Parameter   | Description                                            | Value                                                                        |
|-------------|--------------------------------------------------------|------------------------------------------------------------------------------|
| update_time | Interval of updating the data of an SNMP cache object. | The value can be 5 to 60 minutes. The default value of system is 10 minutes. |

##### Usage Guidelines

The optional interval of updating the data of the SNMP cache object is 5 to 60 minutes.

##### Example

Change the interval of updating SNMP cache data to 5 minutes.

```text
admin:/>change snmp cache update_time=5
Command executed successfully.
```

##### System Response

None
