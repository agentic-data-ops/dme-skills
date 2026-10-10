# change ldap configuration


##### Function

The **change ldap configuration** command is used to modify the configuration of Lightweight Directory Application Protocol (LDAP) servers.

##### Format

**change ldap configuration** { type=? \| ip_list=? \| port=? \| over_ssl=? \| base_dn=? \| bind_dn=? \| bind_password=? \| user_search_path=? \| group_search_path=? \| user_id_attr=? \| user_name_attr=? \| group_id_attr=? \| group_name_attr=? \| group_member_attr=? \| user_objectclass=? \| group_objectclass=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Type of the LDAP server. | The value is case-insensitive and can be "LDAP" or "AD", where: <br>"LDAP": indicates the common openLDAP protocol.<br>"AD": indicates the Active Directory (AD) protocol. |
| ip_list=? | IP addresses of employed LDAP servers. | The value can be a maximum of four IP addresses separated by commas (,). You can access the LDAP server by using any of the listed IP addresses. |
| port=? | ID of the employed listening port on an LDAP server. | The value is an integer between 1 and 65535. |
| over_ssl=? | Whether to enable SSL communication for an LDAP server. | The value can be "yes" or "no", where: <br>"yes": The SSL function is used.<br>"no": The SSL function is not used.<br> The default value is "no". |
| base_dn=? | A basic distinguished name (DN). This parameter defines a start point for searching on an LDAP directory server. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| bind_dn=? | A DN bound with an LDAP server. If anonymous binding is not available for an LDAP server, you must bind DNs before you can retrieve the information on users or user groups. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| bind_password=? | A password for a bound DN. | The value contains 1 to 63 characters. |
| user_search_path=? | An LDAP directory server path under which users will be searched for. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| group_search_path=? | An LDAP directory server path under which user groups will be searched for. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| user_id_attr=? | Attribute of a user ID. | The value contains 1 to 63 characters. The default value can be "uidNumber" or "uSNCreated", where: <br>"uidNumber" when type=? is set to LDAP.<br>"uSNCreated" when type=? is set to AD. |
| user_name_attr=? | Attribute of a user name. | The value contains 1 to 63 characters. The default value can be "uid" or "sAMAccountName", where: <br>"uid" when type=? is set to LDAP.<br>"sAMAccountName" when type=? is set to AD. |
| group_id_attr=? | Attribute of a user group ID. | The value contains 1 to 63 characters. The default value can be "gidNumber" or "uSNCreated", where: <br>"gidNumber" when type=? is set to LDAP.<br>"uSNCreated" when type=? is set to AD. |
| group_name_attr=? | Attribute of a user group name. | The value contains 1 to 63 characters. The default value can be "cn" or "sAMAccountName", where: <br>"cn" when type=? is set to LDAP.<br>"sAMAccountName" when type=? is set to AD. |
| group_member_attr=? | Attribute of a user group member name. | The value contains 1 to 63 characters. The default value can be "uniqueMember" or "member", where: <br>"uniqueMember" when type=? is set to LDAP.<br>"member" when type=? is set to AD. |
| user_objectclass=? | Name of a class to which a user belongs. | The value contains 1 to 63 characters. The default value can be "posixAccount" or "user", where: <br>"posixAccount" when type=? is set to LDAP.<br>"user" when type=? is set to AD. |
| group_objectclass=? | Name of a class to which a user group belongs. | The value contains 1 to 63 characters. The default value can be "groupOfUniqueNames" or "group", where: <br>"groupOfUniqueNames" when type=? is set to LDAP.<br>"group" when type=? is set to AD. |

##### Usage Guidelines

-   Configurations of the LDAP server must be consistent with that on the storage server. Otherwise, LDAP functions may not work properly.
-   To ensure secure data transmission, you are advised to use Secure Sockets Layer (SSL) encryption.

##### Example

Modify the information on an LDAP server, where SSL encryption will be enabled, updated password for the bound DN is "7654321", the updated path under which user groups will be searched for is "ou=newpath", and the ID of the updated employed port is "4320".

```text
admin:/>change ldap configuration over_ssl=yes bind_password=****** group_search_path=ou=newpath port=4320
Command executed successfully.
```

##### System Response

None
