# delete disk_domain


##### Function

The **delete disk_domain** command is used to delete a disk domain.

##### Format

**delete disk_domain** disk_domain_id=? \[ disk_erase=? \| action=? \| standards=? \| pattern_list=? \| count=? \| verify=? \| capacity_ratio=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disk_domain_id=? | ID of a disk domain that you want to delete. | To obtain the value, run "show disk_domain general". |
| disk_erase=? | Whether to erase data. | The value can be: <br>"yes": erases disk data.<br>"no": does not erase disk data.<br> The default value is "no". |
| action=? | Data erasing mode. | The value can be: <br>"overwrite": overwriting.<br>"block_erase": erases blocks.<br>"cryptographic_erase": changes the key.<br> For a self-encrypting disk domain, the default value is "cryptographic_erase". For a non-encrypting disk domain, the default value is "block_erase". |
| standards=? | Standards that the overwrite data erasing mode follows. | The value can be "dod(e)", "dod(ece)", "vsitr", or "custom". The default value is "dod(e)". |
| pattern_list=? | User-defined data list entered by a user. | The value can be "r" or a hexadecimal number starting with "0x", both occupying 1 byte. A maximum of 3 bytes can be entered and are separated by commas (,). |
| count=? | Times that the user-defined data list entered by the user is written to disks. | The value is an integer ranging from 1 to 15. The default value is 1. |
| verify=? | Whether to verify erased data. | The value can be: <br>"yes": verifies erased data.<br>"no": does not verify erased data.<br> The default value is "no". |
| capacity_ratio=? | Percentage of erased data to be verified to the total capacity of a disk. | The value ranges from 1 to 100. |

##### Usage Guidelines

Run the "**delete disk_domain** disk_domain_id" command to delete a disk domain.

##### Example

Delete the disk domain whose ID is "0".

```text
admin:/>delete disk_domain disk_domain_id=0
CAUTION: You are about to delete disk domain.
Suggestion: Before performing this operation, ensure that the selected disk domain is correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Delete the disk domain whose ID is "0" and erase the data on disks in the disk domain.

```text
admin:/>delete disk_domain disk_domain_id=0 disk_erase=yes
DANGER: You are about to delete the disk domain and erase the data on disks in the disk domain. This operation will permanently erase the data on the disks and cannot be undone. This operation will power on-off the disk. Multiple data erasing modes are supported, and the processes may take several minutes to several hours depending on different modes and parameters.
Suggestion: Before performing this operation, ensure that you have correctly selected the disk domain.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the disk domain whose ID is "0", erase the data on disks in the disk domain, and verify erased data.

```text
admin:/>delete disk_domain disk_domain_id=0 disk_erase=yes verify=yes
DANGER:You are about to delete a disk domain, erase data on disks in the disk domain, and verify erased data. This operation will permanently erase data on disks in the disk domain and cannot be undone. The disks may fail to be reconnected to the system. Besides, it takes a long time to verify erased data. To obtain the final data erasure result, export data erasure records or view data erasure operation logs. This operation will power on-off the disk. Multiple data erasing modes are supported, and the processes may take several minutes to several hours depending on different modes and parameters.
Suggestion: Before running this command, confirm that you have correctly selected the disk domain to be deleted and data on disks in the disk domain is no longer required. Estimate the time required for verifying erased data, and then determine whether to select the verification function or select a proper proportion of data to be verified. For SSDs, about 200 MB to 350 MB data can be verified per second.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
