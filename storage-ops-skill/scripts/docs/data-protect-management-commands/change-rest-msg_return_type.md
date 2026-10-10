# change rest msg_return_type


##### Function

The **change rest msg_return_type** command is used to change the command output returning mode of REST interfaces to synchronous or asynchronous.

##### Format

**change rest msg_return_type** type=?

##### Parameters

| Parameter | Description                                       | Value                                             |
|-----------|---------------------------------------------------|---------------------------------------------------|
| type=?    | Command output returning mode of REST interfaces. | The value can be "asynchronize" or "synchronize". |

##### Usage Guidelines

None

##### Example

Change the command output returning mode of REST interfaces to "synchronize".

```text
admin:/>change rest msg_return_type type=synchronize
DANGER:You are about to change the return type of REST interfaces.
This operation will cause the DeviceManager unavailable temporarily.
Suggestion: Before performing this operation, ensure that all users have exited the DeviceManager.Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the command output returning mode of REST interfaces to "asynchronize".

```text
admin:/>change rest msg_return_type type=asynchronize
DANGER:You are about to change the return type of REST interfaces.
This operation will cause the DeviceManager unavailable temporarily.
Suggestion: Before performing this operation, ensure that all users have exited the DeviceManager.Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
