# create snapshot general


##### Function

The **create snapshot general** command is used to create snapshots. You can create an identical and usable point-in-time duplicate for a data object by running this command.

##### Format

**create snapshot general** { lun_id_list=? \| snapshot_id_list=? } { name=? \| dst_lun_id_list=? } \[ snapshot_id=? \] \[ description=? \] \[ is_batch_add=? \]

**create snapshot general** { lun_name_list=? \| snapshot_name_list=? } { name=? \| dst_lun_name_list=? } \[ snapshot_id=? \] \[ description=? \] \[ is_batch_add=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_id_list=? | ID of a source logical unit number (LUN). | To obtain the value, run "show snapshot available_lun".<br>You can specify multiple source LUN IDs separated by commas (,), or ID range separated by hyphens(-), such as: 0, 5-8. |
| lun_name_list=? | Name of the source LUN. | To obtain the value, run "show snapshot available_lun".<br>You can add multiple source LUNs and separate them with commas (,). |
| snapshot_id_list=? | ID of a snapshot. | To obtain the value, run "show snapshot available_snapshot".<br>You can specify multiple snapshot IDs separated by commas (,), or ID range separated by hyphens(-), such as: 0, 5-8. |
| snapshot_name_list=? | Snapshot name. | To obtain the value, run "show snapshot general". Multiple snapshots can be activated at the same time. Separate multiple snapshot names with commas (,). |
| name=? | Name of a snapshot. | The value contains 1 to 255 characters including letters, digits, hyphens (-), underscores (_), and periods (.). NOTE: When creating snapshots in a batch, the length of name=? cannot exceed 251 characters. |
| snapshot_id=? | ID of snapshot. You can set the snapshot ID for the newly created snapshot. It cannot be changed after you specified. The storage system can automatically assign a storage snapshot ID when you do not specify. | The value is an integer ranging from 0 to 65535. |
| description | Description. | - |
| dst_lun_id_list | List of target LUN IDs. | To obtain the value, run the "show lun general" command.<br>You can add multiple LUNs. Use commas (,) to separate LUN IDs or use hyphens (-) to specify LUN ID ranges, for example, "0,5-8". |
| dst_lun_name_list | List of target LUN names. | To obtain the value, run the "show lun general" command.<br>You can add multiple LUNs. Use commas (,) to separate LUN names, for example, "0,1". |
| is_batch_add | Whether the operation is a batch operation. NOTE: If the source LUN of a snapshot is the secondary LUN of a remote replication and this parameter is not specified or is set to "no", the created snapshot is redirected to the data at the specified point in time to ensure that the snapshot data is available. If this parameter is set to "yes", the data in the created snapshot is the real-time data of the secondary LUN. The invoker must ensure that the data is available. | The value can be "yes" or "no". The default value is "no". |

##### Usage Guidelines

You can create multi-snapshots for different LUNs/snapshots in the mean time.

##### Example

Create a snapshot for LUN "5", and the name is "new".

```text
admin:/>create snapshot general lun_id_list=5 name=new
Create snapshot of LUN 5 successfully.
```

Create a snapshot for snapshot "5", and the name is "new".

```text
admin:/>create snapshot general snapshot_id_list=5 name=new
Create snapshot of LUN 5 successfully.
```

Create a snapshot respectively for LUNs "1", "3", and "4".

```text
admin:/>create snapshot general lun_id_list=1,3,4 name=new001
Create snapshot of LUN 1 successfully.
Create snapshot of LUN 3 successfully.
Create snapshot of LUN 4 successfully.
```

Use target LUN "1" to create a snapshot for LUN "0".

```text
admin:/>create snapshot general lun_id_list=0 dst_lun_id_list=1
WARNING: You are about to create a snapshot. This operation will reclaim data of the target LUN. Before this operation, ensure that the host is not reading or writing the target LUN, and no data of the target LUN is stored in the host cache.
Suggestion: If you want to retain data of the target LUN, back up the data in advance.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Create snapshot of LUN 0 successfully.
```

Use the batch creation interface to create a snapshot for the LUNs whose IDs are 24 to 29.

```text
admin:/>create snapshot general lun_id_list=24-29 name=new is_batch_add=yes
Create snapshot of LUN 24 successfully.
Create snapshot of LUN 25 successfully.
Create snapshot of LUN 26 successfully.
Create snapshot of LUN 27 successfully.
Create snapshot of LUN 28 successfully.
Create snapshot of LUN 29 successfully.
```

##### System Response

None
