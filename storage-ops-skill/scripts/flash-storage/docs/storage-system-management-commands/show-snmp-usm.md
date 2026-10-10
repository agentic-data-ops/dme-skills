# show snmp usm


##### Function

The **show snmp usm** command is used to query the configuration of the USM user.

##### Format

**show snmp usm** \[ user_name=? \]

##### Parameters

| Parameter   | Description                                                                                      | Value                                                                                                                                                                       |
|-------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user_name=? | USM user name. If this parameter is specified, USM information on the specified user is queried. | To obtain the value, run "**show snmp usm**" without parameters. |

##### Usage Guidelines

-   To query configurations of all USM users, run "**show snmp usm**".
-   To query configurations of a specific USM user, run "**show snmp usm** user_name=?".

##### Example

Query configurations of all USM users.

```text
admin:/>show snmp usm
User Name Is Default Authenticate Protocol Private Protocol User Level
--------- ---------- --------------------- ---------------- -----------
User      No         MD5                   AES              Read Write
User2     No         MD5                   3DES             Read Write
```

##### System Response

The following table describes the parameter meanings.

| Parameter             | Meaning                                             |
|-----------------------|-----------------------------------------------------|
| User Name             | USM user name.                                      |
| Is Default            | Whether the user name is the default USM user name. |
| Authenticate Protocol | User authentication protocol.                       |
| Private Protocol      | User private protocol.                              |
| User Level            | User level.                                         |
