# show performance retention_strategy


##### Function

The **show performance retention_strategy** command is used to query the retention policy for performance data.

##### Format

**show performance retention_strategy**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the retention policy for performance data.

```text
admin:/>show performance retention_strategy
Storage Pool ID : 0
Storage Duration : 2 Years
Retention Switch : on
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Storage Pool ID  | ID of the storage pool for storing performance data. This parameter can be set only once and cannot be changed once being set. |
| Storage Duration | Data retention duration.                                                                                                       |
| Retention Switch | Whether to retain performance data.                                                                                            |
