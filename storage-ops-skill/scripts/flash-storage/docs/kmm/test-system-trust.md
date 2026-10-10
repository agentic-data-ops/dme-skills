# test system trust


##### Function

This **test system trust** command is used to test whether the system can be trusted and show the test result to users.

##### Format

**test system trust** \[ controller_id=? \]

##### Parameters

| Parameter     | Description    | Value                                                                                         |
|---------------|----------------|-----------------------------------------------------------------------------------------------|
| controller_id | Controller ID. | For example, 0A or 1C. You can run the "show controller general" command to obtain the value. |

##### Usage Guidelines

None

##### Example

Test whether the system can be trusted and show the test result to users.

```text
admin:/>test system trust
WARNING: You are about to test whether the system can be trusted. This process takes a few minutes.
Suggestion: Before performing this operation, confirm that you need to test whether the system can be trusted.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Controller ID   Test Result
-------------   -----------
0A              Trusted
0B              Untrusted
0C              Cannot be determined
0D              Trusted
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                              |
|---------------|------------------------------------------------------|
| Controller ID | Controller ID.                                       |
| Test Result   | Result of testing whether the system can be trusted. |
