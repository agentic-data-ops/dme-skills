# create snapshot duplicate


##### Function

The **create snapshot duplicate** command is used to create a duplicate for a snapshot or a HyperCDP object. You can back up a snapshot or a HyperCDP object by running this command.

##### Format

**create snapshot duplicate** snapshot_id=? { name=? \| dst_lun_id=? }

**create snapshot duplicate** snapshot_name=? { name=? \| dst_lun_name=? }

**create snapshot duplicate** cdp_id=? { name=? \| dst_lun_id=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a duplicate. | The value contains 1 to 255 characters including letters, digits, hyphens (-), underscores (_), and periods (.). |
| snapshot_id=? | ID of a snapshot. | To obtain the value, run "show snapshot general". |
| snapshot_name=? | Snapshot name. | The value contains 1 to 255 characters, including letters, digits, hyphens (-), underscores (_), and periods (.).<br>To obtain the value, run "show snapshot general". |
| cdp_id=? | ID of a HyperCDP object. | The value is an integer ranging from 0 to 1999999.<br>To obtain the value, run "show hyper_cdp general". |
| dst_lun_id=? | ID of the target LUN. | To obtain the value, run the "show lun general" command without parameters. |
| dst_lun_name=? | Target LUN name. | To obtain the value, run the "show lun general" command without parameters. |

##### Usage Guidelines

-   Duplicates can only be created for HyperCDP objects or active snapshots.
-   The point in time of a duplicate is the same as that of the HyperCDP object or snapshot for which the duplicate is created for.
-   By default, a newly created duplicate is in the activated state.

##### Example

Create copy "dupsnap" for snapshot "7".

```text
admin:/>create snapshot duplicate snapshot_id=7 name=dupsnap
Command executed successfully.
```

Create copy "dupsnap1" for HyperCDP object "1".

```text
admin:/>create snapshot duplicate cdp_id=1 name=dupsnap1
Command executed successfully.
```

Use target LUN "1" to create a copy for snapshot "10".

```text
admin:/>create snapshot duplicate snapshot_id=10 dst_lun_id=1
WARNING: You are about to create a snapshot copy. This operation will reclaim data of the target LUN. Before this operation, ensure that the host is not reading or writing the target LUN, and no data of the target LUN is stored in the host cache.
Suggestion: If you want to retain data of the target LUN, back up the data in advance.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
