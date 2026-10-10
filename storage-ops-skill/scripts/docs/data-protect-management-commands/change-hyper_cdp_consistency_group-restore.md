# change hyper_cdp_consistency_group restore


##### Function

The **change hyper_cdp_consistency_group restore** command is used to restore data using HyperCDP consistency groups. You can use the HyperCDP consistency groups to restore the source protection group data by running this command.

##### Format

**change hyper_cdp_consistency_group restore** cdp_consistency_group_id=? \[ restore_speed=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_consistency_group_id=? | ID of a HyperCDP consistency group. | The value is an integer ranging from 0 to 99999.<br>To obtain the value, run "show hyper_cdp_consistency_group universal". |
| restore_speed=? | Restoration speed. | The value can be: <br>"Low": 0 to 5 MB/s.<br>"Middle": 10 to 20 MB/s.<br>"High": 50 to 70 MB/s.<br>"Highest": The speed of a single engine reaches 1 GB/s when host services exist and 1.5 GB/s when no host services exist.<br> The default value is "Middle". |

##### Usage Guidelines

-   This operation will cause the data of a HyperCDP consistency group to overwrite that of the source protection group.
-   Before performing this operation, back up data on the source protection group and ensure that the selected HyperCDP consistency group is correct.

##### Example

Restore the data of a source protection group using that of HyperCDP consistency group "7" at the high restoration speed.

```text
admin:/>change hyper_cdp_consistency_group restore cdp_consistency_group_id=7 restore_speed=High
WARNING: You are about to restore the HyperCDP consistency group. This operation will use data of HyperCDP objects in HyperCDP consistency group to overwrite data on LUNs in protection group. This operation may cause heavy service pressure and decrease the read/write performance of the host. Before performing this operation, ensure that LUNs in the protection group are not read or written by the host, no data is stored in the host cache, and HyperCDP objects in the HyperCDP consistency group are not written by the host.
Suggestions:
1. Before performing this operation, back up the protection group data.
2. Ensure that the free capacity of the storage pool is greater than the actual capacity of LUNs in the protection group.
3. Select the medium speed. If you select the high or highest speed, perform this operation during off-peak hours.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
