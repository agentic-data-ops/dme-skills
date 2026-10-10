# show share nfs_count


##### Function

The **show share nfs_count** command is used to query the number of NFS shares.

##### Format

**show share nfs_count** \[ file_system_id=? \]

##### Parameters

| Parameter        | Description     | Value                             |
|------------------|-----------------|-----------------------------------|
| file_system_id=? | File system ID. | The value ranges from 0 to 65535. |

##### Usage Guidelines

None

##### Example

Query the number of NFS shares.

```text
admin:/>show share nfs_count file_system_id=6
Number : 1
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning               |
|-----------|-----------------------|
| Number    | Number of NFS shares. |
