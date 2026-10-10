# delete hyper_cdp_schedule


##### Function

The **delete hyper_cdp_schedule** command is used to delete HyperCDP schedules.

##### Format

**delete hyper_cdp_schedule** { schedule_id_list=? }

**delete hyper_cdp_schedule** { schedule_name_list=? } \[ vstore_id=? \]

##### Parameters

| Parameter            | Description                      | Value                                                                                                                                                                                          |
|----------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| schedule_id_list=?   | ID of a HyperCDP schedule.       | To obtain the value, run "show hyper_cdp_schedule general". You can specify multiple HyperCDP schedule IDs separated by commas (,), or an ID range separated by hyphens (-), such as: "1,5-8". |
| schedule_name_list=? | List of HyperCDP schedule names. | You can run the show hyper_cdp_schedule general command to obtain the value. You can specify multiple HyperCDP schedules. Use commas (,) to separate multiple HyperCDP schedule names.         |
| vstore_id=?          | Specified vStore ID.             | The value is an integer ranging from 0 to 1023. The default value is 0.                                                                                                                        |

##### Usage Guidelines

-   Before performing the operation, confirm that the schedule ID is correct and exits.
-   The built-in schedule of the file system cannot be operated by name.

##### Example

Delete HyperCDP schedules whose IDs are "1", "5", and "6".

```text
admin:/>delete hyper_cdp_schedule schedule_id_list=1,5-6
WARNING: You are about to delete the HyperCDP schedule. This operation will remove information about the HyperCDP schedule from the system.
Suggestion: Before performing this operation, ensure that the HyperCDP schedule can be deleted.
Have you read warning message carefully?(y/n)y

Are you sure really want to perform the operation?(y/n)y
Delete HyperCDP schedule 1 successfully.
Delete HyperCDP schedule 5 successfully.
Delete HyperCDP schedule 6 successfully.
```

##### System Response

None
