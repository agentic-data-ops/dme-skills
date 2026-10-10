# change hyper_copy general


##### Function

The **change hyper_copy general** command is used to modify HyperCopy pair settings.

##### Format

**change hyper_copy general** hyper_copy_id=? \[ copy_speed=? \] \[ name=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| hyper_copy_id | ID of a HyperCopy pair that you want to modify its settings. | The value is an integer ranging from 0 to 65535. |
| copy_speed | Copy speed. | The value can be "low", "middle", "high", or "highest", where: <br>"low": indicates the low speed.<br>"middle": indicates the medium speed.<br>"high": indicates the high speed.<br>"highest": indicates the highest speed. |
| name | New name of a HyperCopy pair. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| description | Description. | - |

##### Usage Guidelines

None

##### Example

Change the copy speed of HyperCopy pair "1" to "high".

```text
admin:/>change hyper_copy general hyper_copy_id=1 copy_speed=high
WARNING: You are about to change the copy rate of HyperCopy pair  to the high or highest speed. This operation may cause heavy service pressure and decrease the read/write performance of the host.
Suggestion: Perform this operation during off-peak hours.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
