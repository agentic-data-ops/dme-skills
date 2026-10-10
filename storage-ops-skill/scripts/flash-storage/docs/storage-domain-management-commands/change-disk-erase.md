# change disk erase


##### Function

The **change disk erase** command is used to erase data on disks. Data can be erased from only non-member disks or faulty member disks in a disk domain.

##### Format

**change disk erase** disk_id_list=? \[ action=? \| standards=? \| pattern_list=? \| count=? \| verify=? \| capacity_ratio=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disk_id_list=? | ID list of disks on which data erasure will be performed. | The value can be a disk ID range or a disk ID list, where: <br>Disk ID range: The format is start disk ID-end disk ID, for example, "DAE000.1-5".<br>Disk ID list: Multiple disk IDs are separated with commas (,), for example, "DAE000.1,DAE000.2,DAE000.3".<br> To obtain the value, run "show disk general". |
| action=? | Mode of erasing data on disks. | The value can be "overwrite", "block_erase", or "cryptographic_erase". The default value is "block_erase". |
| standards=? | Overwrite standard for data erasure. | The value can be "dod(e)", "dod(ece)", "vsitr", or "custom". The default value is "dod(e)". |
| pattern_list=? | Customized data list entered by users when overwrite is applied in data erasure and the standard is "custom". | The value can be "r" or a hexadecimal number starting with "0x", both occupying 1 byte. A maximum of 3 bytes can be entered and are separated by commas (,). |
| count=? | Times that the "pattern_list" value entered by users is written to disks when overwrite is applied in data erasure and the standard is "custom". | The value is an integer ranging from 1 to 15. The default value is "1". |
| verify=? | Whether to verify erased data. | The value can be "yes" or "no", where: "yes": verifies erased data. "no": does not verify erased data. The default value is "no". |
| capacity_ratio=? | Percentage of erased data to be verified to the total capacity of a disk. | The value is from 1 to 100. The default value is "10". |

##### Usage Guidelines

None

##### Example

Erase user data on disks whose IDs are "DAE000.1", "DAE000.2", and "DAE000.3" in block erase mode.

```text
admin:/>change disk erase disk_id_list=DAE000.1,DAE000.2,DAE000.3
DANGER: You are about to erase data on disks in a specified list. The erased data cannot be restored and the disks may fail to be reconnected with the system. To obtain the final data erasure result, export data erasure records or view data erasure operation logs. This operation will power on-off the disk. Multiple data erasing modes are supported, and the processes may take several minutes to several hours depending on different modes and parameters.
Suggestion: Before performing this operation, confirm that you need to erase the data on disks in the list and check whether the disks are still in use.
Have you read danger alert message carefully?(y/n)y
Enter "I have read and understand the consequences associated with performing this operation." to confirm running this command:
I have read and understand the consequences associated with performing this operation.
Command executed successfully.
```

##### System Response

None
