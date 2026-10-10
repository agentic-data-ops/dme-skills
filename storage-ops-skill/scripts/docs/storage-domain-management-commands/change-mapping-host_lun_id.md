# change mapping host_lun_id


##### Function

The **change mapping host_lun_id** command is used to modify IDs of mapped host LUNs.

##### Format

**change mapping host_lun_id** { host_id=? \| host_group_id=? } { host_lun_id_list=? } { force=? }

**change mapping host_lun_id** { host_name=? \| host_group_name=? } { host_lun_id_list=? } { force=? }

##### Parameters

| Parameter          | Description                                                                                                                                                                                 | Value                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| host_id=?          | Host ID.                                                                                                                                                                                    | The value ranges from 0 to n minus one, where n indicates the maximum number of hosts.                                                                                                                                                                                                                                                                                                                              |
| host_group_id=?    | Host group ID.                                                                                                                                                                              | The value ranges from 0 to n minus one, where n indicates the maximum number of host groups.                                                                                                                                                                                                                                                                                                                        |
| host_name=?        | Host name.                                                                                                                                                                                  | \-                                                                                                                                                                                                                                                                                                                                                                                                                  |
| host_group_name=?  | Host group name.                                                                                                                                                                            | \-                                                                                                                                                                                                                                                                                                                                                                                                                  |
| host_lun_id_list=? | Host LUN ID that is assigned to a specified LUN.                                                                                                                                            | The value contains one or more matches between LUN IDs and host LUN IDs. The format of a match is "LUN ID:Host LUN ID". If there are multiple matches, separate them with commas (,). Run the "show host lun" and "show host snapshot" commands to query the host LUN IDs that have been assigned. A LUN ID ranges from 0 to 65535, and a host LUN ID ranges from 0 to 4095. A maximum of 64 matches are supported. |
| force=?            | Whether to perform a consistency check for HyperMetro host LUN IDs. This parameter is not specified by default. In this case, a consistency check for HyperMetro host LUN IDs is performed. | The value is "true", indicating not to perform a consistency check for HyperMetro host LUN IDs.                                                                                                                                                                                                                                                                                                                     |

##### Usage Guidelines

None

##### Example

Modify host LUN IDs mapped to host "2".

```text
admin:/>change mapping host_lun_id host_id=2 host_lun_id_list=2:5,4:7
DANGER: You are about to change the host LUN ID of a LUN in the mapping view. If host services are running, this operation may interrupt the services or cause data inconsistency. In SAN-based HyperMetro scenarios where the ESX host is used, this operation may cause the mapped host LUN IDs of LUNs on the primary and secondary ends to be inconsistent, resulting in abnormal functions of the ESX host. In addition, RDM disks may be formatted or overwritten. This operation may cause the LUN unable to be detected by the host if the new host LUN ID is beyond the host LUN ID range supported by the host.
Suggestion:
1. Before performing this operation, ensure that you have selected the correct LUN, stopped host services running on the LUN, and uninstalled physical disks and virtual disks generated by multipathing software from the host. After this operation, scan for disks on the host again.
2. Before performing this operation, ensure that the new host LUN ID is within the host LUN ID range supported by the host.
3. In SAN-based HyperMetro scenarios where the ESX host is used, before performing this operation, ensure that the mapped host LUN IDs of the target LUNs on the primary and secondary ends are consistent.
4. After performing this operation, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the "Host Connectivity Guide for XXX", where "XXX" indicates the operating system name, for example, Windows.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Change mapping host_lun_id to host_lun_id( 2:5 ) successfully.
Change mapping host_lun_id to host_lun_id( 4:7 ) successfully.
```

Modify host LUN IDs mapped to host group "1".

```text
admin:/>change mapping host_lun_id host_group_id=1 host_lun_id_list=2:7,4:8
DANGER: You are about to change the host LUN ID of a LUN in the mapping view. If host services are running, this operation may interrupt the services or cause data inconsistency. In SAN-based HyperMetro scenarios where the ESX host is used, this operation may cause the mapped host LUN IDs of LUNs on the primary and secondary ends to be inconsistent, resulting in abnormal functions of the ESX host. In addition, RDM disks may be formatted or overwritten. This operation may cause the LUN unable to be detected by the host if the new host LUN ID is beyond the host LUN ID range supported by the host.
Suggestion:
1. Before performing this operation, ensure that you have selected the correct LUN, stopped host services running on the LUN, and uninstalled physical disks and virtual disks generated by multipathing software from the host. After this operation, scan for disks on the host again.
2. Before performing this operation, ensure that the new host LUN ID is within the host LUN ID range supported by the host.
3. In SAN-based HyperMetro scenarios where the ESX host is used, before performing this operation, ensure that the mapped host LUN IDs of the target LUNs on the primary and secondary ends are consistent.
4. After performing this operation, delete the residual drive letter and path information to prevent impact on the newly mapped LUNs. For details, see the "Host Connectivity Guide for XXX", where "XXX" indicates the operating system name, for example, Windows.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Change mapping host_lun_id to host_lun_id( 2:7 ) successfully.
Change mapping host_lun_id to host_lun_id( 4:8 ) successfully.
```

##### System Response

None
