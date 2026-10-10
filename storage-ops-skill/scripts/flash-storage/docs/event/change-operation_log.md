# change operation_log


##### Function

The **change operation_log** command is used to modify the retention policy of operation logs.

##### Format

**change operation_log** retention_days=?

##### Parameters

| Parameter      | Description                                      | Value                                                                                                                                                  |
|----------------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| retention_days | Number of days that operation logs are reserved. | The value can be "0" or an integer ranging from 90 to 365, in days. "0" indicates that the number of days for retaining operation logs is not limited. |

##### Usage Guidelines

-   When "retention_days" is set to "0", the days for retaining operation logs is not limited.
-   When "retention_days" is an integer ranging from 90 to 365, operation logs that have been retained for more than the specified period will be deleted.
-   When "retention_days" is not "0" and an event dump server is configured for the storage device, operation logs that exceed the retention period will be dumped to the server. Otherwise, operation logs that have been generated for more than the retentions days will be deleted.

##### Example

Change the number of days for retaining operation logs to 90 days.

```text

admin:/>change operation_log retention_days=90
WARNING: You are about to modify the retention days for operation logs.
This operation will delete operation logs generated before the retention days.
Suggestion: Before performing this operation, ensure that the configuration is correct.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
admin:/>

```

Change the number of days for retaining operation logs to 0.

```text
admin:/>change operation_log retention_days=0
Command executed successfully.
```

##### System Response

None
