# change user_password


##### Function

The **change user_password** command is used to change current user's logging password.

##### Format

**change user_password**

##### Parameters

None

##### Usage Guidelines

-   The password consists of 8 to 16 characters and is case-sensitive.
-   The password must contain special characters including\` \~ ! @ \# $ % ^ & \* ( ) - \_ = + \\ \| \[ { } \] ; :' " , \< . \> / ? and space.
-   The password must meet password complexity requirements:
-   When "password complex" is set to "Normal", the password must contain at least two of the following three: lowercase character, uppercase character, and number.
-   when "password complex" is set to "High", the password must contain lowercase character, uppercase character, and number.
-   The password must be different from the user name and the username in reversed order.
-   One character must not appear for more than three times consecutively.

 

You can use the "change safe_strategy" command to change the password and login policies of a storage system.

##### Example

Change the password of the logged-in "admin" user.

```text
admin:/>change user_password
Old password:*********
New password:*************
Reenter password:*************
Command executed successfully.
```

##### System Response

None
