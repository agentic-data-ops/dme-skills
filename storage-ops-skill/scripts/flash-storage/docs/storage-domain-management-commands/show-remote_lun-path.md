# show remote_lun path


##### Function

The **show remote_lun path** command is used to query information about the paths on a remote LUN.

##### Format

**show remote_lun path** \[ path_id=? \] \[ remote_lun_wwn=? \]

##### Parameters

| Parameter        | Description              | Value                                                                                                                                                                                                          |
|------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| path_id=?        | Path ID on a remote LUN. | To obtain the value, run the "**show remote_lun path** remote_lun_wwn=?" command. |
| remote_lun_wwn=? | WWN of a remote LUN.     | To obtain the value, run the "show remote_lun general" command.                                                                                                                                                |

##### Usage Guidelines

The following parameters or parameter sets are mutually exclusive: "path_id" and "remote_lun_wwn".

##### Example

Query information about a path on a remote LUN whose WWN is "60:02:2a:11:00:0b:5a:26:06:37:28:12:00:00:00:0b". The command output varies depending on a specific product.

```text
admin:/>show remote_lun path remote_lun_wwn=60:02:2a:11:00:0b:5a:26:06:37:28:12:00:00:00:0b

Path ID Path Type Local Controller Local Port ID Remote IP Remote WWN Remote Port WWPN Host LUN ID Path Priority
------- --------- ---------------- ------------- --------- ---------- ---------------- ----------- -------------
11 FC Link 0A ENG0.A1.H0 -- -- 200a0022a10b5a26 11 Active
12 FC Link 0A ENG0.A1.H2 -- -- 201a0022a10b5a26 11 Active
15 FC Link 0B ENG0.B1.H2 -- -- 201b0022a10b5a26 11 Active
17 FC Link 0B ENG0.B1.H0 -- -- 200b0022a10b5a26 11 Active
```

Query information about a path on a remote LUN whose path ID is "11". The command output varies depending on a specific product.

```text
admin:/>show remote_lun path path_id=11

Path ID : 11
Path Type : FC Link
Local Controller : 0A
Local Port ID : ENG0.A1.H0
Target Name : --
Initiator Name : --
Remote IP : --
Local IP : --
Remote WWN : --
Local Port WWPN : 20080022a103b480
Remote Port WWPN : 200a0022a10b5a26
Host LUN ID : 11
Path Priority : Active
Local ISID : --
Remote TGPT : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                                                 |
|------------------|---------------------------------------------------------|
| Path ID          | Path ID.                                                |
| Path Type        | Path type. The value can be "FC" or "iSCSI".            |
| Local Controller | ID of the local controller.                             |
| Local Port ID    | ID of the local port.                                   |
| Target Name      | iSCSI target name.                                      |
| Initiator Name   | iSCSI initiator name.                                   |
| Remote IP        | IP address of the remote device.                        |
| Local IP         | IP address of the local device.                         |
| Remote WWN       | WWN of the remote device.                               |
| Local Port WWPN  | WWPN of the local port.                                 |
| Remote Port WWPN | WWPN of the remote port.                                |
| Host LUN ID      | Host LUN ID.                                            |
| Path Priority    | Path priority.                                          |
| Local ISID       | iSCSI initiator session identifier of the local device. |
| Remote TGPT      | iSCSI target port group tag of the remote device.       |
