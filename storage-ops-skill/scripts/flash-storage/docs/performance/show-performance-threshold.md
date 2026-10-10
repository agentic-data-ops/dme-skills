# show performance threshold


##### Function

The **show performance threshold** command is used to query the thresholds of performance statistical object parameters.

##### Format

**show performance threshold** \[**threshold_id=***?*\]

##### Parameters

| Parameter      | Description   | Value                                                                                                                                                                                                                       |
|----------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| threshold_id=? | Threshold ID. | To obtain the value, run "**show performance threshold**", the value ranges from 0 to 65535. |

##### Usage Guidelines

None

##### Example

Query threshold "1" of performance statistical object parameters.

```text
admin:/>show performance threshold threshold_id=1
ID  Statistical Object  Statistical Item                      Threshold  Wave Threshold
--  ------------------  ------------------------------------  ---------  --------------
1   CONTROLLER          Average Write I/O Latency(us)         20000      10
```

Query thresholds of all the performance statistical object parameters.

```text
admin:/>show performance threshold
ID  Statistical Object  Statistical Item                      Threshold  Wave Threshold
--  ------------------  ------------------------------------  ---------  --------------
0   CONTROLLER          Average Read I/O Latency(us)          50000      10
1   CONTROLLER          Average Write I/O Latency(us)         20000      10
2   LUN                 Average Read I/O Latency(us)          50000      10
3   LUN                 Average Write I/O Latency(us)         20000      10
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                         |
|--------------------|---------------------------------|
| ID                 | Threshold ID.                   |
| Statistical Object | Performance statistical object. |
| Statistical Item   | Type of performance statistics. |
| Threshold          | Anomaly threshold.              |
| Wave Threshold     | Fluctuation threshold.          |
