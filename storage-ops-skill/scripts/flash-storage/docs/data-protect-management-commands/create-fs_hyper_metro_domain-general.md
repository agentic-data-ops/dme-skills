# create fs_hyper_metro_domain general


##### Function

The **create fs_hyper_metro_domain general** command is used to create a file system-based HyperMetro domain.

##### Format

**create fs_hyper_metro_domain general** remote_device_id=? name=? \[ work_mode=? \] \[ description=? \] \[ is_share_authentication_sync=? \] \[ is_network_sync=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_device_id=? | ID of the remote storage device. | To obtain the value, run the "show remote_device general" command. |
| name=? | File system-based HyperMetro domain name. | The value contains 1 to 31 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.), and must start with a digit or a letter. |
| description=? | Description. | The value contains 1 to 127 letters. |
| work_mode=? | Working mode of the file system HyperMetro domain. | The options are as follows: <br>"hypermetro": active-active mode.<br>"synchronous": synchronous mode. |
| is_share_authentication_sync=? | Whether to synchronize shared authentication information. | - |
| is_network_sync=? | Whether to synchronize network configurations. | - |

##### Usage Guidelines

None

##### Example

Create a file system HyperMetro domain. Set the remote device ID to "1" and name to "domainA".

```text
admin:/>create fs_hyper_metro_domain general remote_device_id=1 name=domainA work_mode=hypermetro
Command executed successfully.
```

##### System Response

None
