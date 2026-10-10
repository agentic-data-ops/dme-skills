# change snmp usm


##### Function

The **change snmp usm** command is used to modify the configuration of a USM user.

##### Format

**change snmp usm** user_name=? authenticate_protocol=? private_protocol=? \[ user_level=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| user_name=? | USM user name. | To obtain the value, run "show snmp usm". |
| authenticate_protocol=? | Authentication protocol. | The value can be "SHA512", "SHA384", "SHA256", "SHA224", "MD5", "SHA", or "NONE". NOTE: To ensure data security, you are advised to use the SHA256 protocol or a protocol with a higher security level. |
| private_protocol=? | Data encryption protocol. | The value can be "AES256", "AES192", "AES", "DES", "3DES", or "NONE". NOTE: To ensure data security, you are advised to use the AES protocol or a protocol with a higher security level. |
| user_level=? | USM user level. | The value can be "read_only" or "read_write". NOTE: USM users of the "read_only" level can only read device information, USM users of the "read_write" level can read and write device information, and all USM users have the permission for Trap reporting. |

##### Usage Guidelines

-   SNMPv3 uses the USM security mechanism and provides authentication access.
-   This command provides an interactive mode for entering the password (the password is not displayed on the screen). The password format must meet the following requirements:
-   The password can contain 8 to 32 case-sensitive characters. You can run the "change snmp safe_strategy" command to change the length range.
-   The password must meet the password complexity requirements. You can run the "change snmp safe_strategy" command to change the password complexity level.
-   If the password complexity requirement is common, the password must contain special characters and at least two of the following types: lowercase letters, uppercase letters, and digits.
-   When the password complexity requirement is high, the password must contain special characters and the following three types of characters: lowercase letters, uppercase letters, and digits.
-   A password cannot contain only repeated strings, such as aaaaaaaa, abababab, and abcdabcd.
-   The authentication protocol password and data encryption protocol password cannot be the same as the USM user name or the reversed USM user name.
-   The authentication protocol password must be different from the data encryption protocol password.

 

-   You can run the "change snmp safe_strategy" command to modify the USM user password policy.
-   The special characters include \` \~! @ \# $ % ^ & amp;; \* () - \_ = + \\ \| \[{}\]; :'", & lt;.. \> /? and space.

.

##### Example

Change the authentication protocol to "SHA224", data encryption protocol to "AES", and user level to "read_only" for USM user "user".

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

Change the authentication protocol to "NONE", data encryption protocol to "NONE", and user level to "read_write" for USM user "user".

```text

admin:/>change snmp usm user_name=user authenticate_protocol=NONE private_protocol=NONE user_level=read_write
CAUTION: You are about to change the USM user to non-authentication and non-encryption. This operation may affect system security.
Suggestion: Setthe security authentication protocol and data encryption protocol for the USM user.
Do you wish to continue?(y/n)y
Command executed successfully.

```

Change the authentication protocol to "SHA256", data encryption protocol to "NONE", and user level to "read_write" for USM user "user".

```text

admin:/>change snmp usm user_name=user authenticate_protocol=SHA256 private_protocol=NONE user_level=read_write
Please input your authenticate password:***************
Please input your authenticate password again:***************
CAUTION: You are about to change the encryption mode of the USM user to no encryption. This operation may affect system security.
Suggestion: Set the security authentication protocol and data encryption protocol for the USM user.
Do you wish to continue?(y/n)y
Command executed successfully.

```

##### System Response

None
