# change remote_replication second_fs_access


##### Function

The **change remote_replication second_fs_access** command is used to set the read and write attributes of a secondary file system.

##### Format

**change remote_replication second_fs_access** remote_replication_id=? access=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| remote_replication_id=? | Remote replication pair ID. | To obtain the value, run "show remote_replication unified". |
| access=? | Read and write attributes of the secondary file system. | The value can be "read_only" or "read_write", where: <br>"read_only": The secondary file system is read-only.<br>"read_write": The secondary file system can be read and written. |

##### Usage Guidelines

None

##### Example

Change the read/write attribute of the secondary file system of the remote replication pair whose ID is "2100ef02030405060000000200000000" to "read_write".

```text
admin:/>change remote_replication second_fs_access remote_replication_id=2100ef02030405060000000200000000 access=read_write
Command executed successfully.
```

##### System Response

None
