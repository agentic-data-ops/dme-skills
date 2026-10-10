# show remote_lun general


##### Function

The **show remote_lun general** command is used to query basic information about remote LUNs in a remote device.

##### Format

**show remote_lun general** array_type=? \[ remote_device_id=? \] \[ remote_lun_wwn=? \] \[ link_type=? \] \[ link_id=? \] \[ lun_name_list=? \] \[ lun_id_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| array_type=? | Type of a remote device. | The value can be: <br>1:"replication": The remote device is from Huawei.<br>2:"heterogeneity": The remote device is from a third-party manufacturer.<br>4:"cloud_replication": The remote device is from Huawei and supports cloud replication services. |
| remote_device_id=? | ID of a remote device. | To obtain the value, run "show remote_device general". |
| remote_lun_wwn=? | WWN of a remote LUN. | To obtain the value, run "show remote_lun general". |
| link_type=? | Link type. | The value can be "FC" or "iSCSI", where: <br>"FC": A remote device is connected to a local device by Fibre Channel links.<br>"iSCSI": A remote device is connected to a local device by iSCSI links. |
| link_id=? | Link ID. | To obtain the value, run the "show remote_device link" or "show remote_device elink" command without parameters. |
| lun_id_list | LUN ID list. | Multiple IDs are separated by commas (,), or an ID range is represented using a hyphen(-). |
| lun_name_list | LUN name list. | LUN names are separated by commas (,) or a name range is represented using a hyphen (-). The names before and after the hyphen (-) must be of the same format and length, and cannot contain hyphens (-). |

##### Usage Guidelines

-   The "remote_lun_wwn" parameter can be specified only when the "array_type" parameter is set to "heterogeneity".
-   The "link_type" parameter can be specified only when the "array_type" parameter is set to "heterogeneity".
-   When the "link_type" parameter is specified, you must set the "link_id" parameter.
-   The following parameters or parameter sets are mutually exclusive: "remote_device_id", "remote_lun_wwn", and "link_type".

##### Example

Query basic information about remote LUNs in the remote device whose ID is "0".

```text
admin:/>show remote_lun general array_type=replication remote_device_id=0
Lun Id Name Health Status Device ID
------ -------------------- ------------- ---------
0 LUN000_001 Normal 0
10 snap_001 Normal 0
11 snap_002 Normal 0
12 snap_001_Snap_012_10 Normal 0
13 snap_002_Snap_012_11 Normal 0
14 COPY_001 Normal 0
15 COPY_002 Normal 0
16 COPY_003 Normal 0
17 COPY_004 Normal 0
1 LUN000_002 Normal 0
2 LUN000_003 Normal 0
3 LUN000_004 Normal 0
4 LUN000_005 Normal 0
5 LUN_clone Normal 0
6 LUN_clone01_001 Normal 0
7 LUN_clone01_002 Normal 0
8 LUN_clone01_003 Normal 0
9 CLONE Normal 0

Device SN Capacity Lun WWN Vendor Model Lun Path Number
-------------------- ---------- -------------------------------- -------- --------------- ---------------
210235G7KA10D9000001 5.000GB 6200bc71009b99520025cd0800000000 -- -- --
210235G7KA10D9000001 1.000GB 6200bc71009b9952016ad8bc0000000a -- -- --
210235G7KA10D9000001 1.000GB 6200bc71009b9952016ad91d0000000b -- -- --
210235G7KA10D9000001 1.000GB 6200bc71009b9952016aeaa60000000c -- -- --
210235G7KA10D9000001 1.000GB 6200bc71009b9952016aeae90000000d -- -- --
210235G7KA10D9000001 1.000GB 6200bc71009b9952016c55d30000000e -- -- --
210235G7KA10D9000001 1.000GB 6200bc71009b9952016c55f30000000f -- -- --
210235G7KA10D9000001 1.000GB 6200bc71009b9952016c561700000010 -- -- --
210235G7KA10D9000001 1.000GB 6200bc71009b9952016c564a00000011 -- -- --
210235G7KA10D9000001 5.000GB 6200bc71009b99520025cd2c00000001 -- -- --
210235G7KA10D9000001 5.000GB 6200bc71009b99520025cd4e00000002 -- -- --
210235G7KA10D9000001 5.000GB 6200bc71009b99520025cd7d00000003 -- -- --
210235G7KA10D9000001 5.000GB 6200bc71009b99520025cda300000004 -- -- --
210235G7KA10D9000001 2.000GB 6200bc71009b99520116390e00000005 -- -- --
210235G7KA10D9000001 2.000GB 6200bc71009b995201168beb00000006 -- -- --
210235G7KA10D9000001 2.000GB 6200bc71009b995201168c1200000007 -- -- --
210235G7KA10D9000001 2.000GB 6200bc71009b995201168c3100000008 -- -- --
210235G7KA10D9000001 2.000GB 6200bc71009b9952011c644700000009 -- -- --
```

Query basic information about remote LUNs in the remote device whose ID is "513".

```text
admin:/>show remote_lun general array_type=heterogeneity remote_device_id=513
Lun Id  Name  Health Status  Device ID  Device SN             Capacity  Lun WWN                                          Vendor    Model             Lun Path Number
------  ----  -------------  ---------  --------------------  --------  -----------------------------------------------  --------  ----------------  ---------------
--      --    Normal         513        ST000000000000000172  80.000GB  6f:50:20:31:00:04:05:06:41:60:f1:d5:00:00:00:06  HUAWEI    XSG1              1
```

Query information about the LUNs whose ID list is "11-13" in the remote device whose ID is "0".

```text
admin:/>show remote_lun general array_type=replication remote_device_id=0 lun_id_list=11-13
Lun Id Name                 Health Status Device ID Device SN            Capacity   Lun WWN                          Vendor   Model           Lun Path Number

------ -------------------- ------------- --------- -------------------- ---------- -------------------------------- -------- --------------- ---------------
10     snap_001             Normal        0         210235G7KA10D9000001 1.000GB    6200bc71009b9952016ad8bc0000000a --       --              --
11     snap_002             Normal        0         210235G7KA10D9000001 1.000GB    6200bc71009b9952016ad91d0000000b --       --              --
12     snap_001_Snap_012_10 Normal        0         210235G7KA10D9000001 1.000GB    6200bc71009b9952016aeaa60000000c --       --              --
13     snap_002_Snap_012_11 Normal        0         210235G7KA10D9000001 1.000GB    6200bc71009b9952016aeae90000000d --       --              --
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                       |
|-----------------|-----------------------------------------------|
| Lun Id          | ID of a remote LUN.                           |
| Name            | Name of a remote LUN.                         |
| Health Status   | Health status of a remote LUN.                |
| Device ID       | ID of a remote device.                        |
| Device SN       | Serial number of a remote device.             |
| Capacity        | Capacity of a remote LUN.                     |
| Lun WWN         | World wide name (WWN) of a remote LUN.        |
| Vendor          | Vendor of a remote device.                    |
| Lun Path Number | Number of paths of a remote LUN.              |
| Model           | Product model of a remote device.             |
| Device Name     | Name of a remote device.                      |
| Device WWN      | World wide name (WWN) of a remote device.     |
| Sector Size(B)  | Size of a sector.                             |
| Is Thin LUN     | Whether the current remote LUN is a thin LUN. |
| Is Used         | Whether the current remote LUN is used.       |
