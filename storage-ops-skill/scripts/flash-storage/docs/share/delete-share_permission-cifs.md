# delete share_permission cifs


##### Function

The **delete share_permission cifs** command is used to delete a CIFS share permission.

##### Format

**delete share_permission cifs** { share_permission_id=? \| share_name=? domain_type=? access_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_permission_id=? | Share permission ID. | The value is an integer. |
| share_name=? | Name of the CIFS share. | The value consists of 1 to 80 characters excluding \"/\\[]:|<>+;,?*=. |
| domain_type=? | User or user group type. NOTE: This parameter is not supported by the current version. The execution result is invalid. | The value can be "Local", "AD", "LDAP", or "NIS", where: <br>"AD": AD domain user or user group.<br>"LDAP": LDAP domain user or user group.<br>"Local": local user or user group.<br>"NIS": NIS domain user or user group. |
| access_name=? | Access name, which can be a resource user or user group, AD domain user or user group, LDAP domain user or user group, or NIS domain user or user group. Multiple users or user groups are separated by commas (,). | The value contains 1 to 288 characters.<br>Add special character @ before a resource user group name, LDAP domain user group name, or NIS domain user group name to distinguish it from a resource user name, LDAP domain user name, or NIS domain user name.<br>The name of an AD domain user or user group must be in the format of domain name\\domain user name or @domain name\\domain user group name.<br>The type of an LDAP or NIS domain user or user group must be specified by parameter "domain_type=?". |

##### Usage Guidelines

Parameters share_permission_id or share_name,domain_type and access_name must be entered.

##### Example

Delete a CIFS share permission.

```text
admin:/>delete share_permission cifs share_permission_id=12884901890
Command executed successfully.
```

Delete a CIFS share permission.

```text
admin:/>delete share_permission cifs share_name=cifs1 domain_type=Local access_name=user1
Command executed successfully.
```

Delete CIF share permissions.

```text
admin:/>delete share_permission cifs share_name=cifs1 domain_type=Local access_name=user1,user2
Command executed successfully.
```

##### System Response

None
