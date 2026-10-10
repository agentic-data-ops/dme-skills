# show dtree count


##### Function

The **show dtree count** command is used to query the number of dtrees.

##### Format

**show dtree count** { file_system_id=? \| file_system_name=? } \[ name=? \] \[ quotaConfigured=? \] \[ shareType=? \] \[ vstoreId=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_system_id=? | File system ID. | The value is a file system ID. |
| file_system_name=? | File system name. | To obtain the value, run "show file_system general". |
| name=? | Fuzzy query of names. | Substring of dtree names. |
| quotaConfigured=? | Whether to enable the function of determining whether to configure a quota in exact matching mode. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "yes" or "no", where: "yes": enabled. "no": disabled. |
| shareType=? | Share type. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "NFS", "CIFS", or "null", where: "NFS": NFS share. "CIFS": CIFS share. "null": no share is configured. |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

None

##### Example

Query the number of dtrees.

```text
admin:/>show dtree count parent_id=1
10
```

##### System Response

The following table describes the meaning of some returned fields.

| Parameter | Meaning           |
|-----------|-------------------|
| count     | Number of dtrees. |
