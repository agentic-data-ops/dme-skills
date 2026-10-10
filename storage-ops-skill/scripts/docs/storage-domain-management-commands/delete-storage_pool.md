# delete storage_pool


##### Function

The **delete storage_pool** command is used to delete a specified storage pool.

##### Format

**delete storage_pool** { pool_id=? \| pool_name=? }

**delete storage_pool** { pool_id=? \| pool_name=? } delete_disk_domain=? \[ disk_erase=? \| action=? \| standards=? \| pattern_list=? \| count=? \| verify=? \| capacity_ratio=? \] \*

**delete storage_pool** { pool_id=? \| pool_name=? } delete_disk_domain=? \[ disk_erase=? \| action=? \| type=? \| standards=? \| pattern_list=? \| count=? \| verify=? \| capacity_ratio=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pool_id=? | ID of a storage pool that you want to delete. | To obtain the value, run "show storage_pool general". |
| pool_name=? | Name of a storage pool that you want to delete. | To obtain the value, run the "show storage_pool general" command. |
| delete_disk_domain=? | Whether to delete the disk domain. | The value can be "yes" or "no", where: <br>"yes": deletes the disk domain.<br>"no": does not delete the disk domain.<br> The default value is "no". |
| disk_erase=? | Whether to erase data. | The value can be: <br>"yes": erases disk data.<br>"no": does not erase disk data.<br> The default value is "no". |
| action=? | Data erasing mode. | The value can be: <br>"overwrite": overwriting.<br>"block_erase": erases blocks.<br>"cryptographic_erase": changes the key.<br> For a self-encrypting disk domain, the default value is "cryptographic_erase". For a non-encrypting disk domain, the default value is "block_erase". |
| standards=? | Standards that the overwrite data erasing mode follows. | The value can be "dod(e)", "dod(ece)", "vsitr", or "custom". The default value is "dod(e)". |
| pattern_list=? | User-defined data list entered by a user. | The value can be "r" or a hexadecimal number starting with "0x", both occupying 1 byte. A maximum of 3 bytes can be entered and are separated by commas (,). |
| count=? | Times that the user-defined data list entered by the user is written to disks. | The value is an integer ranging from 1 to 15. The default value is 1. |
| verify=? | Whether to verify erased data. | The value can be: <br>"yes": verifies erased data.<br>"no": does not verify erased data.<br> The default value is "no". |
| capacity_ratio=? | Percentage of erased data to be verified to the total capacity of a disk. | The value is from 1 to 100. |

##### Usage Guidelines

-   Before running this command, ensure that the selected storage pool is exactly the one you want to delete.
-   A storage pool that contains LUNs cannot be deleted. In this condition, you must delete the LUNs before you can delete the storage pool.
-   Running this command will erase details on the deleted storage pool from the storage system.

##### Example

Delete storage pool "0".

```text
admin:/>delete storage_pool pool_id=0
CAUTION: You are about to delete storage pool.
Suggestion: Before performing this operation, ensure that the selected storage pool is correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Delete storage pool "0" and disk domain to which the storage pool belongs.

```text
admin:/>delete storage_pool pool_id=0 delete_disk_domain=yes
DANGER: You are about to delete the storage pool and its disk domain.
Suggestion: Before performing this operation, ensure that you have correctly selected the storage pool.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Deleting storage pool (sp) in background.
Run the "show task general task_id=3" command to query the execution result.
```

Delete storage pool "0", delete the disk domain, and destroy the data of disks in the disk domain.

```text
admin:/>delete storage_pool pool_id=0 delete_disk_domain=yes disk_erase=yes
DANGER: You are about to delete the storage pool and its disk domain and erase data on disks in the storage pool. This operation will permanently erase data on the disks, which cannot be undone.
Suggestion: Before performing this operation, ensure that you have correctly selected the storage pool.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Deleting storage pool (sp) in background.
Run the "show task general task_id=4" command to query the execution result.
```

##### System Response

None
