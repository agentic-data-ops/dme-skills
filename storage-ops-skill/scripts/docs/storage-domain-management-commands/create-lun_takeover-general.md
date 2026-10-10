# create lun_takeover general


##### Function

The **create lun_takeover general** command is used to create takeover LUNs.

##### Format

**create lun_takeover general** type=? { remote_lun_wwn_list=? name=? storage_pool_id=? write_policy=? \[ prefetch_policy=? \] \[ io_priority=? \] \[ owner_controller=? \] \[ lun_id=? \] \[ dif_switch=? \] \| edevlun_id=? } \[ ignore_reservation=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a LUN that you want to create. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| lun_id=? | ID of a LUN that you want to create. This parameter cannot be used along with the "number=?" parameter. | The value is an integer ranging from 0 to 65535. The storage system automatically allocates an ID for a newly created LUN if this parameter is not used. |
| write_policy=? | Cache write policy. | The value must be "write_through", which indicates write through. The system considers that a data write is successful only after data is written to disks. Disks are accessed in each data write. |
| prefetch_policy=? | Cache prefetch policy. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "none", which indicates non-prefetch. The default value is "none". |
| io_priority=? | I/O priority of a LUN. | The value can be "Low", "Middle", or "High", where: <br>"Low": indicates the low priority.<br>"Middle": indicates the medium priority.<br>"High": indicates the high priority.<br> The default value is "Low". |
| owner_controller=? | Owning controller of a LUN. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0. |
| dif_switch=? | Whether or not to enable the DIF function. | The value can be "Yes" or "No", where: <br>"Yes": The DIF function will be enabled.<br>"No": The DIF function will not be enabled. |
| remote_lun_wwn_list=? | WWN of a remote LUN. | The WWN of the remote LUN consists of 1 to 32 characters, including digits ranging from 0 to 9, lowercase letters ranging from a to f, and uppercase letters ranging from A to F. For example, "6e4a8b6100b0a1cc0003c8c600000001". Two characters can be separated by colons (:). For example, "6e:4a:8b:61:00:b0:a1:cc:00:03:c8:c6:00:00:00:01".<br>You can enter 1 to 10 WWNs of remote LUNs separated by commas (,).<br>You can run the "show remote_lun general" command to obtain the WWN of the remote LUN. |
| storage_pool_id=? | ID of the storage pool to which a LUN belongs. | To obtain the value, run the "show storage_pool general" command. |
| type=? | Type of the LUN takeover. | The value can be "BASIC", "EXTEND", or "THIRD-PARTY", where: <br>"BASIC": basic takeover.<br>"EXTEND": extended takeover.<br>"THIRD-PARTY": third-party takeover. |
| edevlun_id=? | ID of the eDevLUN. | To obtain the value, run the "show lun general usage_type=External" command. |

##### Usage Guidelines

None

##### Example

Create a takeover LUN and set its parameters as follows:
-   Type of the LUN takeover: "BASIC"
-   eDevLUN ID: "0".

```text
admin:/>create lun_takeover general type=BASIC edevlun_id=0
Command executed successfully.
```

Create a takeover LUN and ignore the reservation check by setting parameters as follows:
-   Type of the LUN takeover: "THIRD-PARTY"
-   "remote_lun_wwn_list": "6e4a8b6100b0a1cc0003c8c600000001"
-   "name": "xc"
-   "storage_pool_id": "0"
-   "write_policy": "write_through"
-   "ignore_reservation": "yes".

```text
developer:/>create lun_takeover general type=THIRD-PARTY remote_lun_wwn_list=6e4a8b6100b0a1cc0003c8c600000001 name=xc storage_pool_id=0 write_policy=write_through ignore_reservation=yes
DANGER: You are about to create the remote LUN as an eDevLUN and ignore the SCSI reservation check. If SCSI reservation information exists on the remote LUN, services may fail to be delivered to the created eDevLUN.
Suggestion: After performing this operation, run the show lun_reserve general command to check whether SCSI reservation exists on the eDevLUN to prevent service delivery failure.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
