# show remote_replication available_file_system


##### Function

The **show remote_replication available_file_system** command is used to query the information on available file system tasks.

##### Format

**show remote_replication available_file_system** array_type=? remote_device_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| array_type=? | Type of a remote device. | The value can be: "replication": replication type. |
| remote_device_id=? | ID of a remote device. | To obtain the value, run "show remote_device general". |

##### Usage Guidelines

None

##### Example

Query the available file system whose manufacturer type is current manufacturer and the remote device ID is 0.

```text

admin:/>show remote_replication available_file_system array_type=replication remote_device_id=0

File System ID  Name  Health Status  Device ID  Device SN             Capacity  Vendor  Model
--------------  ----  -------------  ---------  --------------------  --------  ------  -----
3               fs1   Normal         0          ST000000000000000212   1.000GB  --      --
4               fs2   Normal         0          ST000000000000000212   1.000GB  --      --

```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                             |
|----------------|-------------------------------------|
| File System ID | ID of the file system.              |
| Name           | Name of the file system.            |
| Health Status  | Health state.                       |
| Device ID      | ID of the remote device.            |
| Device SN      | Serial number of the remote device. |
| Capacity       | Capacity of the file system.        |
| Vendor         | Vendor of the remote device.        |
| Model          | Model of the remote device.         |
