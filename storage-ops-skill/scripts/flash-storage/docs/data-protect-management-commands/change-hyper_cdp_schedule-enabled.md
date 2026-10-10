# change hyper_cdp_schedule enabled


##### Function

The **change hyper_cdp_schedule enabled** command is used to enable or disable a HyperCDP schedule.

##### Format

**change hyper_cdp_schedule enabled** { schedule_id_list=? } enabled=?

**change hyper_cdp_schedule enabled** { schedule_name_list=? } \[ vstore_id=? \] enabled=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id_list=? | ID list of HyperCDP schedules. | To obtain the value, run "show hyper_cdp_schedule general". The value is an integer from 1 to 512.<br>Multiple HyperCDP schedule IDs are separated by commas (,) or you can specify an ID range using a hyphen (-), such as: "1,5-"8. |
| schedule_name_list=? | List of HyperCDP schedule names. | To obtain the value, run the "show hyper_cdp_schedule general" command.<br>You can enable or disable multiple HyperCDP schedules at the same time. Use commas (,) to separate multiple HyperCDP schedule names. |
| enabled=? | Whether to enable or disable a HyperCDP schedule. | The value can be "yes" or "no", where: <br>"yes": enables a HyperCDP schedule.<br>"no": disables a HyperCDP schedule. |
| vstore_id=? | Specified vStore ID. | The value is an integer ranging from 0 to 1023. The default value is 0. |

##### Usage Guidelines

-   Before performing the operation, confirm that the schedule ID is correct and exits.
-   The built-in schedule of the file system cannot be operated by name.

##### Example

Enable the HyperCDP schedule whose ID is "3".

```text
admin:/>change hyper_cdp_schedule enabled schedule_id_list=3 enabled=yes
Change HyperCDP schedule enabled 3 successfully.
```

Disable the HyperCDP schedule whose ID is "1".

```text
admin:/>change hyper_cdp_schedule enabled schedule_id_list=1 enabled=no
WARNING: You are about to disable HyperCDP schedule. After this operation, HyperCDP objects will no longer be created based on the schedule.
Suggestion: Before performing this operation, ensure that you do not need to create HyperCDP objects anymore.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Change HyperCDP schedule disabled 1 successfully.
```

Forcibly disable the HyperCDP schedule whose ID is "1".

```text
developer:/>change hyper_cdp_schedule enabled schedule_id_list=1 enabled=no force=yes
WARNING: You are about to disable HyperCDP schedule. After this operation, HyperCDP objects will no longer be created based on the schedule.
Suggestion: Before performing this operation, ensure that you do not need to create HyperCDP objects anymore.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Change HyperCDP schedule disabled 1 successfully.
```

##### System Response

None
