# change recycle_bin_policy


##### Function

The change recycle_bin_policy command is used to modify parameters related to the recycle bin policy.

##### Format

**change recycle_bin_policy delay_delete_enable=***?*** \[ delay_delete_interval=***?* \]

##### Parameters

| Parameter             | Description                                            | Value                                     |
|-----------------------|--------------------------------------------------------|-------------------------------------------|
| delay_delete_enable   | Whether to enable delayed deletion in the recycle bin. | The value can be "yes" or "no".           |
| delay_delete_interval | Delayed deletion interval.                             | The value ranges from 1 to 168, in hours. |

##### Usage Guidelines

-   Run the "change recycle_bin_policy delay_delete_enable=?" command to enable or disable delayed deletion in the recycle bin.
-   Run the "change recycle\_ bin_policy delay_delete_enable=? delay_delete_interval=?" command to enable or disable delayed deletion in the recycle bin and modify the delayed deletion interval.

##### Example

Disable delayed deletion in the recycle bin.

```text
admin:/>change recycle_bin_policy delay_delete_enable=no
WARNING: You are about to perform a close recycle bin operation. After the recycle bin is closed, the objects such as Lun and snapshot will be deleted immediately, and the data cannot be retrieved in case of false deletion.
Suggestion: Please confirm if recycle bin function is required.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Enable delayed deletion in the recycle bin and modify the delayed deletion interval to 48 hours.

```text
admin:/>change recycle_bin_policy delay_delete_enable=yes delay_delete_interval=48
Command executed successfully.
```

##### System Response

None
