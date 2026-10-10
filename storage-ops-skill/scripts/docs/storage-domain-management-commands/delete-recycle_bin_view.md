# delete recycle_bin_view


##### Function

The **delete recycle_bin_view** command is used to delete objects from the recycle bin view.

##### Format

**delete recycle_bin_view** delete_type=? { delete_id_list=? \| delete_name_list=? }

##### Parameters

| Parameter        | Description                                                   | Value                                                     |
|------------------|---------------------------------------------------------------|-----------------------------------------------------------|
| delete_type      | Type of an object to be deleted.                              | The value is "LUN".                                       |
| delete_id_list   | ID list of objects to be deleted from the recycle bin view.   | To obtain the value, run "show recycle_bin_view general". |
| delete_name_list | Name list of objects to be deleted from the recycle bin view. | To obtain the value, run "show recycle_bin_view general". |

##### Usage Guidelines

-   Run the "**delete recycle_bin_view** delete_type=? delete_id_list=?" command to delete objects of specified IDs and of a specified type from the recycle bin view.
-   Run the "**delete recycle_bin_view** delete_type=? delete_name_list=?" command to delete objects of specified names and of a specified type from the recycle bin view.

##### Example

Delete the objects whose IDs are "6" and "7" and type is "LUN" from the recycle bin view.

```text
admin:/>delete recycle_bin_view delete_type=LUN delete_id_list=6,7

WARNING: You are about to forcibly delete the LUN in the recycle bin. If some data of the LUN is temporarily stored on the high-speed cache, this operation may cause user data loss.
Suggestion:
1. Before performing this operation, ensure that the data of the LUN on the high-speed cache has been written to disks or external disk arrays.
2. If the data of the LUN on the high-speed cache cannot be written to disks or external disk arrays due to disk or disk array faults, rectify the faults and then write the data to the disks or external disk arrays. Then run the deletion command to delete the LUN.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete LUN 6 successfully.
Delete LUN 7 successfully.
```

##### System Response

None
