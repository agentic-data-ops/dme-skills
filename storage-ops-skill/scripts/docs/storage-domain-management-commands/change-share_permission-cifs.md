# change share_permission cifs


##### Function

The **change share_permission cifs** command is used to change the type of a CIFS share permission.

##### Format

**change share_permission cifs** share_permission_id=? permission_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_permission_id=? | Share permission ID. | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| permission_type=? | Permission type. | The value can be "read_only", "read_write", "no_access", or "all_control", where: <br>"read_only": read-only.<br>"read_write": read and write.<br>"no_access": no permission.<br>"all_control": The user has the read and write permissions and can change the permission. |

##### Usage Guidelines

None

##### Example

Query a CIFS share permission before the modification.

```text
admin:/>show share_permission cifs share_permission_id=1
Share Permission ID : 1
Access Name : user1
Share ID : 4
Domain Type : Local
Permission Type : Read Only
```

Change the type of a CIFS share permission.

```text
admin:/>change share_permission cifs share_permission_id=1 permission_type=all_control
Command executed successfully.
```

Query a CIFS share permission after the modification.

```text
admin:/>show share_permission cifs share_permission_id=1
Share Permission ID : 1
Access Name : user1
Share ID : 4
Domain Type : Local
Permission Type : All Control
```

##### System Response

None
