# change system timezone


##### Function

The **change system timezone** command is used to change the time zone where the storage system resides in. If the displayed time zone is different from the actual local time zone, you can run this command to change the time zone.

##### Format

**change system timezone** continent=? capital=?

##### Parameters

| Parameter   | Description                                                                      | Value                                                                                                                                            |
|-------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| continent=? | General area (continent or region) where the storage system resides.             | The value can be "Africa", "America", "Antarctica", "Arctic", "Asia", "Atlantic", "Australia", "Etc", "Europe", "Indian", "Pacific", or "other". |
| capital=?   | Specific area (major city, province, or state) where the storage system resides. | The value varies depending on the "continent=?" parameter. Refer to the information displayed in the CLI.                                        |

##### Usage Guidelines

-   If the storage system's time zone is changed incorrectly, the scheduled tasks and the maintenance engineers' work are adversely affected.
-   Before running this command, check whether the time zone you want to set is correct.

##### Example

Change the storage system's time zone to "Asia/Shanghai".

```text
admin:/>change system timezone continent=Asia capital=Shanghai
WARNING: You are about to change the system time zone. This operation may affect licenses, alarms, performance monitoring, certificates, and CallHome data backhaul.
Suggestion: Before performing this operation, ensure that the time zone needs to be changed. Do not perform this operation during system upgrade.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
