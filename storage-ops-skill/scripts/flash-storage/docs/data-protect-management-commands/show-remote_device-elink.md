# show remote_device elink


##### Function

The **show remote_device elink** command is used to query information about the heterogeneous links connected to a storage system.

##### Format

**show remote_device elink** \[ link_type=? \] \[ link_id=? \] \[ remote_device_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| link_type=? | Link type. | The value can be "FC" or "iSCSI", where: <br>"FC": A remote device is connected to a local device by Fibre Channel links.<br>"iSCSI": A remote device is connected to a local device by iSCSI links. |
| link_id=? | Link ID. | To obtain the value, run the "show remote_device elink" command without parameters. |
| remote_device_id=? | ID of a remote device. | To obtain the value, run the "show remote_device general" command. |

##### Usage Guidelines

-   The "link_id" parameter can be set only when the "link_type" is set.
-   The following parameters or parameter sets are mutually exclusive: "link_id" and "remote_device_id".
-   Run the "**show remote_device elink**" command to query the information about all links connected to the storage system.
-   Run the "**show remote_device elink** link_type=? link_id=?" command to query the information about a specified link.
-   Run the "**show remote_device elink** remote_device_id=?" command to query the information about links on a specified remote device.

##### Example

Query information about heterogeneous links whose type is "FC" and ID is "514".

```text
admin:/>show remote_device elink link_type=FC remote_device_id=514
ID Health Status Running Status Local Controller Remote Device Type
--------- ------------- -------------- ---------------- ----------
268435456 Normal Link Up 0A Heterogeneity
268435457 Normal Link Up 0B Heterogeneity
268435458 Normal Link Up 0A Heterogeneity
268435459 Normal Link Up 0B Heterogeneity
In Remote Device Remote Device ID Remote Device WWN Remote Controller
------------ ---------------- ----------------- -----------------
Yes 514 a1003300 --
Yes 514 a1003300 --
Yes 514 a1003300 --
Yes 514 a1003300 --

```

##### System Response

The following table describes the parameter meanings.

| Parameter               | Meaning                                                  |
|-------------------------|----------------------------------------------------------|
| ID                      | ID of the heterogeneous link.                            |
| Health Status           | Health status of the heterogeneous link.                 |
| Running Status          | Running status of the heterogeneous link.                |
| Local Controller        | ID of the local controller.                              |
| Remote Device Type      | Type of the remote device.                               |
| In Remote Device        | Whether the remote device is connected to the system.    |
| Remote Device ID        | ID of the remote device.                                 |
| Remote Device WWN       | WWN of the remote device.                                |
| Remote Controller       | ID of the remote controller.                             |
| Local Port ID           | Local port to which the link belongs.                    |
| Local Port WWPN         | WWPN of the local port.                                  |
| Remote Device Name      | Name of the remote device to which the link belongs.     |
| Remote Port ID          | Remote port to which the link belongs.                   |
| Remote Port WWPN        | WWPN of the remote port.                                 |
| Bandwidth Limit Enabled | Whether flow control is enabled for the link.            |
| Bandwidth Limit Size    | Flow control bandwidth.                                  |
| Bandwidth Utilization   | Bandwidth usage.                                         |
| Remote Device SN        | SN of the remote device to which the link belongs.       |
| Vendor                  | Vendor of the remote device.                             |
| Model                   | Product model of the remote device.                      |
| LUN Number              | Number of LUNs.                                          |
| Initiator Name          | iSCSI initiator name.                                    |
| Target Name             | iSCSI target name.                                       |
| Target IP               | IP address of the iSCSI target.                          |
| Target Port             | Port of the iSCSI target.                                |
| Chap Enabled            | Whether CHAP authentication is enabled.                  |
| Chap User               | CHAP user.                                               |
| Recovery Policy         | Recovery policy.                                         |
| Local IP                | IP address of the iSCSI initiator.                       |
| Local ISID              | iSCSI initiator session identifier of the local device.  |
| Remote TGPT             | Port group label of the iSCSI target on a remote device. |
