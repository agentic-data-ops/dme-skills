# change remote_device user_password


##### Function

The "**change remote_device user_password**" command is used to change the user's password that logging in to remote device.

##### Format

**change remote_device user_password** remote_device_id=? remote_user=?

##### Parameters

| Parameter          | Description                                  | Value                                                                                                                                                                                                                                |
|--------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| remote_device_id=? | ID of a remote device.                       | To obtain the value, run "show remote_device general".                                                                                                                                                                               |
| remote_user=?      | User name used to log in to a remote device. | The value consists of 5 to 32 ASCII characters, including digits, letters, and underscores (\_), and must start with a letter. To create a required remote device administrator, run the "create user" command on the remote device. |

##### Usage Guidelines

Description of accounts used for communication authentication between remote devices:

-   You need to create an authentication account on remote devices rather than local devices.
-   The authentication account must be a remote device administrator. Run the "create user" command to create one and set the role ID to 12.

##### Example

Change the password of the logged-in "admin" user to "remote@storage", where the remote device ID is "0".

```text
admin:/>change remote_device user_password remote_device_id=0 remote_user=admin
Password:**************
Reenter password:**************
Command executed successfully.
```

##### System Response

None
