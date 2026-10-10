# change event_config


##### Function

The **change event_config** command is used to configure the health check policy of the storage system.

##### Format

**change event_config** enabled=? period=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Switch of health check. | The value can be "yes" or "no", where: <br>"yes": Health check will be enabled.<br>"no": Health check will be disabled. |
| period=? | Health check period. | The value ranges from 1 to 168, expressed in hours. |

##### Usage Guidelines

Run "show event_config" to query the health check result.

##### Example

Enable the health check function and setting the check period to 80 hours.

```text
admin:/>change event_config enabled=yes period=80
Command executed successfully.
```

Query the health check result.

```text
admin:/>show event_config

Enable  Period(hours)
------  -------------
Yes     12

```

##### System Response

None
