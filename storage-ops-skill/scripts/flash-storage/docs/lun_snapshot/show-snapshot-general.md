# show snapshot general


##### Function

The **show snapshot general** command is used to query snapshot information.

##### Format

**show snapshot general** \[ snapshot_id=? \| snapshot_id_list=? \] \[ snapshot_name=? \| snapshot_name_list=? \] \[ parent_id=? \] \[ parent_name=? \] \[ \[ source_lun_id=? \] \[ source_lun_name=? \] \[ cascaded_level=? \] \] \[ usage_type=? \]

##### Parameters

| Parameter            | Description             | Value                                                                                                                                                                                                                                                                                                                                                 |
|----------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| snapshot_id=?        | Snapshot ID.            | To obtain the value, run "**show snapshot general**" without parameters.                                                                                                                                                   |
| snapshot_id_list=?   | Snapshot ID list.       | To obtain the value, run the "**show snapshot general**" command without parameters. You can add multiple snapshots. Separate multiple IDs by commas (,), or specify an ID range using a hyphen (-), for example, "0,5-8". |
| snapshot_name=?      | Snapshot name.          | To obtain the value, run "**show snapshot general**" without parameters.                                                                                                                                                   |
| snapshot_name_list=? | Snapshot name list.     | To obtain the value, run the "**show snapshot general**" command without parameters. You can add multiple snapshots. Separate multiple names by commas (,).                                                                |
| parent_id=?          | Parent object ID.       | The value ranges from 0 to 65535.                                                                                                                                                                                                                                                                                                                     |
| parent_name=?        | Parent object name.     | \-                                                                                                                                                                                                                                                                                                                                                    |
| source_lun_id=?      | Source LUN ID.          | The value ranges from 0 to 65535.                                                                                                                                                                                                                                                                                                                     |
| source_lun_name=?    | Name of the source LUN. | \-                                                                                                                                                                                                                                                                                                                                                    |
| cascaded_level=?     | Cascaded level.         | The value ranges from 0 to 7.                                                                                                                                                                                                                                                                                                                         |
| usage_type=?         | Snapshot type.          | The value can be "LUN_SNAP" or "VVOL_SNAP".                                                                                                                                                                                                                                                                                                           |

##### Usage Guidelines

-   Run "**show snapshot general**" to query information about all snapshots.
-   Run "**show snapshot general** snapshot_id=?" to query information about a specified snapshot.

##### Example

Query detailed information about the snapshot whose ID is "1".

```text
admin:/>show snapshot general snapshot_id=1

ID                            : 16
Name                          : sn
Source LUN ID                 : 0
Source LUN Name               : lun0000
Health Status                 : Normal
Running Status                : Activated
Capacity                      : 1.000GB
Subscribed Capacity           : 0.000B
WWN                           : 688cf98100dac53000c1fe6c00000010
Time Stamp                    : 2020-07-05/15:58:02 UTC+08:00
Restore Start Time            : --
Restore End Time              : --
Restore Speed                 : Middle
Restore Progress(%)           : --
Exposed To Initiator          : Unmapped
IO Priority                   : Low
SmartQoS Policy ID            : --
Parent ID                     : 0
Parent Name                   : lun0000
Cascaded Level                : 0
Protection Capacity           : 0.000B
Restore Target Object ID      : --
Restore Target Object Name    : --
Is Scheduled Snapshot         : No
Usage Type                    : LUN_SNAP
Description                   :
HyperCopy ID(s)               : --
Snapshot consistency group ID : --
Clone ID(s)                   : --
NGUID                         : 7100dac53000c1fe88cf986c00000010
```

##### System Response

The following table describes the parameter meanings.

| Parameter                     | Meaning                                    |
|-------------------------------|--------------------------------------------|
| ID                            | ID of the snapshot.                        |
| Name                          | Name of the snapshot.                      |
| Source LUN ID                 | Source LUN ID of the snapshot.             |
| Source LUN Name               | Source LUN name of the snapshot.           |
| Health Status                 | Health status of the snapshot.             |
| Running Status                | Running status of the snapshot.            |
| Capacity                      | Capacity.                                  |
| Subscribed Capacity           | Actual used capacity.                      |
| WWN                           | World Wide Name (WWN) of the snapshot.     |
| Time Stamp                    | Activation time of the snapshot.           |
| Restore Start Time            | Rollback start time of the snapshot.       |
| Restore End Time              | Rollback end time of the snapshot.         |
| Restore Speed                 | Rollback speed of the snapshot.            |
| Restore Progress(%)           | Rollback progress (%).                     |
| Exposed To Initiator          | Mapped or not.                             |
| IO Priority                   | Indicates the I/O priority.                |
| SmartQoS Policy ID            | SmartQoS policy ID.                        |
| Parent ID                     | Parent ID of the snapshot.                 |
| Parent Name                   | Parent name of the snapshot.               |
| Cascaded Level                | Cascaded level of the snapshot.            |
| Protection Capacity           | Protection capacity.                       |
| Restore Target Object ID      | ID of the object to be rolled back.        |
| Restore Target Object Name    | Name of the object to be rolled back.      |
| Is Scheduled Snapshot         | Whether the snapshot is a timing snapshot. |
| Usage Type                    | Snapshot type.                             |
| Description                   | Description.                               |
| HyperCopy ID(s)               | HyperCopy pair ID list.                    |
| Snapshot consistency group ID | Snapshot consistency group ID.             |
| Clone ID(s)                   | Clone ID list.                             |
| NGUID                         | UUID.                                      |
