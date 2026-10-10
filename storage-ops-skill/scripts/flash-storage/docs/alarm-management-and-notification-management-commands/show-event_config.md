# show event_config


##### Function

The **show event_config** is used to query the health check policy of the storage system.

##### Format

**show event_config**

##### Parameters

None

##### Usage Guidelines

Run the "change event_config" to modify the health check policy of the storage system.

##### Example

Query the health check policy of the storage system.

```text
admin:/>show event_config

Enable  Period(hours)
------  -------------
Yes     12
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                 |
|---------------|-------------------------|
| Enable        | Switch of health check. |
| Period(hours) | Health check period.    |
