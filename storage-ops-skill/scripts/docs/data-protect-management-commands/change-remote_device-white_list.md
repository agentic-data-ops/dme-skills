# change remote_device white_list


##### Function

The **change remote_device white_list** command is used to modify the white list of heterogeneous disk arrays.

##### Format

**change remote_device white_list** record_id=? path_selector=? fail_back=? fail_over=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| record_id=? | Record ID. | The value is an integer from 0 to 2147483647. |
| path_selector=? | Algorithm used by a storage system to select a path. | The value can be "FIX", "ROUND_ROBIN", or "LEAST_QUEUE". |
| fail_back=? | Mode used by a storage system to restore faulty links. | The value can be "FAILBACK_IMMEDIAT", "NOT_FAILBACK", or "DELAY_FAILBACK", where: <br>"FAILBACK_IMMEDIATE": Failback will be performed immediately.<br>"NOT_FAILBACK": Failback will not be performed.<br>"DELAY_FAILBACK": Failback will be postponed. |
| fail_over=? | Whether path failover is supported. | The value can be "ENABLE" or "DISABLE", where: <br>"ENABLE": enables failover.<br>"DISABLE": disables failover. |

##### Usage Guidelines

None

##### Example

Modify the white list of heterogeneous disk arrays.

```text
admin:/>change remote_device white_list record_id=59 path_selector=FIX fail_back=NOT_FAILBACK fail_over=ENABLE
Command executed successfully.
```

##### System Response

None
