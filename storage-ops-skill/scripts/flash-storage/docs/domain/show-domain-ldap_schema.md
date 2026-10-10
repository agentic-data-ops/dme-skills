# show domain ldap_schema


##### Function

The **show domain ldap_schema** command is used to query LDAP domain authentication advanced configurations.

##### Format

**show domain ldap_schema** \[ schema=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| schema | LDAP schema template. | The value can be "RFC2307" or "AD_IDMU", where: <br>"RFC2307":The schema template of LDAP is RFC2307.<br>"AD_IDMU":The schema template of LDAP is AD_IDMU. |

##### Usage Guidelines

None

##### Example

Query information about the schema configuration of LDAP domain authentication.

```text
admin:/>show domain ldap_schema
RFC2307 posixAccount Object Class : User
RFC2307 posixGroup Object Class : Group
RFC2307 nisNetgroup Object Class : nisNetgroup
RFC2307 uid Attribute : uid
RFC2307 uidNumber Attribute : uidNumber
RFC2307 gidNumber Attribute : gidNumber
RFC2307 cn(for Groups) Attribute : cn
RFC2307 cn(for Netgroups) Attribute : name
RFC2307 memberUid Attribute : memberUid
RFC2307 memberNisNetgroup Attribute :  memberNisNetgroup
RFC2307 nisNetgroup Triple Attribute : nisNetgroupTriple
Enable Support RFC2307bis : False
RFC2307bis GroupOfUniqueNames Object Class : GroupOfUniqueNames
RFC2307bis uniqueMember Attribute : uniqueMember
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                  | Meaning                                     |
|--------------------------------------------|---------------------------------------------|
| RFC2307 posixAccount Object Class          | RFC2307 posixAccount Object Class.          |
| RFC2307 posixGroup Object Class            | RFC2307 posixGroup Object Class.            |
| RFC2307 nisNetgroup Object Class           | RFC2307 nisNetgroup Object Class.           |
| RFC2307 uid Attribute                      | RFC2307 uid Attribute.                      |
| RFC2307 uidNumber Attribute                | RFC2307 uidNumber Attribute.                |
| RFC2307 gidNumber Attribute                | RFC2307 gidNumber Attribute.                |
| RFC2307 cn(for Groups) Attribute           | RFC2307 cn(for Groups) Attribute.           |
| RFC2307 cn(for Netgroups) Attribute        | RFC2307 cn(for Netgroups) Attribute.        |
| RFC2307 memberUid Attribute                | RFC2307 memberUid Attribute.                |
| RFC2307 memberNisNetgroup Attribute        | RFC2307 memberNisNetgroup Attribute.        |
| RFC2307 nisNetgroup Triple Attribute       | RFC2307 nisNetgroup Triple Attribute.       |
| Enable Support RFC2307bis                  | Whether the RFC2307bis is supported.        |
| RFC2307bis GroupOfUniqueNames Object Class | RFC2307bis groupOfUniqueNames Object Class. |
| RFC2307bis uniqueMember Attribute          | RFC2307bis uniqueMember Attribute.          |
