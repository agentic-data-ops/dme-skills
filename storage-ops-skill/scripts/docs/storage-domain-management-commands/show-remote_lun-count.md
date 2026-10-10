# show remote_lun count


##### Function

The **show remote_lun count** command is used to query the number of LUNs in a remote device.

##### Format

**show remote_lun count** array_type=? \[ remote_device_id=? \] \[ link_type=? \] \[ link_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| array_type=? | Type of a remote device. | The value can be "replication" or "heterogeneity", where: <br>"replication": The remote device is made by Huawei.<br>"heterogeneity": The remote device is made by a third-party manufacturer. |
| remote_device_id=? | ID of a remote device. | To obtain the value, run "show remote_device general". |
| link_type=? | Link type. | The value can be "FC" or "iSCSI", where: <br>"FC": A remote device is connected to a local device by Fibre Channel links.<br>"iSCSI": A remote device is connected to a local device by iSCSI links. |
| link_id=? | Link ID. | To obtain the value, run the "show remote_device link" or "show remote_device elink" command without parameters. |

##### Usage Guidelines

-   If the "link_type" parameter is specified, the "link_id" parameter is mandatory.
-   The following parameters or parameter sets are mutually exclusive: "link_type" and "remote_device_id".

##### Example

Query the number of LUNs in the remote device whose ID is "0".

```text
admin:/>show remote_lun count array_type=replication remote_device_id=0
Remote Lun Count
----------------
8
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                |
|------------------|------------------------|
| Remote Lun Count | Number of remote LUNs. |
