# delete notification trap


##### Function

The **delete notification trap** command is used to delete a trap server.

##### Format

**delete notification trap** server_id=?

##### Parameters

| Parameter   | Description            | Value                                                                 |
|-------------|------------------------|-----------------------------------------------------------------------|
| server_id=? | ID of the trap server. | To obtain the value, run "show notification trap" without parameters. |

##### Usage Guidelines

After the trap server is deleted, the corresponding application sever or maintenance terminal cannot receive alarm information from the storage system.

##### Example

To delete the trap server whose ID is "1".

```text
admin:/>delete notification trap server_id=1
WARNING: You are about to delete Trap IP address. After this operation, the corresponding Trap Server cannot receive alarms from the current device.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
