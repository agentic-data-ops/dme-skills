# delete lun


##### Function

The **delete lun** command is used to delete LUNs.

##### Format

**delete lun** { lun_id_list=? \| lun_name_list=? } \[ force=? \] \[ is_delay=? \]

##### Parameters

| Parameter       | Description                                 | Value                                                                                                                                                                                             |
|-----------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lun_id_list=?   | ID list of LUNs that you want to delete.    | To obtain the value, run "show lun general". Multiple IDs are separated by commas (,), or ID range separated by hyphens (-), such as: 0,5-8.                                                      |
| lun_name_list=? | Name list of LUNs that you want to delete.  | To obtain the value, run "show lun general".                                                                                                                                                      |
| force=?         | Whether to forcibly delete a LUN.           | The value can be "yes" or "no", and the default value is "no". This parameter is only used to forcibly delete eDevLUNs, but is not recommended to be used to forcibly delete LUNs of other types. |
| is_delay=?      | Whether to remove a LUN to the recycle bin. | The value can be "yes" or "no". The default value depends on the recycle policy.                                                                                                                  |

##### Usage Guidelines

-   Running this command will delete the information about the LUN from the storage system and the data on the LUN.
-   Before running this command, ensure that the selected LUN is exactly the one you want to delete and no service is running on the LUN.
-   A LUN cannot be deleted when any one of the following conditions is met:
-   The LUN has been added to a mapping view.
-   The LUN has been used for remote replication.
-   The LUN has been used for snapshot.
-   If immediate deletion is not specified, the system determines whether to delete the object to the recycle bin or forcibly delete it based on the recycle bin policy. Run the "show recycle_bin_policy general" command to query the recycle bin configuration policy.

##### Example

Delete the LUNs whose IDs are "5" and "6".

```text
admin:/>delete lun lun_id_list=5,6
WARNING: You are about to delete LUN. This operation will delete the data on the LUN.
Suggestion: Before performing this operation, ensure that the data on the LUN has been backed up or is no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete LUN 5 successfully.
Delete LUN 6 successfully.
```

Delete the LUN whose ID is "3".

```text
admin:/>delete lun lun_id_list=3 force=yes
DANGER: You are about to forcibly delete the LUN. If some data of the LUN is temporarily stored on the high-speed cache, this operation may cause user data loss.
Suggestion:
1. Before forcibly deleting the LUN, ensure that the data of the LUN on the high-speed cache has been written to disks or external disk arrays.
2. If the data of the LUN on the high-speed cache cannot be written to disks or external disk arrays due to disk or disk array faults, recover those faults and write data to disks or external disk arrays. Then run the command without the forcible deletion option to delete the LUN.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete LUN 3 successfully.
```

Remove the LUN whose ID is "3" to the recycle bin.

```text
admin:/>delete lun lun_id_list=3 is_delay=yes
WARNING: You are about to move LUN to the recycle bin. After this operation, the LUN and data on the LUN will be deleted at the preset time point, and space occupied by the LUN will be reclaimed based on the reclamation policy
Suggestion: Before performing this operation, ensure that data on the LUN has been backed up or is no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete LUN 3 successfully.
```

##### System Response

None
