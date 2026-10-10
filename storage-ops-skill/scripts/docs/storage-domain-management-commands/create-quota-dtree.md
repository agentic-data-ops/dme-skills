# create quota dtree


##### Function

The **create quota dtree** command is used to create a quota for a specified dtree.

##### Format

**create quota dtree** dtree_id=? quota_type=? \[ user_name=? \] \[ group_name=? \] \[ user_group_type=? \] \[ domain_type=? \] { space_hard_quota=? \| space_soft_quota=? \| file_hard_quota=? \| file_soft_quota=? }

**create quota dtree** dtree_name=? file_system_name=? quota_type=? \[ user_name=? \] \[ group_name=? \] \[ user_group_type=? \] \[ domain_type=? \] { space_hard_quota=? \| space_soft_quota=? \| file_hard_quota=? \| file_soft_quota=? }

**create quota dtree** dtree_name=? file_system_name=? quota_type=? \[ user_name=? \] \[ group_name=? \] \[ user_group_type=? \] \[ domain_type=? \] { space_hard_quota=? \| space_soft_quota=? \| file_hard_quota=? \| file_soft_quota=? } \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| dtree_id=? | Dtree ID. | The value is in the format of "File system ID@Dtree ID", where a file system ID ranges from 0 to 65535. To obtain the value, run the "show dtree general" command. |
| dtree_name=? | Dtree name. | The value contains 1 to 255 characters, including letters, digits, spaces, and special characters !\"#&%$'()*+-.;<=>?@[]^_`{|}~. On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. To obtain the value, run the "show dtree general" command. |
| file_system_name=? | File system name. | To obtain the value, run "show file_system general". |
| quota_type=? | Quota type. | The value can be "directory", "user", or "group". |
| user_name=? | User name. | The value contains 1 to 128 characters. To obtain the local user name, run the "show unix_user general" command. To obtain the local Windows user name, run the "show windows_user general" command. For an AD domain user, the format is "Domain\\User name". You can enter an asterisk (*) to indicate all users. |
| group_name=? | User group name. | The value contains 1 to 128 characters. To obtain the value, run the "show unix_group general" command. You can enter an asterisk (*) to indicate all user group names. |
| user_group_type=? | User type or user group type. | The value can be "local" or "domain", where: <br>"local": local user or local user group.<br>"domain": domain user or domain user group. |
| domain_type=? | Domain type. | The value can be "local_user", "local_user_group", "domain_user", or "domain_user_group", where: <br>"local_user": local user.<br>"local_user_group": local user group.<br>"domain_user": domain user.<br>"domain_user_group": domain user group. |
| space_hard_quota=? | Space hard quota. | The value must be greater than the space soft quota, and smaller than or equal to 256 PB.The unit can be MB, GB, TB. |
| space_soft_quota=? | Space soft quota. | The value must be smaller than the hard space quota. If the hard space quota is not specified, the value must be smaller than or equal to 256PB.The unit can be MB, GB, TB. |
| file_hard_quota=? | File quantity hard quota, expressed in thousand (K). | The value must be greater than the file quantity soft quota, and smaller than or equal to 2,000,000K. |
| file_soft_quota=? | File quantity soft quota, expressed in thousand (K). | The value must be smaller than the file quantity hard quota. If the file quantity hard quota is not specified, the value must be smaller than or equal to 2,000,000K. |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

-   When "quota_type" is set to "directory", a default directory quota is created for dtrees. In this case, parameters "user_name", "group_name", and "user_group_type" do not need to be specified.
-   When "quota_type" is set to "user", a user quota is created for dtrees.
-   To create a quota for a local user, set "user_group_type" to "local". In this case, parameter "user_name" must be specified. You can enter an asterisk (\*) for "user_name" to create a default quota for all local users.
-   To create a default quota for users in a local user group, set "user_group_type" to "local". In this case, parameter "group_name" must be specified. You can enter an asterisk (\*) for "group_name" to create a default quota for all local user groups.
-   To create a quota for a domain user, set "user_group_type" to "domain". In this case, parameters "user_name" and "domain_type" (used to specify the domain type) must be specified. You can enter an asterisk (\*) for "user_name" to create a default quota for all domain users.
-   To create a default quota for domain users in a domain user group, set "user_group_type" to "domain". In this case, parameters "group_name" and "domain_type" (used to specify the domain type) must be specified. You can enter an asterisk (\*) for "group_name" to create a default quota for all domain user groups.
-   When "quota_type" is set to "group", a user group quota is created for the file system.
-   To create a quota for a local user group, set "user_group_type" to "local". In this case, parameter "group_name" must be specified. You can enter an asterisk (\*) for "group_name" to create a default quota for all local user groups.
-   To create a quota for a domain user group, set "user_group_type" to "domain". In this case, parameters "group_name" and "domain_type" (used to specify the domain type) must be specified. You can enter an asterisk (\*) for "group_name" to create a default quota for all domain user groups.
-   You cannot create a quota for user groups in the AD domain.

##### Example

Create a quota for the dtree with ID "1@1", where the quota type is "directory" and space hard quota is 1 GB.

```text
admin:/>create quota dtree dtree_id=1@1 quota_type=directory space_hard_quota=1GB
Command executed successfully.
```

Create a quota for local resource user "engineerA" in the dtree with ID "1@4097", where the quota type is "user" and space hard quota is 1 GB.

```text
admin:/>create quota dtree dtree_id=1@4097 quota_type=user user_group_type=local user_name=engineerA space_hard_quota=1GB
Command executed successfully.
```

##### System Response

None
