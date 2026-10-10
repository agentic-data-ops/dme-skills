# change domain ldap_schema


##### Function

The **change domain ldap_schema** command is used to modify LDAP domain authentication advanced configurations.

##### Format

**change domain ldap_schema** { posixaccount_objectclass=? \| posixgroup_objectclass=? \| nisnetgroup_objectlass=? \| uid_attribute=? \| uidnumber_attribute=? \| gidnumber_attribute=? \| cn_group_attribute=? \| cn_netgroup_attribute=? \| memberuid_attribute=? \| member_nisnetgroup_attribute=? \| nisnetgroup_triple_attribute=? \| enable_rfc2307bis=? \| groupof_uniquenames_objectclass=? \| uniquemember_attribute=? \| schema=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| posixaccount_objectclass | User object. | - |
| posixgroup_objectclass | User group object. | - |
| nisnetgroup_objectclass | Network group object. | - |
| uid_attribute | uid attribute. | - |
| uidnumber_attribute | uidNumber attribute. | - |
| memberuid_attribute | memberUid attribute. | - |
| cn_netgroup_attribute | Network group CN attribute. | - |
| cn_group_attribute | Group CN attribute. | - |
| gidnumber_attribute | gidNumber attribute. | - |
| member_nisnetgroup_attribute | memberNisNetgroup attribute. | - |
| nisnetgroup_triple_attribute | nisNetgroupTriple attribute. | - |
| enable_rfc2307bis | Whether RFC2307bis is supported. | false: not supported true: supported. |
| groupof_uniquenames_objectclass | groupOfUniqueNames object. | - |
| uniquemember_attribute | uniqueMember object. | - |
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

Modify information about the schema configuration of LDAP domain authentication.

```text

admin:/>change domain ldap_schema posixaccount_objectclass=User posixgroup_objectclass=Group nisnetgroup_objectlass=nisNetgroup uid_attribute=uid uidnumber_attribute=uidNumber gidnumber_attribute=gidNumber

cn_group_attribute=cn
cn_netgroup_attribute=name memberuid_attribute=memberUid member_nisnetgroup_attribute=memberNisNetgroup nisnetgroup_triple_attribute=nisNetgroupTriple enable_rfc2307bis=yes groupof_uniquenames_objectclass=GroupOfUniqueNames
uniquemember_attribute=uniqueMember
Command executed successfully.

```

##### System Response

None
