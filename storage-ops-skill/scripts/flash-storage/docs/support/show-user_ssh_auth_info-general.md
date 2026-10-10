# show user_ssh_auth_info general


##### Function

The **show user_ssh_auth_info general** command is used to query the SSH authentication information about users.

##### Format

**show user_ssh_auth_info general** \[ user_name=? \]

##### Parameters

| Parameter   | Description                              | Value                                                                                                                                |
|-------------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| user_name=? | Name of the user that you want to query. | The value contains 1 to 64 ASCII characters, excluding double quotation marks ("). To obtain the value, run the "show user" command. |

##### Usage Guidelines

-   Run the "**show user_ssh_auth_info general**" command to query the SSH authentication information about all users.
-   Run the "**show user_ssh_auth_info general** user_name=?" command to query the SSH authentication information about a specified user.

##### Example

Query the SSH authentication information about all users.

```text
admin:/>show user_ssh_auth_info general

User Name       Auth Type     Fingerprint
--------------  ------------  -----------------------------------------------
admin           password      --
mm_user         password      --
testUser        publickey     29:b8:d9:a4:0c:a6:99:e2:c0:34:68:23:77:47:63:0f
```

Query the SSH authentication information about user "testUser".

```text
admin:/>show user_ssh_auth_info general user_name=testUser

User Name   : testUser
Auth Type   : publickey
Publickey   : ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDN9B+eG2I4+kYkyMz1yFZUHchHgNAR+uvntY
mt7iKhtG9tI9hi+SvTGohH3ddMip8kz5ZwaUryMUYnRh1pOMBk5zho6ar/EAbuz7xC6WCe43zz
axC1wvJiBHZTEH7UZPkaPt3FIhCKfv0hNWp0nMXa3AWyIVPrR0P5tDNO4dJtz+qcKwYV+/XggD
7YkGiCJzzRjLcSAN6mSSuI3SmsnPVkods+yaHzJ6244Ux2FefyiidOxY4Yxa/5Qbbipa3PpPr6
HnNOKnkPGkqM+xZW7KNJAyAEU63m/c1TpNaYz02AVLQiuAhbmvexQYgMcjviIE43f/D2Y6riRM
qAQJhVHnC9 root@Storage
Fingerprint : 29:b8:d9:a4:0c:a6:99:e2:c0:34:68:23:77:47:63:0f
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                  |
|-------------|--------------------------|
| User Name   | User name.               |
| Auth Type   | SSH authentication mode. |
| Publickey   | Public key.              |
| Fingerprint | Public key fingerprint.  |
