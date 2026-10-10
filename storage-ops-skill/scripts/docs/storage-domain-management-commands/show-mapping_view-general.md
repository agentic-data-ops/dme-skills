# show mapping_view general


##### Function

The **show mapping_view general** command is used to query information about mapping views of a storage system.

##### Format

**show mapping_view general** { mapping_view_id=? \| mapping_view_name=? } \[ detail=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| mapping_view_id=? | ID of a mapping view. | To obtain the value, run "show mapping_view general" without parameters. |
| mapping_view_name=? | Name of a mapping view. | To obtain the value, run "show mapping_view general" without parameters. |
| detail=? | Whether to enable the function of querying details about a mapping view. | "enable": enables details about a mapping view.<br>"hierarchical_detail": enables or disables the hierarchical detail function. |

##### Usage Guidelines

-   Run the "**show mapping_view general**" command to query information about all mapping views of a storage system.
-   Run the "**show mapping_view general** mapping_view_id=?" command to query information about a specific mapping view.
-   Run the "**show mapping_view general** mapping_view_id=? detail=enable" command to query details about a specific mapping view .

##### Example

Query information about the mapping view whose ID is "1".

```text
admin:/>show mapping_view general mapping_view_id=1

Mapping View ID    : 1
Mapping View Name   : MappingView001
Inband Command       : Disable
LUN Group ID        : 1
LUN Group Name      : LUNGroup001
Port Group ID       : 1
Port Group Name      : PortGroup001
Host Group ID       : 1
Host Group Name      : HostGroup001
```

Query information about the mapping view whose name is "map01".

```text
admin:/>show mapping_view general mapping_view_name=map01

Mapping View ID    : 1
Mapping View Name   : MappingView001
Inband Command       : Disable
LUN Group ID        : 1
LUN Group Name      : LUNGroup001
Port Group ID       : 1
Port Group Name      : PortGroup001
Host Group ID       : 1
Host Group Name      : HostGroup001
```

Query details of the mapping view whose ID is "1".

```text
admin:/>show mapping_view general mapping_view_id=0 detail=enable

------------ Host Information-------------
ID  Name    Health Status  Operating System  IP Address  Model  Location
--  ------  -------------  ----------------  ----------  -----  --------
1   host_1  Normal         Linux             --
2   host_2  Normal         Linux             --
3   host_3  Normal         Linux             --
------------ FC and ISCSI Initiator Information-------------
WWN               Running Status  Free  Alias  Host ID  Multipath Type  Failover Mode  Path Type  Special Mode Type
----------------  --------------  ----  -----  -------  --------------  -------------  ---------  -----------------
6d494e81000e9d01  Offline         No    --     1        Default         --             --         --
6d494e81000e9d02  Offline         No    --     1        Default         --             --         --
iSCSI IQN  Running Status  Free  Alias  Host ID  CHAP Enabled  CHAP User  Multipath Type  CHAP Target User  Discovery Chap Type  Normal Chap Type  Failover Mode  Path Type  Special Mode Type
---------  --------------  ----  -----  -------  ------------  ---------  --------------  ----------------  -------------------  ----------------  -------------  ---------  -----------------
iscsi_1    Offline         No    --     2        No            --         Default         --                --                   --                --             --         --
iscsi_2    Offline         No    --     2        No            --         Default         --                --                   --                --             --         --
------------ LUN Information-------------
ID  Name      Pool ID  Capacity  Health Status  Running Status  Type   WWN
--  --------  -------  --------  -------------  --------------  -----  --------------------------------
0   lun_0000  0         1.000MB  Normal         Online          Thick  6d494e81000e9de300601d4f00000001
1   lun_0001  0         1.000MB  Normal         Online          Thick  6d494e81000e9de300601d8300000002
2   lun_0002  0         1.000MB  Normal         Online          Thick  6d494e81000e9de300601d9f00000003
------------ Port Information-------------
ETH port:
ID              Health Status  Running Status  Type       IPv4 Address  IPv6 Address  MAC                Role         Working Rate(Mbps)  Enabled  Max Speed(Mbps)
--------------  -------------  --------------  ---------  ------------  ------------  -----------------  -----------  ------------------  -------  ---------------
CTE0.B.IOM1.P0  Normal         Link Down       Host Port  --            --            00:01:02:03:04:05  INI and TGT  --                  Yes      10000
FC port:
ID          Health Status  Running Status  Type       Working Rate(Mbps)  WWN               Role         Working Mode  Configured Mode  Enabled  Max Speed(Mbps)  Number Of Initiators
----------  -------------  --------------  ---------  ------------------  ----------------  -----------  ------------  ---------------  -------  ---------------  --------------------
CTE0.A3.P0  Normal         Link Up         Host Port  8000                2208c88d8370071a  INI and TGT  FC-AL         Auto-Adapt       Yes      16000            1
FCoE port:
ID              Health Status  Running Status  Type       Working Rate(Mbps)  WWN               Role  Enabled  Max Speed(Mbps)  Number Of Initiators
--------------  -------------  --------------  ---------  ------------------  ----------------  ----  -------  ---------------  --------------------
CTE0.B.IOM1.P0  Normal         Link Down       Host Port  --                  2000000102030405  TGT   Yes      10000            0
```

Query details of the mapping view whose name is "map01".

```text
admin:/>show mapping_view general mapping_view_name=map01 detail=enable

------------ Host Information-------------
ID  Name    Health Status  Operating System  IP Address  Model  Location
--  ------  -------------  ----------------  ----------  -----  --------
1   host_1  Normal         Linux             --
2   host_2  Normal         Linux             --
3   host_3  Normal         Linux             --
------------ FC and ISCSI Initiator Information-------------
WWN               Running Status  Free  Alias  Host ID  Multipath Type  Failover Mode  Path Type  Special Mode Type
----------------  --------------  ----  -----  -------  --------------  -------------  ---------  -----------------
6d494e81000e9d01  Offline         No    --     1        Default         --             --         --
6d494e81000e9d02  Offline         No    --     1        Default         --             --         --
iSCSI IQN  Running Status  Free  Alias  Host ID  CHAP Enabled  CHAP User  Multipath Type  CHAP Target User  Discovery Chap Type  Normal Chap Type  Failover Mode  Path Type  Special Mode Type
---------  --------------  ----  -----  -------  ------------  ---------  --------------  ----------------  -------------------  ----------------  -------------  ---------  -----------------
iscsi_1    Offline         No    --     2        No            --         Default         --                --                   --                --             --         --
iscsi_2    Offline         No    --     2        No            --         Default         --                --                   --                --             --         --
------------ LUN Information-------------
ID  Name      Pool ID  Capacity  Health Status  Running Status  Type   WWN
--  --------  -------  --------  -------------  --------------  -----  --------------------------------
0   lun_0000  0         1.000MB  Normal         Online          Thick  6d494e81000e9de300601d4f00000001
1   lun_0001  0         1.000MB  Normal         Online          Thick  6d494e81000e9de300601d8300000002
2   lun_0002  0         1.000MB  Normal         Online          Thick  6d494e81000e9de300601d9f00000003
------------ Port Information-------------
ETH port:
ID              Health Status  Running Status  Type       IPv4 Address  IPv6 Address  MAC                Role         Working Rate(Mbps)  Enabled  Max Speed(Mbps)
--------------  -------------  --------------  ---------  ------------  ------------  -----------------  -----------  ------------------  -------  ---------------
CTE0.B.IOM1.P0  Normal         Link Down       Host Port  --            --            00:01:02:03:04:05  INI and TGT  --                  Yes      10000
FC port:
ID          Health Status  Running Status  Type       Working Rate(Mbps)  WWN               Role         Working Mode  Configured Mode  Enabled  Max Speed(Mbps)  Number Of Initiators
----------  -------------  --------------  ---------  ------------------  ----------------  -----------  ------------  ---------------  -------  ---------------  --------------------
CTE0.A3.P0  Normal         Link Up         Host Port  8000                2208c88d8370071a  INI and TGT  FC-AL         Auto-Adapt       Yes      16000            1
FCoE port:
ID              Health Status  Running Status  Type       Working Rate(Mbps)  WWN               Role  Enabled  Max Speed(Mbps)  Number Of Initiators
--------------  -------------  --------------  ---------  ------------------  ----------------  ----  -------  ---------------  --------------------
CTE0.B.IOM1.P0  Normal         Link Down       Host Port  --                  2000000102030405  TGT   Yes      10000            0
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                                 |
|-------------------|-----------------------------------------|
| Mapping View ID   | ID of a mapping view.                   |
| Mapping View Name | Name of a mapping view.                 |
| Inband Command    | Whether the in-band command is enabled. |
| Work Mode         | Work mode of the mapping view.          |
| LUN Group ID      | Associated LUN group ID.                |
| LUN Group Name    | Associated LUN group name.              |
| Port Group ID     | Associated port group ID.               |
| Port Group Name   | Associated port group name.             |
| Host Group ID     | Associated host group ID.               |
| Host Group Name   | Associated host group name.             |
