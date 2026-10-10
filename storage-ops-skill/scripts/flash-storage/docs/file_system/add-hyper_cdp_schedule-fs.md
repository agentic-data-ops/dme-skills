# add hyper_cdp_schedule fs


##### Function

The **add hyper_cdp_schedule fs** command is used to add file systems to a HyperCDP schedule.

##### Format

**add hyper_cdp_schedule fs** schedule_id=? file_system_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schedule_id=? | HyperCDP schedule ID. | To obtain the value, run "show hyper_cdp_schedule general". |
| file_system_id_list=? | ID list of the file systems to be added. | To obtain the value, run "show fs general".<br>You can specify multiple file systems IDs separated by commas (,) or an ID range using hyphens (-), such as: 0,5-8. |

##### Usage Guidelines

After you add file systems to a HyperCDP schedule, the HyperCDP schedule will take effect for the added file systems.

##### Example

Add file systems whose IDs are "0", "5", and "6" to the HyperCDP schedule whose ID is "1".

```text
admin:/> add hyper_cdp_schedule fs schedule_id=1 file_system_id_list=0,5-6
Add HyperCDP schedule fs successfully.
Add HyperCDP schedule fs 5 successfully.
Add HyperCDP schedule fs 6 successfully.
```

##### System Response

None
