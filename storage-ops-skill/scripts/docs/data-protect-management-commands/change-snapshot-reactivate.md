# change snapshot reactivate


##### Function

The **change snapshot reactivate** command is used to reactivate snapshots. Use this command if you want to set the point in time of a snapshot to the latest point in time of the source LUN or HyperCDP object.

##### Format

**change snapshot reactivate** snapshot_id_list=? \[ activate_time=? \]

**change snapshot reactivate** snapshot_name_list=? \[ activate_time=? \]

**change snapshot reactivate** snapshot_id=? \[ cdp_id=? \]

**change snapshot reactivate** snapshot_name=? \[ cdp_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id_list=? | ID of a snapshot. | To obtain the value, run "show snapshot general". You can specify multiple snapshot IDs separated by commas (,), or an ID range separated by hyphens (-), such as: 0,5-8. A maximum of 2048 snapshot IDs are allowed. |
| snapshot_id=? | ID of a snapshot. | To obtain the value, run "show snapshot general". |
| snapshot_name_list=? | Snapshot name. | To obtain the value, run "show snapshot general". Multiple snapshots can be activated at the same time. Separate multiple snapshot names with commas (,). |
| snapshot_name=? | Specifies the snapshot name. | You can run the show snapshot general command to obtain the value. |
| activate_time=? | Snapshot activation time. | The value can be "same" or "different", where: <br>"same": All snapshots are activated simultaneously after being deactivated.<br>"different": Snapshots are reactivated one by one.<br> The default value is "different". |
| cdp_id=? | ID of a HyperCDP object. | The value is an integer from 0 to 1999999.<br>To obtain the value, run "show hyper_cdp general". |

##### Usage Guidelines

-   Running this command erases the existing data of the selected snapshot.
-   Before running this command, ensure that the selected snapshot is exactly the one you want to reactivate, and that the existing data of the snapshot is no longer needed or it has been backed up.
-   If the selected snapshot is in the activated state, running this command deactivates and then reactivates the snapshot and sets the latest snapshot time to the reactivation time.
-   If the selected snapshot is in the deactivated state, running this command activates the snapshot and sets the latest snapshot time to the reactivation time.
-   If the selected snapshot is either in the rolling back or the error state, running this command fails.

##### Example

Reactivate snapshot "5".

```text
admin:/>change snapshot reactivate snapshot_id_list=5
DANGER: You are about to reactivate the snapshot. This operation will delete existing snapshot data and protect source LUN data at the current point in time. When multiple snapshots are reactivated, the default activation points in time are different.
Suggestion: Before performing this operation, ensure that the selected snapshot is no longer necessary or has been backed up.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Reactivate snapshot 5 successfully.
```

Reactivate snapshots "12" and "92" simultaneously.

```text
admin:/>change snapshot reactivate snapshot_id_list=12,92 activate_time=same
DANGER: You are about to reactivate the snapshot. This operation will delete existing snapshot data and protect source LUN data at the current point in time. When multiple snapshots are reactivated, the default activation points in time are different.
Suggestion: Before performing this operation, ensure that the selected snapshot is no longer necessary or has been backed up.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Reactivate snapshot successfully.
```

Reactivate snapshots "12" and "92" one by one.

```text
admin:/>change snapshot reactivate snapshot_id_list=12,92 activate_time=different
DANGER: You are about to reactivate the snapshot. This operation will delete existing snapshot data and protect source LUN data at the current point in time. When multiple snapshots are reactivated, the default activation points in time are different.
Suggestion: Before performing this operation, ensure that the selected snapshot is no longer necessary or has been backed up.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Reactivate snapshot 12 successfully.
Reactivate snapshot 92 successfully.
```

Reactivate snapshot "1" for HyperCDP object "0".

```text
admin:/>change snapshot reactivate snapshot_id=1 cdp_id=0
DANGER: You are about to reactivate the snapshot by using a HyperCDP object. This operation deletes existing snapshot data and protects the data at the point in time when the HyperCDP object is activated.
Suggestion: Before performing this operation, ensure that the selected snapshot and HyperCDP object are correct and the data of the selected snapshot is no longer necessary or has been backed up.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Reactivate snapshot successfully.
```

##### System Response

None
