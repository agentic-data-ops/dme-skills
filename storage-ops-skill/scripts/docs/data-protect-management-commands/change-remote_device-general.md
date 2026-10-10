# change remote_device general


##### Function

The **change remote_device general** command is used to modify the name and link of remote devices.

##### Format

**change remote_device general** remote_device_id=? \[ bandwidth_switch=? \] \[ compress_algorithm=? \] \[ compress_judge=? \] { link_type=? link_id=? \| local_eth_logical_port=? remote_ip=? } \[ local_rep_port_group_id=? \] \[ local_rep_port_group_name=? \] \[ name=? \] \[ remote_rep_port_group_id=? \] \[ remote_rep_port_group_name=? \] \[ transport_optimize=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_device_id=? | ID of a remote device. | To obtain the value, run "show remote_device general". |
| name=? | Updated name of a remote device. | The value contains 1 to 31 characters, including letters, digits, hyphens (-), underscores (_), and periods (.). |
| compress_algorithm=? | Compression level to be set. | The value can be "fast" or "deep", where: <br>"fast": highest performance.<br>"deep": best compression.<br> The default value is "deep". |
| compress_judge=? | Whether to enable SmartCompression. | The value can be "yes" or "no", where: <br>"yes": enables SmartCompression.<br>"no": disables SmartCompression.<br> The default value is yes. |
| link_type=? | Link type. | The options are as follows: <br>"FC": The remote device is connected to the local device through a Fibre Channel link.<br>"IP": The remote device is connected to the local device through an IP link. |
| link_id=? | ID of a Fibre Channel link. This parameter is valid only when "link_type=?" is set to "FC". | To obtain the value, run "show remote_device link". |
| local_eth_logical_port=? | Name of the logical port. This parameter is valid only when "link_type=?" is set to "IP". | To obtain the value, run "show logical_port general". |
| remote_ip=? | IP address of a remote device. This parameter is valid only when "link_type=?" is set to "IP". | - |
| local_rep_port_group_name=? | Name of the local port group. | To obtain the value, run "show rep_port_group general". |
| remote_rep_port_group_name=? | Name of a remote port group. | To obtain the value, run "show rep_port_group general". |
| local_rep_port_group_id=? | ID of the local port group used by the remote device. | To obtain the value, run "show rep_port_group general". |
| remote_rep_port_group_id=? | ID of the remote port group used by the remote device. | To obtain the value, run "show rep_port_group general". |
| bandwidth_switch=? | Whether to enable flow control on the remote device. When this function is enabled, the total bandwidth occupied by background I/Os sent by the local storage array is controlled. | The options are as follows: <br>"on": enables bandwidth control.<br>"off": disables bandwidth control. |
| bandwidth_value=? | Bandwidth of the remote device (upper limit of the background I/O sending bandwidth of the local storage array). This parameter is valid only when bandwidth_switch is set to ON. This parameter is invalid when bandwidth_switch is set to OFF. | The value is in the format Number + Unit. The unit can be KB, MB, or GB.<br>The value ranges from 1 MB to 100 GB. |
| transport_optimize=? | Whether to enable IP link optimization. | "yes": IP link optimization is enabled.<br>"no": IP link optimization is disabled. |

##### Usage Guidelines

Description of accounts used for communication authentication between remote devices:

-   You need to create an authentication account on remote devices rather than local devices.
-   The authentication account must be a remote device administrator. Run the "create user" command to create one and set the role ID to "12".

##### Example

Rename the remote device whose ID is "513" to "newname001".

```text
admin:/>change remote_device general remote_device_id=513 name=newname001
Command executed successfully.
```

Modify the compression level of the remote device whose ID is "1" to "deep" and the intelligent compression switch to "yes".

```text
admin:/>change remote_device general remote_device_id=1 compress_algorithm=deep compress_judge=yes
Command executed successfully.
```

Enable bandwidth control for the remote device whose ID is "0" and set the bandwidth to 1 MB.

```text
admin:/>change remote_device general remote_device_id=0 bandwidth_switch=on bandwidth_value=1MB
CAUTION: You are about to enable bandwidth control for the remote device.
This operation will control the bandwidth of background I/Os sent by the local storage array. If the threshold is too low, the replication duration may be long or replication services may be interrupted.
Suggestion: Before performing this operation, ensure that the set bandwidth upper limit meets the background I/O bandwidth requirements of replication services.
Command executed successfully.
```

##### System Response

None
