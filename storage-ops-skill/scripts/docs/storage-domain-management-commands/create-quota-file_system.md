# create quota file_system


##### Function

The **create quota file_system** command is used to create a quota for a file system.

##### Format

**create quota file_system** { file_system_name=? \| file_system_id=? } quota_type=? \[ user_group_type=? \] \[ user_name=? \] \[ group_name=? \] \[ domain_type=? \] { space_hard_quota=? \| space_soft_quota=? \| file_hard_quota=? \| file_soft_quota=? } \*

**create quota file_system** { file_system_name=? \| file_system_id=? } quota_type=? \[ user_group_type=? \] \[ user_name=? \] \[ group_name=? \] \[ domain_type=? \] { space_hard_quota=? \| space_soft_quota=? \| file_hard_quota=? \| file_soft_quota=? } \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| file_system_id=? | File system ID. | To obtain the value, run the "show file_system general" command. |
| file_system_name=? | File system name. | To obtain the value, run the "show file_system general" command. |
| quota_type=? | Quota type. | The value can be "directory", "user", or "group". |
| user_name=? | User name. | The value contains 1 to 128 characters. To obtain the local user name, run the "show unix_user general" command. To obtain the local Windows user name, run the "show windows_user general" command. For an AD domain user, the format is "Domain\\User name". You can enter an asterisk (*) to indicate all users. |
| group_name=? | User group name. | The value contains 1 to 128 characters. To obtain the local user group name, run the "show unix_group general" command. You can enter an asterisk (*) to indicate all user groups. |
| user_group_type=? | User type or user group type. | The value can be "local" or "domain", where: <br>"local": local user and local user group.<br>"domain": domain user and domain user group. |
| domain_type=? | Domain type. | The value can be "local", "ad", "ldap", or "nis", where. <br>"local": local domain.<br>"ad": AD domain.<br>"ldap": LDAP domain.<br>"nis": NIS domain. |
| space_hard_quota=? | Space hard quota. | The value must be greater than the space soft quota, and smaller than or equal to 256 PB. The unit can be MB, GB, or TB. |
| space_soft_quota=? | Space soft quota. | The value must be smaller than the space hard quota. If the space hard quota is not specified, the value must be smaller than or equal to 256 PB. The unit can be MB, GB, or TB. |
| file_hard_quota=? | File quantity hard quota, expressed in thousand (K). | The value must be greater than the file quantity soft quota, and smaller than or equal to 2,000,000. |
| file_soft_quota=? | File quantity soft quota, expressed in thousand (K). | The value must be smaller than the file quantity hard quota. If the file quantity hard quota is not specified, the value must be smaller than or equal to 2,000,000. |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

-   When "quota_type" is set to "directory", a default directory quota is created for dtrees. In this case, "user_name" and "group_name" do not need to be specified.
-   When "quota_type" is set to "user", a quota is created for users in dtrees.
-   To create a quota for a local user, set "user_group_type" to "local_user". In this case, "user_name" must be specified and "group_name" does not need to be specified. You can enter an asterisk (\*) for "group_name" to create a default quota for all local users.
-   To create a default quota for users in a local user group, set "user_group_type" to "local_user_group". In this case, "group_name" must be specified and "user_name" does not need to be specified.
-   To create a quota for a domain user, set "user_group_type" to "domain_user". In this case, "user_name" and "domain_type" must be specified and "group_name" does not need to be specified. You can enter an asterisk (\*) for "group_name" to create a default quota for all domain users.
-   To create a default quota for domain users in a domain user group, set "user_group_type" to "domain_user_group". In this case, "group_name" and "domain_type" must be specified and "user_name" does not need to be specified.
-   When "quota_type" is set to "group", a quota is created for user groups in the file system.
-   To create a quota for a local user group, "group_name" and "user_group_type" must be specified and "user_name" does not need to be specified. You can enter an asterisk (\*) for "group_name" to create a default quota for all local user groups in the file system.
-   To create a quota for a domain user group, "group_name", "user_group_type", and "domain_type" must be specified and "user_name" does not need to be specified. You can enter an asterisk (\*) for "group_name" to create a default quota for all domain user groups in the file system.
-   You cannot create a quota for user groups in the AD domain.

##### Example

Create a default directory quota for the file system whose ID is "1", where the quota type is set to "directory", and the space hard quota is 1 GB.

```text
admin:/>create quota file_system file_system_id=1 quota_type=directory space_hard_quota=1GB
Command executed successfully.
```

##### System Response

None
