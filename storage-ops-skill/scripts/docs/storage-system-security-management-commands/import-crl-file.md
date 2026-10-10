# import crl file


##### Function

The **import crl file** command is used to import a new certificate revocation list.

##### Format

**import crl file** ip=? user=? password=? type=? crl_file=? \[ protocol=? \] \[ port=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of the FTP/SFTP server. | - |
| user=? | User allowed by the FTP/SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password of a user allowed by the FTP/SFTP server, displayed as asterisks (*). | The value contains 1 to 64 characters. |
| type=? | Certificate revocation list type. | Possible values are: <br>"key_management_center": key management center.<br>"domain_authentication": domain authentication.<br>"hypermetro_arbitration": HyperMetro arbitration.<br>"call_home_authentication": Call Home authentication.<br>"sso_authentication": SSO authentication.<br>"email_authentication": email authentication.<br>"integrity_protection": integrity protection.<br>"secure_boot": secure boot.<br>"OTP_email_authentication": OTP email authentication.<br>"file_service_domain_authentication": file service domain authentication. |
| crl_file=? | Path for storing the certificate revocation list file on the FTP/SFTP server. | The value is a character string that ends with file name extension ".crl" (case-insensitive). |
| protocol=? | Protocol used for transmitting the new certificate revocation list. | The value can be FTP or SFTP. The default value is SFTP. To ensure data transmission security, you are advised to use the SFTP protocol. |
| port=? | Port of the FTP/SFTP server. | The value is an integer from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |

##### Usage Guidelines

-   This command can be used to import a new certificate revocation list into the storage array from the FTP or SFTP server connected to the storage system.
-   This command supports that a new certificate revocation list can be imported based on application scenarios.
-   The certificate revocation list type supported by this command can be "key_management_center", "domain_authentication", "hypermetro_arbitration", "call_home_authentication", "sso_authentication", "email_authentication", "integrity_protection", "secure_boot", "OTP_email_authentication", or "file_service_domain_authentication".

 

Prerequisites:

-   Storage systems can correctly access the FTP server or SFTP server over the network.
-   The FTP or SFTP service has been enabled on the server.
-   A directory has been created for storing the certificate revocation list.

##### Example

Import a certificate revocation list into the storage array and activate it.

```text
admin/>import crl file ip=10.133.194.20 user=admin password=****** type=domain_authentication crl_file=test.crl protocol=SFTP port=22
WARNING: You are about to import the certificate revocation list. This operation will revoke the certificate file and may cause the SSL connection failure.
Suggestion: Before performing this operation, ensure that you accept the aforementioned risks and the certificate revocation list to be imported is correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
