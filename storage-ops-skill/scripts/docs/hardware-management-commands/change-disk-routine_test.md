# change disk routine_test


##### Function

**change disk routine_test** command is used to set the status and period for a routine disk test.

##### Format

**change disk routine_test** enable_routine_test=? \[ routine_test_period=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enable_routine_test=? | Status of a routine disk test. | The value can be "on" or "off", where: <br>"on": A routine disk test is enabled.<br>"off": A routine disk test is disabled. |
| routine_test_period=? | Period of a routine disk test. This parameter is available only when "enable_routine_test=?" is set to "on". | The value is an integer ranging from 0 to 5,256,000, expressed in minutes. |

##### Usage Guidelines

None

##### Example

Enable a routine disk test and set the test period to 60 minutes.

```text
admin:/>change disk routine_test enable_routine_test=on routine_test_period=60
Command executed successfully.
```

##### System Response

None
