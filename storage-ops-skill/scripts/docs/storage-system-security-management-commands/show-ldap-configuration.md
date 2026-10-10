# show ldap configuration


##### Function

The **show ldap configuration** command is used to query the configuration information on Lightweight Directory Application Protocol (LDAP) servers.

##### Format

**show ldap configuration**

##### Parameters

None

##### Usage Guidelines

None

##### Example

To query the configuration information on LDAP servers, run the following command.

```text
admin:/>show ldap configuration
IP List                 : 192.168.10.84
Port                    : 389
Server Type             : AD
Transfer Over SSL       : No
Root Directory          : dc=hvs,dc=com
Binding DN              : cn=administrator,cn=users,dc=hvs,dc=com
User Directory          : cn=users,dc=hvs,dc=com
Group Directory         : cn=users,dc=hvs,dc=com
User ID Properties      : uSNCreated
Username Properties     : sAMAccountName
Group ID Properties     : uSNCreated
Group Name Properties   : sAMAccountName
Group Member Properties : member
User Object Class       : user
Group Object Type       : group
```

##### System Response

The following table describes the parameter meanings.

| Parameter               | Meaning                                                                          |
|-------------------------|----------------------------------------------------------------------------------|
| IP List                 | \IP addresses of employed LDAP servers.                                      |
| Port                    | \ID of the employed listening port on an LDAP server.                        |
| Server Type             | \Type of the LDAP server.                                                    |
| Transfer Over SSL       | \Whether to enable SSL communication for an LDAP server.                     |
| Root Directory          | A basic distinguished name (DN).                                                 |
| Binding DN              | A DN bound with an LDAP server.                                                  |
| User Directory          | \An LDAP directory server path under which users will be searched for.       |
| Group Directory         | \An LDAP directory server path under which user groups will be searched for. |
| User ID Properties      | \Attribute of a user ID.                                                     |
| Username Properties     | \Attribute of a user name.                                                   |
| Group ID Properties     | \Attribute of a user group ID.                                               |
| Group Name Properties   | \Attribute of a user group name.                                             |
| Group Member Properties | \Attribute of a user group member name.                                      |
| User Object Class       | \Name of a class to which a user belongs.                                    |
| Group Object Type       | \Name of a class to which a user group belongs.                              |
