# create hyper_copy local


##### Function

The **create hyper_copy local** command is used to create a HyperCopy pair.

##### Format

**create hyper_copy local** name=? source_lun_id=? target_lun_id=? \[ copy_speed=? \] \[ start_synchronize_after_create=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name | HyperCopy pair name. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| source_lun_id | Source LUN ID or source snapshot ID. | The value ranges from 0 to 16383. |
| target_lun_id | Target LUN ID. | The value ranges from 0 to 16383. |
| start_synchronize_after_create | Whether to start synchronization after a HyperCopy pair is created. | The value can be "yes" or "no", where: <br>"yes": start synchronization after a HyperCopy pair is created.<br>"no": do not start synchronization after a HyperCopy pair is created. |
| copy_speed | Copy speed. | The value can be "low", "middle", "high", or "highest", where: <br>"low": indicates the low speed.<br>"middle": indicates the medium speed.<br>"high": indicates the high speed.<br>"highest": indicates the highest speed. |
| description | Description. | - |

##### Usage Guidelines

None

##### Example

Create a HyperCopy pair named "new" for source LUN "5" and target LUN "4".

```text
admin:/>create hyper_copy local name=new source_lun_id=5 target_lun_id=4
Create HyperCopy successfully.
```

Create a HyperCopy pair named "new" for source LUN "6" and target LUN "7" with the "high" copy speed.

```text
admin:/>create hyper_copy local name=new source_lun_id=6 target_lun_id=7 copy_speed=high
WARNING: You are about to create a HyperCopy pair . If you select the high or highest copy speed, the HyperCopy pair will be synchronized or restored at the high or highest speed, which may cause heavy service pressure and decrease the read/write performance of the host. If you select to start synchronization after a HyperCopy pair is created, the source object data will overwrite the target object data. Before performing this operation, ensure that the target object is not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. Perform this operation during off-peak hours.
2. To retain the data of the current target object, back up the target object data first.
3. Ensure that the free capacity of the storage pool is greater than the actual capacity of the source object.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Create HyperCopy successfully.
```

Create a HyperCopy pair for the source LUN whose ID is "1" and the target LUN whose ID is "6". The name of the HyperCopy pair is "newcopy". Whether to start synchronizing data after the pair is created is "yes".

```text
admin:/>create hyper_copy local name=newcopy source_lun_id=1 target_lun_id=6 start_synchronize_after_create=yes
WARNING: You are about to create a HyperCopy pair. If you select the high or highest copy speed, the HyperCopy pair will be synchronized or restored at the high or highest speed, which may cause heavy service pressure and decrease the read/write performance of the host. If you select to start synchronization after a HyperCopy pair is created, the source object data will overwrite the target object data. Before performing this operation, ensure that the target object is not being read or written by the host and no data is stored in the host cache.
Suggestion:
1. Perform this operation during off-peak hours.
2. To retain the data of the current target object, back up the target object data first.
3. Ensure that the free capacity of the storage pool is greater than the actual capacity of the source object.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Create HyperCopy successfully.
Change HyperCopy synchronize successfully.
```

##### System Response

None
