# create lun_workload_type general


##### Function

The **create lun_workload_type general** command is used to create a workload type for LUNs. After creating a workload type, you can choose it when you are creating LUNs. Through this method the LUN space parameter can be reasonably set.

##### Format

**create lun_workload_type general** name=? io_size=? dedup_enabled=? compression_enabled=? \[ id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Workload type name. | The value contains 1 to 31 ASCII characters,including digits, letters, underscores (_), hyphens (-), and periods (.). |
| io_size=? | Request size of the workload type. | The value can be "4KB", "8KB", "16KB", "32KB", "64KB", or ">64KB". |
| dedup_enabled=? | Whether to enable deduplication or not. | The value can be "yes" or "no", where: <br>"yes": enables deduplication.<br>"no": disables deduplication.<br> NOTE: <br>In the view of user "admin", if an effective capacity license is available, the value can only be set to "yes". If no effective capacity license is available, the value can only be set to "no".<br>In the developer mode, the value is not related to the effective capacity license. |
| compression_enabled=? | Whether to enable compression or not. | The value can be "yes" or "no", where: <br>"yes": enables compression.<br>"no": disables compression.<br> NOTE: <br>In the view of user "admin", if an effective capacity license is available, the value can only be set to "yes". If no effective capacity license is available, the value can only be set to "no".<br>In the developer mode, the value is not related to the effective capacity license. |
| id | Workload type ID. | The value ranges from 16 to 1024. |

##### Usage Guidelines

Manually assign the parameters for a workload type to be created.

##### Example

Create a workload type and set its parameters as follows:

-   "name": "test1"
-   "io_size": "8KB"
-   "dedup_enabled": "yes"
-   "compression_enabled": "yes".

```text
admin:/>create lun_workload_type general name=test1 io_size=8KB dedup_enabled=yes compression_enabled=yes
Command executed successfully.
```

##### System Response

None
