# scan remote_lun


##### Function

The **scan remote_lun** command is used to scan for LUNs on a third-party storage system. When a LUN mapping is added to or deleted from a remote disk array, or an initiator is added to or deleted from a host group, you must manually run this command.

##### Format

**scan remote_lun** \[ remote_device_id=? \] \[ link_type=? \] \[ link_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_device_id=? | ID of a remote device. | To obtain the value, run "show remote_device general". |
| link_type=? | Link type. | The value can be "FC" or "iSCSI", where: <br>"FC": A remote device is connected to a local device by Fibre Channel links.<br>"iSCSI": A remote device is connected to a local device by iSCSI links. |
| link_id=? | Link ID. | To obtain the value, run the "show remote_device link" or "show remote_device elink" command without parameters. |

##### Usage Guidelines

When the LUN mapping of a remote disk array changes, the local disk array cannot sense the change. You need to manually scan for LUNs on the local storage system and update the LUN mapping change of the remote disk array in a timely manner. Therefore, when a LUN mapping is added to or deleted from a remote disk array, or an initiator is added to or deleted from a host group, you must manually run this command.

##### Example

Scan for LUNs on a third-party storage system.

```text
admin:/>scan remote_lun
Command executed successfully.
```

##### System Response

None
