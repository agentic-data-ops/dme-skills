# remove hyper_cdp_schedule fs


##### Function

The **remove hyper_cdp_schedule fs** command is used to remove file systems from a HyperCDP schedule.

##### Format

**remove hyper_cdp_schedule fs** schedule_id=? file_system_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id=? | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". |
| file_system_id_list=? | ID list of the file systems to be removed. | To obtain the value, run "show file_system general".<br>You can specify multiple file system IDs separated by commas (,) or an ID range separated by hyphens (-), such as: 0,5-8. |

##### Usage Guidelines

-   Before performing the operation, confirm that the HyperCDP schedule ID is correct and exists.
-   Before performing the operation, confirm that the file system IDs are correct and exist.

##### Example

Remove the file system whose ID is "2" from the HyperCDP schedule whose ID is "2".

```text
admin:/>remove hyper_cdp_schedule fs schedule_id=2 file_system_id_list=2
WARNING: You are about to remove file system from HyperCDP schedule, which cannot be undone. This operation will delete the relationship between the file system and the HyperCDP schedule.
Suggestion: Before performing this operation, ensure that you have correctly selected the file system to be removed.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove HyperCDP schedule fs 2 successfully.
```

##### System Response

None
