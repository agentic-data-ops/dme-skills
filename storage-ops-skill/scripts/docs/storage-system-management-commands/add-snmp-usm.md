# add snmp usm


##### Function

The **add snmp usm** command is used to add a USM user.

##### Format

**add snmp usm** user_name=? authenticate_protocol=? private_protocol=? \[ user_level=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| user_name=? | USM user name. | The value contains 4 to 32 ASCII characters, including digits, letters, underscores (_), or hyphens (-), and must start with a letter. |
| authenticate_protocol=? | Authentication protocol. | The value can be "SHA512", "SHA384", "SHA256", "SHA224", "MD5", "SHA", or "NONE". NOTE: To ensure data security, you are advised to use the SHA256 protocol or a protocol with a higher security level. |
| private_protocol=? | Data encryption protocol. | The value can be "AES256", "AES192", "AES", "DES", "3DES", or "NONE". NOTE: To ensure data security, you are advised to use the AES protocol or a protocol with a higher security level. |
| user_level=? | USM user level. | The value can be "read_only" or "read_write", and the default value is "read_write". NOTE: USM users of the "read_only" level can only read device information, USM users of the "read_write" level can read and write device information, and all USM users have the permission for Trap reporting. |

##### Usage Guidelines

-   SNMPv3 adopts the USM security mechanism, providing authentication-based access control.
-   This command provides an interactive mode for entering passwords (characters are displayed behind asterisks (\*)). A password must meet the following requirements:
-   A password contains 8 to 32 case-sensitive characters. You can run the "change snmp safe_strategy" command to change the requirement on the password length.
-   A password must comply with the password complexity requirements. You can run the "change snmp safe_strategy" command to change the password complexity level:
-   If the password complexity is set to "Normal", the password must contain special characters and at least two types of the following characters: uppercase letters, lowercase letters, and digits.
-   If the password complexity is set to "High", the password must contain special characters, uppercase letters, lowercase letters, and digits.
-   Do not use passwords composed of repeated substrings, such as "aaaaaaaa", "abababab", or "abcdabcd". There is no limit on the length of substrings.
-   The authentication protocol password and data encryption password must be different from the USM user name and mirror writing of the user name.
-   The authentication protocol password must be different from the data encryption password.

 

-   You can use the "change snmp safe_strategy" command to change the password policies of USM users.
-   The special characters include \` \~ ! @ \# $ % ^ & \* ( ) - \_ = + \\ \| \[ { } \] ; : ' " , \< . \> / ? and spaces.

##### Example

Add a USM user. Set the user name to "user", authentication protocol to "SHA224", data encryption protocol to "AES", and user level to "read_only".

```text

admin:/>change snmp usm user_name=user authenticate_protocol=SHA224 private_protocol=AES user_level=read_only
Please input your authenticate password:***************
Please input your authenticate password again:***************
Please input your private password:*********
Please input your private password again:*********
CAUTION: You are advised to set the security authentication protocol SHA256 or a higher security level and the data encryption protocol AES or a higher security level for the USM account.
Do you wish to continue?(y/n)y
Command executed successfully.

```

Add a USM user. Set the user name to "user", authentication protocol to "NONE", data encryption protocol to "NONE", and user level to "read_only".

```text

admin:/>add snmp usm user_name=user authenticate_protocol=NONE private_protocol=NONE user_level=read_only
CAUTION: You are about to create a USM user without authentication or encryption. This operation may affect system security.
Suggestion: Set the security authentication protocol and data encryption protocol for the USM user.
Do you wish to continue?(y/n)y
Command executed successfully.

```

Add a USM user. Set the user name to "user", authentication protocol to "SHA256", data encryption protocol to "NONE", and user level to "read_only".

```text

admin:/>add snmp usm user_name=user authenticate_protocol=SHA256 private_protocol=NONE user_level=read_only
Please input your authenticate password:***************
Please input your authenticate password again:***************
CAUTION: You are about to create a non-encrypted USM user. This operation may affect system security. Suggestion: Set the security authentication protocol and data encryption protocol for the USM user.
Do you wish to continue?(y/n)y
Command executed successfully.

```

##### System Response

None
