# create ldap configuration


##### Function

The **create ldap configuration** command is used to configure the attributes associated with Lightweight Directory Application Protocol (LDAP) servers.

##### Format

**create ldap configuration** type=? \[ ip_list=? \| port=? \] \[ base_dn=? \] \[ bind_dn=? \] \[ bind_password=? \] \[ user_search_path=? \] \[ over_ssl=? \] \[ user_id_attr=? \| user_name_attr=? \| group_id_attr=? \| group_name_attr=? \| group_member_attr=? \| user_objectclass=? \| group_objectclass=? \| group_search_path=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Type of the LDAP server. | The value is case-insensitive and can be "LDAP" or "AD", where: <br>"LDAP": common LDAP protocol.<br>"AD": Active Directory (AD) protocol. |
| ip_list=? | LDAP server IP address list. | The value can be a maximum of four IP addresses separated by commas (,). You can access the LDAP server by using any of the listed IP addresses. |
| port=? | Listening port number of the LDAP server. | The value is an integer from1 to 65535. |
| base_dn=? | Base distinguished name (DN). This parameter defines a start point for searching on an LDAP directory server. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| bind_dn=? | DN bound with an LDAP server. If anonymous binding is not available for an LDAP server, you must bind DNs before you can retrieve the information on users or user groups. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| bind_password=? | Password for a bind DN. | The value contains 1 to 63 characters. |
| user_search_path=? | LDAP directory server path under which users will be searched for. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| group_search_path=? | LDAP directory server path under which user groups will be searched for. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| over_ssl=? | Whether to enable SSL communication for an LDAP server. | The value can be "yes" or "no", where: <br>"yes": The SSL function is used.<br>"no": The SSL function is not used.<br> The default value is "no". |
| user_id_attr=? | Attribute of a user ID. | The value contains 1 to 63 characters. The default value can be "uidNumber" or "uSNCreated", where: <br>The value is "uidNumber" when "type" is set to "LDAP".<br>The value is "uSNCreated" when "type" is set to "AD". |
| user_name_attr=? | Attribute of a user name. | The value contains 1 to 63 characters. The default value can be "uid" or "sAMAccountName", where: <br>The value is "uid" when "type" is set to "LDAP".<br>The value is "sAMAccountName" when "type" is set to "AD". |
| group_id_attr=? | Attribute of a user group ID. | The value contains 1 to 63 characters. The default value can be "gidNumber" or "uSNCreated", where: <br>The value is "gidNumber" when "type" is set to "LDAP".<br>The value is "uSNCreated" when "type" is set to "AD". |
| group_name_attr=? | Attribute of a user group name. | The value contains 1 to 63 characters. The default value can be "cn" or "sAMAccountName", where: <br>The value is "cn" when "type" is set to "LDAP".<br>The value is "sAMAccountName" when "type" is set to "AD". |
| group_member_attr=? | Attribute of a user group member name. | The value contains 1 to 63 characters. The default value can be "uniqueMember" or "ember", where: <br>The value is "uniqueMember" when "type" is set to "LDAP".<br>The value is "member" when "type" is set to "AD". |
| user_objectclass=? | Name of a class to which a user belongs. | The value contains 1 to 63 characters. The default value can be "posixAccount" or "user", where: <br>The value is "posixAccount" when "type" is set to "LDAP".<br>The value is "user" when "type" is set to "AD". |
| group_objectclass=? | Name of a class to which a user group belongs. | The value contains 1 to 63 characters. The default value can be "groupOfUniqueNames" or "group", where: <br>The value is "groupOfUniqueNames" when "type" is set to "LDAP".<br>The value is "group" when "type" is set to "AD". |

##### Usage Guidelines

-   Configurations of the LDAP server must be consistent with that on the storage server. Otherwise, LDAP functions may not work properly.
-   To ensure secure data transmission, you are advised to use Secure Sockets Layer (SSL) encryption.

##### Example

Configure the LDAP server, where: Server type: LDAP Server IP address list: 192.168.3.4 and 192.168.5.2 Employed listening port: 389 Base DN: cn=JohnDoe,ou=cd,dc=example,dc=com Bind DN: cn=Manager,ou=cq,dc=example,dc=com Password for the bind DN: 123456 Path under which users will be searched for: cn=emply Path under which user groups will be searched for: cn=emply SSL communication: enabled The remaining parameters are in their defaults.

```text
admin:/>create ldap configuration type=LDAP ip_list=192.168.3.4,192.168.5.2 port=389 base_dn=cn=JohnDoe,ou=cd,dc=example,dc=com bind_dn=cn=Manager,ou=cq,dc=example,dc=com bind_password=****** user_search_path=cn=emply over_ssl=yes
Command executed successfully.
```

##### System Response

None
