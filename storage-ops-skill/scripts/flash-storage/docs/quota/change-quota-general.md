# change quota general


##### Function

The **change quota general** command is used to change a specified quota of a file system.

##### Format

**change quota general** quota_id=? { space_hard_quota=? \| space_soft_quota=? \| file_hard_quota=? \| file_soft_quota=? } \*

##### Parameters

| Parameter          | Description                                           | Value                                                                                                                                                                         |
|--------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| quota_id=?         | Quota ID.                                             | To obtain the value, run the "show quota general" command.                                                                                                                    |
| space_hard_quota=? | Space hard quota.                                     | The value must be greater than the space soft quota, and smaller than or equal to 256 PB. The unit can be MB, GB, TB.                                                         |
| space_soft_quota=? | Space soft quota.                                     | The value must be smaller than the space hard quota. If the space hard quota is not specified, the value must be smaller than or equal to 256 PB. The unit can be MB, GB, TB. |
| file_hard_quota=?  | File quantity hard quota, expressed in thousands (K). | The value must be greater than the file quantity soft quota, and smaller than or equal to 2,000,000.                                                                          |
| file_soft_quota=?  | File quantity soft quota, expressed in thousands (K). | The value must be smaller than the file quantity hard quota. If the file quantity hard quota is not specified, the value must be smaller than or equal to 2,000,000.          |

##### Usage Guidelines

None

##### Example

Change the hard space quota of ID "1@4097@3" to 1 GB.

```text
admin:/>change quota general quota_id=1@4097@3 space_hard_quota=1GB
Command executed successfully.
```

##### System Response

None
