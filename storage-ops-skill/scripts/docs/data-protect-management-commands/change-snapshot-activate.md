# change snapshot activate


##### Function

The **change snapshot activate** command is used to activate snapshots.

##### Format

**change snapshot activate** { snapshot_id_list=? \| snapshot_name_list=? }

**change snapshot activate** { snapshot_id=? \| snapshot_name_list=? } \[ cdp_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id_list=? | Snapshot ID list. NOTE: If the source LUN of a snapshot is the secondary LUN of a remote replication and the snapshot is activated using this parameter, the snapshot data is the real-time data of the secondary LUN. The invoker must ensure that the data is available. | To obtain the value, run "show snapshot general". You can specify multiple snapshot IDs separated by commas (,), or an ID range separated by hyphens (-), such as: 0,5-8. A maximum of 2048 snapshot IDs are allowed. |
| snapshot_id=? | Snapshot ID. NOTE: If the source LUN of a snapshot is the secondary LUN of a remote replication, the snapshot activated by this parameter is redirected to the internal data at the complete time point to ensure that the snapshot data is available. | To obtain the value, run "show snapshot general". |
| snapshot_name_list=? | Snapshot name. NOTE: If the source LUN of a snapshot is the secondary LUN of a remote replication, the snapshot activated by this parameter is redirected to the internal data at the complete time point to ensure that the snapshot data is available. | You can run the show snapshot general command to obtain the value. Multiple snapshots can be activated at the same time. Separate multiple snapshot names with commas (,). |
| cdp_id=? | ID of a HyperCDP object. | The value is an integer from 0 to 1999999.<br>To obtain the value, run "show hyper_cdp general". |

##### Usage Guidelines

-   Only the snapshots in the inactive state can be activated.
-   Multiple snapshots on different source LUNs can be activated simultaneously, but they on the same source LUN cannot be activated simultaneously.

##### Example

Activate snapshot "10".

```text
admin:/>change snapshot activate snapshot_id_list=10
WARNING: You are about to activate the snapshot.
Suggestion: Before performing this operation, ensure that the storage pool capacity is sufficient.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Activate snapshot successfully.
```

Activate snapshots "7", "8", and "9" simultaneously.

```text
admin:/>change snapshot activate snapshot_id_list=7,8,9
WARNING: You are about to activate the snapshot.
Suggestion: Before performing this operation, ensure that the storage pool capacity is sufficient.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Activate snapshot successfully.
```

Activate snapshot "1" for HyperCDP object "0".

```text
admin:/>change snapshot activate snapshot_id=1 cdp_id=0
WARNING: You are about to activate the snapshot.
Suggestion: Before performing this operation, ensure that the storage pool capacity is sufficient.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Activate snapshot successfully.
```

##### System Response

None
