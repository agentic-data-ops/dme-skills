# change snapshot capacity


##### Function

The **change snapshot capacity** command is used to modify the capacity of a snapshot.

##### Format

**change snapshot capacity** { snapshot_id=? \| snapshot_id_list=? \| snapshot_name=? \| snapshot_name_list=? } capacity=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| snapshot_id=? | ID of a snapshot whose capacity you want to modify. | To obtain the value, run "show snapshot general". |
| snapshot_id_list | ID list of snapshots that you want to modify their settings. | To obtain the value, run "show snapshot general".<br>You can specify multiple snapshot IDs separated by commas (,), or an ID range separated by hyphens (-), such as: "0,5-8". |
| snapshot_name=? | Name of the snapshot whose capacity needs to be changed. | You can run the show snapshot general command to obtain the value. |
| snapshot_name_list=? | Snapshot name. | To obtain the value, run "show snapshot general". Multiple snapshots can be activated at the same time. Separate multiple snapshot names with commas (,). |
| capacity=? | Updated capacity of a snapshot. This parameter is not supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | The value is in the format of capacity value + unit, expressed in KB, MB, GB, TB, or Blocks. <br>The value ranges from 512 KB to 256 TB.<br>One block equals 512 bytes.<br>When the unit is GB or TB, a decimal number can be used. |

##### Usage Guidelines

-   Before running this command, ensure that the selected snapshot is exactly the one whose capacity you want to modify.
-   Before running this command, clean up the cache of the application server that has mappings to the selected snapshot.

##### Example

Change the capacity of snapshot "10" to 300 MB.

```text
admin:/>change snapshot capacity snapshot_id=10 capacity=300MB
CAUTION: You are about to perform a snapshot expansion. This operation expands the capacity of the snapshot.
Suggestion: Rescan for the snapshot on the server after the capacity expansion.
Do you wish to continue?(y/n)y
Change snapshot 10 successfully.
```

##### System Response

None
