# show unix_group general


##### Function

The **show unix_group general** command is used to query the information of UNIX groups.

##### Format

**show unix_group general** \[ name=? \]

##### Parameters

| Parameter | Description             | Value                                                                                                                                                                     |
|-----------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?    | Name of the UNIX group. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |

##### Usage Guidelines

None

##### Example

Query information about all UNIX groups.

```text
admin:/>show unix_group general
Group ID Group Type Group Name
-------- ---------- ----------
99999    Default    Administrators
100000   Default    default_group
100001   Create     group1
```

Query information about the UNIX group with a specified name.

```text
admin:/>show unix_group general name=group1
Group ID : 100001
Group Name : group1
Group Type : Create
Description :
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                        |
|-------------|--------------------------------|
| Group ID    | ID of the UNIX group.          |
| Group Type  | Type of the UNIX group.        |
| Group Name  | Name of the UNIX group.        |
| Description | Description of the UNIX group. |
