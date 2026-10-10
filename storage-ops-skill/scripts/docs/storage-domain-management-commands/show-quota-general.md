# show quota general


##### Function

The **show quota general** command is used to query quotas.

##### Format

**show quota general** { quota_id=? \| file_system_id=? \| dtree_id=? } \[ quota_type=? \]

**show quota general** { dtree_name=? \| file_system_name=? \| file_system_id=? \| dtree_id=? } \[ quota_type=? \] \[ vstore_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| quota_id=? | File system quota ID. | To obtain the value, run the "show quota general" command. |
| file_system_id=? | File system ID. | To obtain the value, run the "show file_system general" command. |
| file_system_name=? | File system name. | To obtain the value, run the "show file_system general" command. |
| dtree_id=? | Dtree ID. | The value is in the format of "File system ID@Dtree ID", where a file system ID ranges from 0 to 65535. To obtain the value, run the "show dtree general" command. |
| dtree_name=? | Dtree name. | The value contains 1 to 255 characters, including letters, digits, spaces, and special characters !\"#&%$'()*+-.;<=>?@[]^_`{|}~. On the CLI, the following characters need to be represented with escape sequences: "\|" indicates "|", "\\" indicates "\", "\q" indicates "?", and "\s" indicates a space. To obtain the value, run the "show dtree general" command. |
| quota_type | Quota type. | The value can be "directory", "user", or "group". <br>"directory": directory quota.<br>"user": user quota.<br>"group": group quota. |
| vstore_id=? | vStore ID. | vStore ID. The default value is "0". |

##### Usage Guidelines

-   Enter "quota_id" to delete a specified quota, without "quota_type" inputting.
-   Enter "file_system_id" to query all quotas of a file system. If "quota_type" is entered additionally, the command will show all quotas of this type in the file system.
-   Enter "dtree_id" to query all quotas of a specified dtree. If "quota_type" is entered additionally, the command will show all quotas of this type in the quota tree.

##### Example

Query all quotas in the file system whose ID is "1".

```text

admin:/>show quota general file_system_id=1

Quota ID  Dtree Name  Quota Type  User/Group Name  User/Group Type  Space Soft Quota  Space Hard Quota  File Soft Quota  File Hard Quota  Space Used  File Used  Space Used Rate(%)  File Used Rate(%) Domain Type
--------  ----------  ----------  ---------------  ---------------  ----------------  ----------------  ---------------  ---------------  ----------  ---------  ------------------  ----------------- -----------
1@3       All dtrees  Directory   --               --                         --                --               --              100          --         --                  --                 --        --

```

Query the directory quota of the dtree whose ID is "2@4097".

```text
admin:/>show quota general dtree_id=2@4097 quota_type=directory

Quota ID           : 2@4097@3
Dtree Name         : dtree
Quota Type         : Directory
User/Group Name    : --
User/Group Type    : --
Space Soft Quota   : 10.000GB
Space Hard Quota   : --
File Soft Quota    : 1000
File Hard Quota    : --
Space Used         : 0.000B
File Used          : 0
Space Used Rate(%) : 0
File Used Rate(%)  : 0
Domain Type        : --
```

Query the quota whose ID is "2@4097@3".

```text
admin:/>show quota general quota_id=2@4097@3

Quota ID           : 2@4097@3
Dtree Name         : dtree
Quota Type         : Directory
User/Group Name    : --
User/Group Type    : --
Space Soft Quota   : 100.000GB
Space Hard Quota   : 200.000GB
File Soft Quota    : 1000
File Hard Quota    : 2000
Space Used         : 0.000B
File Used          : 0
Space Used Rate(%) : 0
File Used Rate(%)  : 0
Domain Type        : --

```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                          |
|--------------------|----------------------------------|
| Quota ID           | Quota ID.                        |
| Dtree Name         | Dtree name.                      |
| Quota Type         | Quota type.                      |
| User/Group Name    | User name or user group name.    |
| User/Group Type    | User type or user group type.    |
| Domain Type        | Domain type.                     |
| Space Soft Quota   | Space soft quota.                |
| Space Hard Quota   | Space hard quota.                |
| File Soft Quota    | File quantity soft quota.        |
| File Hard Quota    | File quantity hard quota.        |
| Space Used         | Used space.                      |
| File Used          | Number of files that are in use. |
| Space Used Rate(%) | Space hard quota usage.          |
| File Used Rate(%)  | File quantity hard quota usage.  |
