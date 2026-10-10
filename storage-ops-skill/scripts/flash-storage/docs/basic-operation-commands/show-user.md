# show user


##### Function

The **show user** command is used to check basic information about users.

##### Format

**show user** \[ user_name=? \]

##### Parameters

| Parameter   | Description                              | Value                                                                                                                                                               |
|-------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| user_name=? | Name of the user that you want to query. | To obtain the value, run "**show user**" without parameters. |

##### Usage Guidelines

-   The super administrator can query all users' basic information, whereas others can query only their own basic information.
-   To query the basic information on existing users, run "**show user**".
-   To query the basic information on a specific user, run "**show user** user_name=?".

##### Example

Query the basic information about all users.

```text
admin:/>show user

Name                 Status   Type                     Lock Status  Create Time                    Domain User Group  Account Status  Role ID  Login Method                               Login Factor       Email
-----------------    -------  -----------------------  -----------  -----------------------------  -----------------  --------------  -------  -----------------------------------------  -----------------  --------------
admin                Online   Local                    Unlocked     2018-08-13/15:36:40 UTC+08:00  --                 Normal          1        CLI,SFTP,DeviceManager,RESTful,SerialPort  password_emailOTP  test@test.com
```

Query the basic information about user "admin".

```text
admin:/>show user user_name=admin

Name    Status  Type   Lock Status  Create Time                    Domain User Group  Account Status  Role ID  Login Method                               Login Factor  Email
-----   ------  -----  -----------  -----------------------------  -----------------  --------------  -------  -----------------------------------------  ------------  -------
admin   Online  Local  Unlocked     2018-08-13/15:36:40 UTC+08:00  --                 Normal          1        CLI,SFTP,DeviceManager,RESTful,SerialPort  password      --
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Name | User name. |
| Status | Whether the user has logged in. |
| Type | User type. |
| Lock Status | Whether the user is locked. |
| Create Time | Time when a user is created. |
| Domain User Group | Domain user group the user belongs to. NOTE: This parameter is currently valid for LDAP users only. |
| Account Status | User account status. |
| Role ID | User role ID. |
| Login Method | Valid login method set for a user. |
| Is Password Never Expire | Whether a password never expires. |
| Login Factor | Authentication factor type of a user. |
| Email | Email address for receiving the email one-time password. |
