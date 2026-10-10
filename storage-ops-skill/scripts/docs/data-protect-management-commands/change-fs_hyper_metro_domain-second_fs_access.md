# change fs_hyper_metro_domain second_fs_access


##### Function

The **change fs_hyper_metro_domain second_fs_access** command is used to modify the access permission of the secondary end of a HyperMetro domain cluster.

##### Format

**change fs_hyper_metro_domain second_fs_access** domain_id=? access=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id=? | File system HyperMetro domain ID. | You can run the "show fs_hyper_metro_domain general" command to obtain the value. |
| access=? | Access permission of the secondary file system in the HyperMetro domain. | The value can be "no_access" or "read_write", where: <br>"no_access": Access is not allowed.<br>"read_write": read and write. |

##### Usage Guidelines

None

##### Example

Modify the access permission of the secondary end of the HyperMetro domain cluster. The domain ID is "48ad083e9b9f0100", and the permission is changed to Read and Write.

```text
admin:/>change fs_hyper_metro_domain second_fs_access domain_id=48ad083e9b9f0100 access=read_write
WARNING: You are about to change the access permission of the secondary file system in the HyperMetro domain cluster.
1. If the permission is changed to inaccessible, the secondary file system cannot provide services.
2. If the permission is changed to readable and writable, the secondary file system can provide services. After data is synchronized from the primary file system to the secondary file system, data newly written to the secondary file system will be overwritten.
Suggestion: N/A.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
