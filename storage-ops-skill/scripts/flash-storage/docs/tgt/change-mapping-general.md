# change mapping general


##### Function

The **change mapping general** command is used to modify mapping information.

##### Format

**change mapping general** { host_id=? \| host_group_id=? } { lun_id=? \| lun_group_id=? } { new_port_group_id=? \| remove_port_group=? }

**change mapping general** { host_name=? \| host_group_name=? } { lun_name=? \| lun_group_name=? } { new_port_group_name=? \| remove_port_group=? }

##### Parameters

| Parameter             | Description                          | Value                                               |
|-----------------------|--------------------------------------|-----------------------------------------------------|
| host_id=?             | Host ID.                             | To obtain the value, run "show host general".       |
| host_group_id=?       | Host group ID.                       | To obtain the value, run "show host_group general". |
| lun_id=?              | LUN ID.                              | To obtain the value, run "show lun general".        |
| lun_group_id=?        | LUN group ID.                        | To obtain the value, run "show lun_group general".  |
| new_port_group_id=?   | New port group ID.                   | \-                                                  |
| host_name=?           | Host name.                           | \-                                                  |
| host_group_name=?     | Host group name.                     | \-                                                  |
| lun_name=?            | LUN name.                            | \-                                                  |
| lun_group_name=?      | LUN group name.                      | \-                                                  |
| new_port_group_name=? | New port group name.                 | \-                                                  |
| remove_port_group=?   | Removes a port group from a mapping. | The value is "yes".                                 |

##### Usage Guidelines

None

##### Example

For the port group with a mapping between host "0" and LUN "0", modify the port group ID to "0".

```text
admin:/>change mapping general host_id=0 lun_id=0 new_port_group_id=0
DANGER: You are about to modify the mapping between the LUN and host in the port group. This operation will modify the port groups of all LUNs that are directly mapped to the host, and the host cannot access the LUN after this operation.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN and host whose mapping is to be modified, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

For the port group with a mapping between host "0" and LUN group "0", modify the port group ID to "0".

```text
admin:/>change mapping general host_id=0 lun_group_id=0 new_port_group_id=0
DANGER: You are about to modify the mapping between the LUN group and host in the port group. After this operation, the host cannot access the LUNs.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN group and host whose mapping is to be modified, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

For the port group with a mapping between host group "0" and LUN group "0", modify the port group ID to "0".

```text
admin:/>change mapping general host_group_id=0 lun_group_id=0 new_port_group_id=0
DANGER: You are about to modify the mapping between the LUN group and host group in the port group. After this operation, the hosts cannot access the LUNs.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN group and host group whose mapping is to be modified, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

For the port group with a mapping between the host named "HostTest" and LUN named "LunTest", modify the port group name to "PortGroupTest".

```text
admin:/>change mapping general host_name=HostTest lun_name=LunTest new_port_group_name=PortGroupTest
DANGER: You are about to modify the mapping between the LUN and host in the port group. This operation will modify the port groups of all LUNs that are directly mapped to the host, and the host cannot access the LUN after this operation.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN and host whose mapping is to be modified, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

For the port group with a mapping between the host named "HostTest" and LUN group named "LunGroupTest", modify the port group name to "PortGroupTest".

```text
admin:/>change mapping general host_name=HostTest lun_group_name=LunGroupTest new_port_group_name=PortGroupTest
DANGER: You are about to modify the mapping between the LUN group and host in the port group. After this operation, the host cannot access the LUNs.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN group and host whose mapping is to be modified, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

For the port group with a mapping between the host group named "HostGroupTest" and LUN group named "LunGroupTest", modify the port group name to "PortGroupTest".

```text
admin:/>change mapping general host_group_name=HostGroupTest lun_group_name=LunGroupTest new_port_group_name=PortGroupTest
DANGER: You are about to modify the mapping between the LUN group and host group in the port group. After this operation, the hosts cannot access the LUNs.
Suggestion:
1. Before performing this operation, ensure that you have correctly selected the LUN group and host group whose mapping is to be modified, and host services related to the mapping have been stopped.
2. After this operation is complete, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the Host Connectivity Guide for XXX. XXX indicates the operating system name, for example, Windows.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
