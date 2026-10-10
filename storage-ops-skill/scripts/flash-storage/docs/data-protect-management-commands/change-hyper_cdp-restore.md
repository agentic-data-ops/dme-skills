# change hyper_cdp restore


##### Function

The **change hyper_cdp restore** command is used to restore data using HyperCDP objects. You can use the HyperCDP objects to restore the source LUN data by running this command.

##### Format

**change hyper_cdp restore** cdp_id=? \[ restore_speed=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_id=? | ID of a HyperCDP object. | The value is an integer ranging from 0 to 1999999.<br>To obtain the value, run "show hyper_cdp general". |
| restore_speed=? | Restoration speed. | The value can be: <br>"Low": 0 to 5 MB/s.<br>"Middle": 10 to 20 MB/s.<br>"High": 50 to 70 MB/s.<br>"Highest": The speed of a single engine reaches 1 GB/s when host services exist and 1.5 GB/s when no host services exist.<br> The default value is "Middle". |

##### Usage Guidelines

-   This operation will cause the data of a HyperCDP object to overwrite that of the source LUN.
-   Before performing this operation, back up data on the source LUN and ensure that the selected HyperCDP object is correct.

##### Example

Restore the data of a source LUN using that of HyperCDP object "7" at the high restoration speed.

```text
admin:/>change hyper_cdp restore cdp_id=7 restore_speed=High
WARNING: You are about to use HyperCDP to restore source LUN. This operation will overwrite data on the source LUN with that on the HyperCDP. This operation may cause heavy service loads and decrease the read/write performance of the host. Before performing this operation, ensure that the source LUN is not being read or written by hosts, no data is saved on the cache of hosts and the source object is not written by hosts.
Suggestion:
1. Before performing this operation, back up the data on the source LUN.
2. Ensure that the free capacity of the storage pool is larger than the capacity occupied by the source LUN.
3. Select the medium speed. If you select the high or highest speed, perform this operation during off-peak hours.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
