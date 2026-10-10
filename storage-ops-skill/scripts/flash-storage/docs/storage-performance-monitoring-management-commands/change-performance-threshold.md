# change performance threshold


##### Function

The **change performance threshold** command is used to change the thresholds of performance statistical object parameters.

##### Format

**change performance threshold** threshold_id=? { threshold_value=? \| wave_threshold_value=? } \*

##### Parameters

| Parameter              | Description                | Value                                                                                    |
|------------------------|----------------------------|------------------------------------------------------------------------------------------|
| threshold_id=?         | Threshold ID.              | To obtain the value, run "show performance threshold", the value ranges from 0 to 65535. |
| threshold_value=?      | New anomaly threshold.     | The value ranges from 0 to 4294967295.                                                   |
| wave_threshold_value=? | New fluctuation threshold. | The value ranges from 0 to 100.                                                          |

##### Usage Guidelines

Before performing this operation, ensure that the selected threshold ID is correct.

##### Example

Change anomaly threshold "1" of performance statistical object parameters to "10".

```text
admin:/>change performance threshold threshold_id=1 threshold_value=10
Command executed successfully.
```

##### System Response

None
