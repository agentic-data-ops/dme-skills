# delete mapping general


##### Function

The **delete mapping general** command is used to delete a mapping.

##### Format

**delete mapping general** { host_id=? \| host_group_id=? } { lun_id_list=? \| lun_group_id=? }

**delete mapping general** { host_name=? \| host_group_name=? } { lun_name_list=? \| lun_group_name=? }

##### Parameters

| Parameter         | Description            | Value                                               |
|-------------------|------------------------|-----------------------------------------------------|
| host_id=?         | Host ID.               | To obtain the value, run "show host general".       |
| host_group_id=?   | Host group ID.         | To obtain the value, run "show host_group general". |
| lun_id_list=?     | One or more LUN IDs.   | To obtain the value, run "show lun general".        |
| lun_group_id=?    | LUN group ID.          | To obtain the value, run "show lun_group general".  |
| host_name=?       | Host name.             | \-                                                  |
| host_group_name=? | Host group name.       | \-                                                  |
| lun_name_list=?   | One or more LUN names. | \-                                                  |
| lun_group_name=?  | LUN group name.        | \-                                                  |

##### Usage Guidelines

None

##### Example

Delete the mapping between host "0" and LUNs with the LUN ID list set to "0,1".

```text
admin:/>delete mapping general host_id=0 lun_id_list=0,1
DANGER: You are about to delete the mapping between the LUN and host. After this operation, the host cannot access the LUN.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN and host to be unmapped, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the mapping between host "0" and LUN group "0".

```text
admin:/>delete mapping general host_id=0 lun_group_id=0
DANGER: You are about to delete the mapping between the LUN group and host. After this operation, the host cannot access the LUNs.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN group and host to be unmapped, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the mapping between host group "0" and LUN group "0".

```text
admin:/>delete mapping general host_group_id=0 lun_group_id=0
DANGER: You are about to delete the mapping between the LUN group and host group. After this operation, the hosts cannot access the LUNs.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN group and host group to be unmapped, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the mapping between the host named "HostTest" and LUNs with the LUN name list set to "LunTest1,LunTest2".

```text
admin:/>delete mapping general host_name=HostTest lun_name_list=LunTest1,LunTest2
DANGER: You are about to delete the mapping between the LUN and host. After this operation, the host cannot access the LUN.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN and host to be unmapped, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the mapping between the host named "HostTest" and LUN group named "LunGroupTest".

```text
admin:/>delete mapping general host_name=HostTest lun_group_name=LunGroupTest
DANGER: You are about to delete the mapping between the LUN group and host. After this operation, the host cannot access the LUNs.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN group and host to be unmapped, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the mapping between the host group named "HostGroupTest" and LUN group named "LunGroupTest".

```text
admin:/>delete mapping general host_group_name=HostGroupTest lun_group_name=LunGroupTest
DANGER: You are about to delete the mapping between the LUN group and host group. After this operation, the hosts cannot access the LUNs.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN group and host group to be unmapped, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
