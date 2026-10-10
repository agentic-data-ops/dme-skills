# change performance retention_strategy


##### Function

The **change performance retention_strategy** command is used to set the retention policy for performance data.

##### Format

**change performance retention_strategy** { storage_duration=? \| retention_switch=? } \*

**change performance retention_strategy** is_delete_performance_data=?

**change performance retention_strategy** storage_pool_id=? storage_duration=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| storage_pool_id=? | ID of the storage pool for storing performance data. This parameter can be set only once and cannot be changed once being set. | The value ranges from 0 to 63. |
| storage_duration=? | Performance data retention duration. | The value ranges from 1 to 3 years. |
| retention_switch=? | Whether to retain performance data. | The value can be "on" or "off", where: <br>"on": enables performance data retention.<br>"off": disables performance data retention. |
| is_delete_performance_data=? | Whether to delete performance data. | The value can be "yes" or "on", where: <br>"yes": deletes performance data.<br>"no": does not delete performance data. |

##### Usage Guidelines

-   This command is a combined one and can be executed to configure, modify, and delete the performance data storage space.
-   When this command is used for configuring the storage space, the command is an asynchronous one. Parameters "storage_pool_id" and "storage_duration" are mandatory. When the storage space is configured, a message indicating a parameter error is displayed if the configuration command is executed repeatedly.
-   When this command is used for modifying the storage space, the command is a synchronous one. At least one of parameters "storage_duration" and "retention_switch" must be entered (after the storage space is configured, parameter "storage_pool_id" cannot be modified). When the storage space is not configured, a message indicating a parameter error is displayed if the modification command is executed.
-   When this command is used for deleting the storage space, the command is an asynchronous one. Parameter "is_delete_performance_data" is mandatory.

##### Example

Create a storage space for performance data. Set the retention period to 1 year. The performance data storage space can be created only once and the storage pool ID cannot be changed once being set.

```text
admin:/>change performance retention_strategy storage_pool_id=0 storage_duration=1
Command executed successfully.
```

Update the duration for performance data retention to 2 years.

```text
admin:/>change performance retention_strategy storage_duration=2
Command executed successfully.
```

Switch on performance data retention.

```text
admin:/>change performance retention_strategy retention_switch=on
Command executed successfully.
```

Delete performance data.

```text
admin:/>change performance retention_strategy is_delete_performance_data=yes
DANGER: You are about to release the space for storing performance data. After this operation, performance data will be deleted and cannot be restored, new historical performance data will not be generated, and historical performance data cannot be viewed or exported.
Suggestion: Before performing this operation, ensure that the historical performance data is no longer needed.
Have you read danger alert message carefully(y/n)y
Are you sure you really want to perform the operation(y/n)y
Command executed successfully.
```

##### System Response

None
