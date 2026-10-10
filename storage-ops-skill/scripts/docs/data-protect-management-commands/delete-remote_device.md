# delete remote_device


##### Function

The **delete remote_device** command is used to delete a specific remote device. When the forcible deletion flag is set to "TRUE", this command can be used to forcibly delete a remote device.

##### Format

**delete remote_device** remote_device_id=? \[ is_force_delete_dev=? \]

##### Parameters

| Parameter          | Description            | Value                                                  |
|--------------------|------------------------|--------------------------------------------------------|
| remote_device_id=? | ID of a remote device. | To obtain the value, run "show remote_device general". |

##### Usage Guidelines

-   Running this command erases information about the selected remote device from the storage system.
-   Before running this command, ensure that the selected remote device is exactly the one you want to delete.
-   Before forcibly deleting a remote device, confirm that the forcible deletion is necessary.

##### Example

Delete the remote device whose ID is "0".

```text
admin:/>delete remote_device remote_device_id=0
WARNING: You are going to remove remote device. This operation deletes the information about the remote device from the system.
Suggestion: Before you perform this operation, ensure that you have selected the correct remote device, which is considered unnecessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
