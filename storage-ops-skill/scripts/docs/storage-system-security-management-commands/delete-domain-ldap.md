# delete domain ldap


##### Function

The **delete domain ldap** command is used to delete the configuration of the LDAP domain.

##### Format

**delete domain ldap**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the LDAP configuration before it is deleted.

```text
admin:/>show domain ldap

IP Address List : 10.129.70.1
Base DN         : dc=huawei,dc=com
Port            : 389
Password Hash   : Md5
Transfer Type   : LDAPS
User Suffix     : dc=huawei,dc=com
Group Suffix    : dc=huawei,dc=com
Shadow Suffix   : dc=huawei,dc=com
Timelimit       : 3
Bind Timelimit  : 3
Idle Timelimit  : 30
Bind DN         : cn=root,dc=huawei,dc=com
```

Delete the LDAP configuration.

```text
admin:/>delete domain ldap
Command executed successfully.
```

Query the LDAP configuration after it is deleted.

```text
admin:/>show domain ldap

IP Address List :
Base DN         :
Port            :
Password Hash   : --
Transfer Type   : --
User Suffix     :
Group Suffix    :
Shadow Suffix   :
Timelimit       : 3
Bind Timelimit  : 3
Idle Timelimit  : 30
Bind DN         :
```

##### System Response

None
