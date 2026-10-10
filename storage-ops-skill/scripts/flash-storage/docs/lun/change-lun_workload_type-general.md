# change lun_workload_type general


##### Function

The **change lun_workload_type general** command is used to modify the settings of an application type, including the name, I/O size, and so on.

##### Format

**change lun_workload_type general** id=? { name=? \| io_size=? \| dedup_enabled=? \| compression_enabled=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| id=? | Application type ID. | To obtain the value, press "Ctrl+A" or run the "show lun_workload_type general" command without parameters. The value ranges from 16 to 1024. |
| name=? | New application type name. | The value contains 1 to 31 ASCII characters,including digits, letters, underscores (_), hyphens (-), and periods (.). |
| io_size=? | Request size of the application type. | The value can be "4KB", "8KB", "16KB", "32KB", "64KB", or "64KB". |
| compression_enabled=? | Whether to enable compression or not. | The value can be "yes" or "no", where: <br>"yes": enables compression.<br>"no": disables compression.<br> NOTE: <br>In the view of user "admin", if an effective capacity license is available, the value can only be set to "yes". If no effective capacity license is available, the value can only be set to "no".<br>In the developer mode, the value is not related to the effective capacity license. |
| dedup_enabled=? | Whether to enable deduplication or not. | The value can be "yes" or "no", where: <br>"yes": enables deduplication.<br>"no": disables deduplication.<br> NOTE: <br>In the view of user "admin", if an effective capacity license is available, the value can only be set to "yes". If no effective capacity license is available, the value can only be set to "no".<br>In the developer mode, the value is not related to the effective capacity license. |

##### Usage Guidelines

-   Before running this command, ensure that the selected application type is exactly the one you want to modify.
-   Before running this command (not to change names), ensure that no LUN uses the workload type.

##### Example

Change the I/O size of the application type whose ID is "16" to "16KB", and enable deduplication and compression.

```text
admin:/>change lun_workload_type general id=16 io_size=16KB dedup_enabled=yes compression_enabled=yes
Command executed successfully.
```

##### System Response

None
