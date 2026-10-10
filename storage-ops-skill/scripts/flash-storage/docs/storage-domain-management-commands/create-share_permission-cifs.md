# create share_permission cifs


##### Function

The **create share_permission cifs** command is used to create a CIFS share permission.

##### Format

**create share_permission cifs** access_name=? { share_id=? \| share_name=? } permission_type=? \[ domain_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| access_name=? | Access name, which can be a resource user or user group, AD domain user or user group, LDAP domain user or user group, or NIS domain user or user group. Multiple users or user groups are separated by commas (,). | The value contains 1 to 288 characters.<br>Add special character @ before a resource user group name, LDAP domain user group name, or NIS domain user group name to distinguish it from a resource user name, LDAP domain user name, or NIS domain user name.<br>The name of an AD domain user or user group must be in the format of domain name\\domain user name or @domain name\\domain user group name.<br>The type of an LDAP or NIS domain user or user group must be specified by parameter "domain_type=?". |
| share_id=? | Share ID. | The value is an integer ranging from 0 to 18,446,744,073,709,551,615. |
| permission_type=? | Permission type. | The value can be "read_only", "read_write", "no_access", or "all_control", where: <br>read_only: The user has the read-only permission.<br>read_write: The user has the read and write permission.<br>no_access: The user has no permission.<br>all_control: The user has the read and write permission and can change the permission. |
| domain_type=? | User or user group type. | The value can be "Local", "AD", "LDAP", or "NIS", where: <br>"AD": AD domain user or user group.<br>"LDAP": LDAP domain user or user group.<br>"Local": local user or user group.<br>"NIS": NIS domain user or user group. |
| share_name=? | CIFS share name. | The value consists of 1 to 80 characters excluding \"/\\[]:|<>+;,?*=. |

##### Usage Guidelines

Parameters "access_name", "share_id" or "share_name", and "permission_type" must be entered at the same time.

##### Example

Create a CIFS share permission with "access_name" being a resource user.

```text
admin:/>create share_permission cifs access_name=user1 share_id=4 permission_type=all_control
Command executed successfully.
```

Create a CIFS share permission with "access_name" being a resource user group.

```text
admin:/>create share_permission cifs access_name=@group1 share_id=4 permission_type=all_control
Command executed successfully.
```

Create a CIFS share permission with "access_name" being an AD domain user.

```text
admin:/>create share_permission cifs access_name=trust-a\\aduser01 share_id=4 permission_type=all_control
Command executed successfully.
```

Create a CIFS share permission with "access_name" being an AD domain user group.

```text
admin:/>create share_permission cifs access_name=@trust-a\\adgroup01 share_id=4 permission_type=all_control
Command executed successfully.
```

Create a CIFS share permission with "access_name" being an NIS domain user.

```text
admin:/>create share_permission cifs access_name=user2 share_id=4 permission_type=all_control domain_type=NIS
Command executed successfully.
```

Create a CIFS share permission with "access_name" being an LDAP domain user group.

```text
admin:/>create share_permission cifs access_name=@group2 share_id=4 permission_type=all_control domain_type=LDAP
Command executed successfully.
```

Query the permission creation result.

```text
admin:/>show share_permission cifs share_id=4
Share Permission ID Access Name Share ID Domain Type Permission Type
------------------- ----------- -------- ----------- ---------------
1 user1 4 Local All Control
2 @group1 4 Local All Control
3 trust-a\aduser01 4 AD All Control
4 @trust-a\adgroup01 4 AD All Control
5 user2 4 NIS All Control
6 @group2 4 LDAP All Control
```

Create a CIFS share permission with "access_name" being a resource user.

```text
admin:/>create share_permission cifs access_name=user1 share_name=cifs2 permission_type=all_control
Command executed successfully.
```

Create CIFS share permissions with "access_name" being multiple users or user groups.

```text
admin:/>create share_permission cifs access_name=user1,user2,@group1 share_name=cifs2 permission_type=all_control
Command executed successfully.
```

##### System Response

None
