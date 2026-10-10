# create mapping general


##### Function

The **create mapping general** command is used to create a mapping.

##### Format

**create mapping general** { host_id=? \| host_group_id=? } { lun_id_list=? \| lun_group_id=? } \[ port_group_id=? \] \[ host_lun_id_list=? \| host_lun_id_start=? \] \[ force=? \]

**create mapping general** { host_name=? \| host_group_name=? } { lun_name_list=? \| lun_group_name=? } \[ port_group_name=? \] \[ host_lun_id_list=? \| host_lun_id_start=? \] \[ force=? \]

##### Parameters

| Parameter           | Description                                                                                                                                                                                 | Value                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| host_id=?           | Host ID.                                                                                                                                                                                    | To obtain the value, run "show host general".                                                                                                                                                                                                                                                                                                                                                                         |
| host_group_id=?     | Host group ID.                                                                                                                                                                              | To obtain the value, run "show host_group general".                                                                                                                                                                                                                                                                                                                                                                   |
| lun_id_list=?       | One or more LUN IDs.                                                                                                                                                                        | To obtain the value, run "show lun general".                                                                                                                                                                                                                                                                                                                                                                          |
| lun_group_id=?      | LUN group ID.                                                                                                                                                                               | To obtain the value, run "show lun_group general".                                                                                                                                                                                                                                                                                                                                                                    |
| port_group_id=?     | Port group ID.                                                                                                                                                                              | To obtain the value, run "show port_group general".                                                                                                                                                                                                                                                                                                                                                                   |
| host_name=?         | Host name.                                                                                                                                                                                  | \-                                                                                                                                                                                                                                                                                                                                                                                                                    |
| host_group_name=?   | Host group name.                                                                                                                                                                            | \-                                                                                                                                                                                                                                                                                                                                                                                                                    |
| lun_name_list=?     | One or more LUN names.                                                                                                                                                                      | \-                                                                                                                                                                                                                                                                                                                                                                                                                    |
| lun_group_name=?    | LUN group name.                                                                                                                                                                             | \-                                                                                                                                                                                                                                                                                                                                                                                                                    |
| port_group_name=?   | Port group name.                                                                                                                                                                            | \-                                                                                                                                                                                                                                                                                                                                                                                                                    |
| host_lun_id_list=?  | Host LUN ID that is assigned to a specified LUN.                                                                                                                                            | The value contains one or more matches between LUN IDs and host LUN IDs. The format of a match is "LUN ID:Host LUN ID". If there are multiple matches, separate them with commas (,). Run the "show host lun" and "show host snapshot" commands to query the host LUN IDs that have been assigned. A LUN ID ranges from 0 to 65535, and a host LUN ID ranges from 0 to 4095. A maximum of 1024 matches are supported. |
| host_lun_id_start=? | Start value of a host LUN ID that is allocated to a LUN.                                                                                                                                    | Run the "show host lun" and "show host snapshot" commands to query the host LUN IDs that have been assigned. A host LUN ID ranges from 0 to 4095.                                                                                                                                                                                                                                                                     |
| force=?             | Whether to perform a consistency check for HyperMetro host LUN IDs. This parameter is not specified by default. In this case, a consistency check for HyperMetro host LUN IDs is performed. | The value is "true", indicating not to perform a consistency check for HyperMetro host LUN IDs.                                                                                                                                                                                                                                                                                                                       |

##### Usage Guidelines

None

##### Example

Create a mapping. Set the host ID to "30", LUN ID list to "30,31", and port group ID to "1".

```text
admin:/>create mapping general host_id=30 lun_id_list=30,31 port_group_id=1
DANGER: You are about to create a mapping. There is no port in port group.
Suggestion: Before performing this operation, ensure that the ports in the port group are configured correctly.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
DANGER: You are about to map LUN to host, and modify the mapping between the LUN and host in the port group. If the LUN has been mapped to another host and the host access to the LUN is not exclusive, data may be damaged or inconsistent when multiple service hosts write data to the LUN.
This operation will modify the port groups of all LUNs that are directly mapped to the host, and the host cannot access the LUN after this operation.
Suggestion: Before performing this operation,
1. Ensure that exclusive access to the LUN has been configured for multiple service hosts.
2. Ensure that you have correctly selected the LUN and host whose mapping is to be modified, and host services related to the mapping have been stopped.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Create mapping to lun 30 successfully.
Create mapping to lun 31 successfully.
```

In port group "0", create a mapping between host "0" and LUN group "0".

```text
admin:/>create mapping general host_id=0 lun_group_id=0 port_group_id=0
DANGER: You are about to map all LUNs in LUN group to host. If one or more LUNs have been mapped to other hosts and host accesses to LUNs are not mutually exclusive, data may be damaged or inconsistent when multiple service hosts write data to LUNs.
Suggestion: Before performing this operation, ensure that exclusive access to LUNs has been configured for multiple service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

In port group "0", create a mapping between host group "0" and LUN group "0".

```text
admin:/>create mapping general host_group_id=0 lun_group_id=0 port_group_id=0
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

In the port group named "PortGroupTest", create a mapping between the host named "HostTest" and LUNs with the LUN name list set to "LunTest1,LunTest2".

```text
admin:/>create mapping general host_name=HostTest lun_name_list=LunTest1,LunTest2 port_group_name=PortGroupTest
DANGER: You are about to map LUN to host, and modify the mapping between the LUN and host in the port group. If the LUN has been mapped to another host and the host access to the LUN is not exclusive, data may be damaged or inconsistent when multiple service hosts write data to the LUN.
This operation will modify the port groups of all LUNs that are directly mapped to the host, and the host cannot access the LUN after this operation.
Suggestion: Before performing this operation,
1. Ensure that exclusive access to the LUN has been configured for multiple service hosts.
2. Ensure that you have correctly selected the LUN and host whose mapping is to be modified, and host services related to the mapping have been stopped.
Have you read danger alert message carefully?(y/n)Y

Are you sure you really want to perform the operation?(y/n)Y
Create mapping to lun LunTest1 successfully.
Create mapping to lun LunTest2 successfully.
```

In the port group named "PortGroupTest", create a mapping between the host named "HostTest" and LUN group named "LunTestGroup".

```text
admin:/>create mapping general host_name=HostTest lun_group_name=LunTestGroup port_group_name=PortGroupTest
DANGER: You are about to map all LUNs in LUN group to host. If one or more LUNs have been mapped to other hosts and host accesses to LUNs are not mutually exclusive, data may be damaged or inconsistent when multiple service hosts write data to LUNs.
Suggestion: Before performing this operation, ensure that exclusive access to LUNs has been configured for multiple service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

In the port group named "PortGroupTest", create a mapping between the host group named "HostTestGroup" and LUN group named "LunTestGroup".

```text
admin:/>create mapping general host_group_name=HostTestGroup lun_group_name=LunTestGroup port_group_name=PortGroupTest
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a mapping between host group "1" and LUN group "1", and set the start value of a host LUN ID to "50".

```text
admin:/>create mapping general host_group_id=1 lun_group_id=1 host_lun_id_start=50
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a mapping between host group "1" and LUN group "1", and assign host LUN IDs "6" and "7" for LUN "1" and LUN "2" respectively.

```text
admin:/>create mapping general host_group_id=1 lun_group_id=1 host_lun_id_list=1:6,2:7
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a mapping between host "0" and LUNs "0" and "1". The ID of the port group is "0", in which no port exists.

```text
admin:/>create mapping general host_id=0 lun_id_list=0,1 port_group_id=0
DANGER: You are about to create a mapping. There is no port in port group.
Suggestion: Before performing this operation, ensure that the ports in the port group are configured correctly.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
DANGER: You are about to map LUN to host, and modify the mapping between the LUN and host in the port group. If the LUN has been mapped to another host and the host access to the LUN is not exclusive, data may be damaged or inconsistent when multiple service hosts write data to the LUN.
This operation will modify the port groups of all LUNs that are directly mapped to the host, and the host cannot access the LUN after this operation.
Suggestion: Before performing this operation,
1. Ensure that exclusive access to the LUN has been configured for multiple service hosts.
2. Ensure that you have correctly selected the LUN and host whose mapping is to be modified, and host services related to the mapping have been stopped.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Create mapping to lun 0 successfully.
Create mapping to lun 1 successfully.
```

Create a mapping between host "0" and LUN group "0". The ID of the port group is "0", in which a port has not been connected to a host.

```text
admin:/>create mapping general host_id=0 port_group_id=0 lun_group_id=0
DANGER: You are about to create a mapping. Ports in port group are not detected or not connected to any host in the mapping.
Suggestion: Before performing this operation, confirm that the ports in the port group are configured correctly.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
DANGER: You are about to map all LUNs in LUN group to host. If one or more LUNs have been mapped to other hosts and host accesses to LUNs are not mutually exclusive, data may be damaged or inconsistent when multiple service hosts write data to LUNs.
Suggestion: Before performing this operation, ensure that exclusive access to LUNs has been configured for multiple service hosts.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a mapping between host group "0" and LUN group "0". The ID of the port group is "0", in which a port has not been connected to a host in host group "0".

```text
admin:/>create mapping general host_group_id=0 port_group_id=0 lun_group_id=0
DANGER: You are about to create a mapping. Ports in port group are not detected or not connected to some hosts in the mapped host group.
Suggestion: Before performing this operation, confirm that the ports in the port group are configured correctly.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
DANGER: You are about to map all LUNs in the LUN group to all hosts in the host group. If the host group contains multiple hosts but mutual access exclusion is not properly configured, multiple service hosts may write data to the same LUN, causing data corruption or inconsistency.
Suggestion: Before you perform this operation, ensure that mutual access exclusion has been correctly configured on service hosts.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
