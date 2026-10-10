# change lun_clone split


##### Function

The **change lun_clone split** command is used to start and stop splitting a clone pair or modify the split speed of a clone pair.

##### Format

**change lun_clone split** clone_id=? { action=? \| split_speed=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| clone_id | Clone pair ID. | Run "show lun_clone general" to obtain the value. |
| split_speed | Split speed. | The value can be "low", "middle", "high", or "highest", where: <br>"low": indicates the low speed.<br>"middle": indicates the medium speed.<br>"high": indicates the high speed.<br>"highest": indicates the highest speed.<br> The default value is "middle". |
| action | Split action. | The value can be "start" or "stop", where: <br>"start": starts splitting.<br>"stop": stops splitting. |

##### Usage Guidelines

-   Before running this command, ensure that the selected clone pair is exactly the one you want to split.
-   You can split a clone pair that is in the online state only. To query the status of a clone pair, run "show lun_clone general".

##### Example

Split clone pair "7" at the medium split speed.

```text
admin:/>change lun_clone split clone_id=7 action=start split_speed=middle
DANGER: You are about to split the clone pair. This operation may occupy extra memory.
Suggestion: Before performing this operation, ensure that the ID of the selected LUN clone is correct.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
