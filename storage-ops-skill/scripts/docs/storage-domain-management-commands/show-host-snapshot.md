# show host snapshot


##### Function

The **show host snapshot** command is used to query all the snapshots in the storage system that have been mapped to hosts.

##### Format

**show host snapshot** { host_id=? \| host_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_id=? | Host ID. | To obtain the value, run the "show host general" command. |
| host_name=? | Host name. | To obtain the value, run "show host general". |
| snapshot_name_list=? | Snapshot name list. | You can run the "show snapshot general" command to obtain the snapshot name list. When multiple snapshots need to be specified: You can use commas (,) to separate multiple LUN names or snapshot names. For example, snapshot_name_list=snapshot1,snapshot2,snapshot3. |
| snapshot_id_list=? | Snapshot ID list. | You can run the "show snapshot available_snapshot" command to obtain the value. You can add multiple snapshots. Use commas (,) to separate multiple snapshot IDs, or use hyphens (-) to specify ID ranges, for example, 0,5-8. |

##### Usage Guidelines

None.

##### Example

Query all the snapshots that have been mapped to host "2".

```text
admin:/>show host snapshot host_id=2

Snapshot ID Snapshot Name Host LUN ID
----------- ------------ -----------
34          SnapShot0000 3
35          SnapShot0001 4
36          SnapShot0002 5
```

Query all snapshots that have been mapped to host "host1".

```text
admin:/>show host snapshot host_name=host1

Snapshot ID Snapshot Name Host LUN ID
----------- ------------ -----------
34          SnapShot0000 3
35          SnapShot0001 4
36          SnapShot0002 5
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning        |
|---------------|----------------|
| Snapshot ID   | Snapshot ID.   |
| Snapshot Name | Snapshot name. |
| Host LUN ID   | Host LUN ID.   |
