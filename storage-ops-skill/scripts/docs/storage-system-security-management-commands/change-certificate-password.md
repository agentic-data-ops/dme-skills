# change certificate password


##### Function

The **change certificate password** command is used to change the password for encrypting the private key of a certificate.

##### Format

**change certificate password** type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Certificate type. | Possible values are: <br>"key_management_center": key management center.<br>"domain_authentication": domain authentication.<br>"hypermetro_arbitration": HyperMetro arbitration.<br>"email_authentication": Email server authentication.<br>"devicemanager_authentication": DeviceManager authentication.<br>"OTP_email_authentication": OTP email server authentication.<br>"file_service_domain_authentication": file service domain authentication.<br>"certification_authority": CA server authentication.<br>"https_protocol": HTTPS protocol.<br>"ftps_protocol": FTPS protocol. |

##### Usage Guidelines

-   This command can be used to change the password for encrypting the private key of the certificate in a specific scenario.
-   This command provides an interactive mode for entering passwords. When you are entering a password, characters are displayed as asterisks (\*).
-   By default, the password contains 8 to 16 case-sensitive characters.
-   The password must contain spaces and special characters, including \` \~ ! @ \# $ % ^ & \* ( ) - \_ = + \| \[ { } \] ; : ' " , \< . \> / ?.
-   The password must meet the following complexity requirements:
-   When the password complexity is normal, the password must contain at least two of the following types: lowercase characters, uppercase characters, and digits.
-   When the password complexity is high, the password must contain lowercase characters, uppercase characters, and digits.
-   The password cannot contain three consecutive duplicate characters.

 

The "change safe_strategy" command can be used to change the password policy and login policy of the storage system.

##### Example

Change the password for encrypting the private key of a certificate.

```text
admin/>change certificate password type=domain_authentication
New password:*************
Reenter password:*************
Command executed successfully.
```

##### System Response

None
