# restore recycle_bin_view


##### Function

The **restore recycle_bin_view** command is used to restore objects from the recycle bin.

##### Format

**restore recycle_bin_view** delete_type=? { delete_id_list=? \| delete_name_list=? }

##### Parameters

| Parameter        | Description                          | Value                                                     |
|------------------|--------------------------------------|-----------------------------------------------------------|
| delete_type      | Type of the objects to be restored.  | The value is "LUN".                                       |
| delete_id_list   | ID list of objects to be restored.   | To obtain the value, run "show recycle_bin_view general". |
| delete_name_list | Name list of objects to be restored. | To obtain the value, run "show recycle_bin_view general". |

##### Usage Guidelines

-   Run the "**restore recycle_bin_view** delete_type=? delete_id_list=?" command to restore objects of the specified IDs and of a specified type from the recycle bin view.
-   Run the "**restore recycle_bin_view** delete_type=? delete_name_list=?" command to restore objects of the specified names and of a specified type from the recycle bin view.

##### Example

Restore the objects whose IDs are "2" and "3" and type is "LUN" from the recycle bin.

```text
admin:/>restore recycle_bin_view delete_type=LUN delete_id_list=2,3
Restore LUN 2 successfully.
Restore LUN 3 successfully.
```

##### System Response

None
