# show share_permission cifs


##### Function

The **show share_permission cifs** command is used to query the permissions of a CIFS share.

##### Format

**show share_permission cifs** { share_permission_id=? \| share_id=? \| share_name=? access_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_permission_id=? | Share permission ID. | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| share_id=? | Share ID. | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| share_name | CIFS share name. | The value consists of 1 to 80 characters excluding \"/\\[]:|<>+;,?*=. |
| access_name | Access name, which can be a resource user or user group, AD domain user or user group, LDAP domain user or user group, or NIS domain user or user group. Multiple users or user groups are separated by commas (,). | The value contains 1 to 288 characters.<br>Add special character @ before a resource user group name, LDAP domain user group name, or NIS domain user group name to distinguish it from a resource user name, LDAP domain user name, or NIS domain user name.<br>The name of an AD domain user or user group must be in the format of Domain name\\Domain user name or @Domain name\\Domain user group name.<br>The type of an LDAP or NIS domain user or user group must be specified by parameter "domain_type=?". |

##### Usage Guidelines

Parameters "share_permission_id", "share_name", and "share_id" are mutually exclusive.

##### Example

Query information about all permissions associated with a CIFS share.

```text
admin:/>show share_permission cifs share_id=4
Share Permission ID  Access Name  Share ID  Domain Type  Permission Type  Share Name
-------------------  -----------  --------  -----------  ---------------  ----------
17179869188          hwuser1      4         LOCAL        Read Write       share3
```

Query information about the CIFS share permission whose ID is "1".

```text
admin:/>show share_permission cifs share_permission_id=1

Share Permission ID : 1
Access Name         : hwuser1
Share ID            : 4
Domain Type         : LOCAL
Permission Type     : Read Write
Share Name          : share3
```

Query information about the CIFS share permission whose ID is "3".

```text

admin:/>show share_permission cifs share_permission_id=3

Share Permission ID : 3
Access Name         : hwuser1
Share ID            : 3
Domain Type         : LOCAL
Permission Type     : Read Write
Share Name          : share1

```

Query information about all permissions associated with a CIFS share.

```text
admin:/>show share_permission cifs share_name=share3
Share Permission ID  Access Name  Share ID  Domain Type  Permission Type  Share Name
-------------------  -----------  --------  -----------  ---------------  ----------
17179869188          hwuser1      4         LOCAL        Read Write       share3
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning                                                                                            |
|---------------------|----------------------------------------------------------------------------------------------------|
| Share Permission ID | Share permission ID.                                                                               |
| Access Name         | User or user group of the share permission.                                                        |
| Share ID            | Share ID.                                                                                          |
| Domain Type         | User or user group type. The value can be "local", "AD", "LDAP", and "NIS".                        |
| Permission Type     | Share permission type. The value can be "read_only", "read_write", "no_access", and "all_control". |
| Share Name          | CIFS share name.                                                                                   |
