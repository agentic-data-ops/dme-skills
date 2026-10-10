# show mapping general


##### Function

The **show mapping general** command is used to query mapping information.

##### Format

**show mapping general** \[ host_id=? \| host_group_id=? \] \[ lun_id=? \| lun_group_id=? \]

**show mapping general** \[ host_name=? \| host_group_name=? \] \[ lun_name=? \| lun_group_name=? \]

##### Parameters

| Parameter         | Description      | Value                                               |
|-------------------|------------------|-----------------------------------------------------|
| host_id=?         | Host ID.         | To obtain the value, run "show host general".       |
| host_group_id=?   | Host group ID.   | To obtain the value, run "show host_group general". |
| lun_id=?          | LUN ID.          | To obtain the value, run "show lun general".        |
| lun_group_id=?    | LUN group ID.    | To obtain the value, run "show lun_group general".  |
| host_name=?       | Host name.       | \-                                                  |
| host_group_name=? | Host group name. | \-                                                  |
| lun_name=?        | LUN name.        | \-                                                  |
| lun_group_name=?  | LUN group name.  | \-                                                  |

##### Usage Guidelines

None

##### Example

Query the mapping between host "0" and LUN "0".

```text
admin:/>show mapping general host_id=0 lun_id=0

Host ID       : 0
LUN ID        : 0
Port Group ID : 0
```

Query the mapping between host "0" and LUN group "0".

```text
admin:/>show mapping general host_id=0 lun_group_id=0

Host ID       : 0
LUN Group ID  : 0
Port Group ID : 0
```

Query the mapping between host group "0" and LUN group "0".

```text
admin:/>show mapping general host_group_id=0 lun_group_id=0

Host Group ID : 0
LUN Group ID  : 0
Port Group ID : 0
```

Query the mapping between the host named "HostTest" and LUN named "LunTest".

```text
admin:/>show mapping general host_name=HostTest  lun_name=LunTest

Host Name       : HostTest
LUN Name        : LunTest
Port Group Name : --
```

Query the mapping between the host named "HostTest" and LUN group named "LunGroupTest".

```text
admin:/>show mapping general host_name=HostTest lun_group_name=LunGroupTest

Host Name       : HostTest
LUN Group Name  : LunGroupTest
Port Group Name : --
```

Query the mapping between the host group named "HostGroupTest" and LUN group named "LunGroupTest".

```text
admin:/>show mapping general host_group_name=HostGroupTest lun_group_name=LunGroupTest

Host Group Name : HostGroupTest
LUN Group Name  : LunGroupTest
Port Group Name : --
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning               |
|-----------------|-----------------------|
| Host ID         | Host ID.              |
| Host Name       | Name of a host.       |
| Host Group ID   | Host group ID.        |
| Host Group Name | Name of a host group. |
| LUN ID          | ID of a LUN.          |
| LUN Name        | Name of a LUN.        |
| LUN Group ID    | ID of a LUN group.    |
| LUN Group Name  | Name of a LUN group.  |
| Port Group ID   | ID of a port group.   |
| Port Group Name | Name of a port group. |
