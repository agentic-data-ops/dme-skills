# delete lun_group


##### Function

The **delete lun_group** command is used to delete a specified LUN group.

##### Format

**delete lun_group** { lun_group_id=? \| lun_group_name=? }

##### Parameters

| Parameter        | Description     | Value                                              |
|------------------|-----------------|----------------------------------------------------|
| lun_group_id=?   | LUN group ID.   | To obtain the value, run "show lun_group general". |
| lun_group_name=? | LUN group name. | To obtain the value, run "show lun_group general". |

##### Usage Guidelines

If a LUN group has LUNs, remove all LUNs from it before deleting it.

##### Example

Delete LUN group "2".

```text
admin:/>delete lun_group lun_group_id=2
WARNING: You are about to delete LUN group. This operation cannot be undone. This operation will delete all LUNs within the LUN group and the information about the LUN group from the system.
Suggestion: Before performing this operation, ensure that the selected LUN group is no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete LUN group "LunGroup1".

```text
admin:/>delete lun_group lun_group_name=LunGroup1
WARNING: You are about to delete LUN group. This operation cannot be undone. This operation will delete all LUNs within the LUN group and the information about the LUN group from the system.
Suggestion: Before performing this operation, ensure that the selected LUN group is no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
