# import certificate


##### Function

The **import certificate** command is used to import a new private key, certificate, and CA certificate.

##### Format

**import certificate** ip=? user=? password=? type=? \[ cert_file=? \] \[ ca_cert_file=? \] \[ key_file=? \] \[ port=? \] \[ protocol=? \] \[ use=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of the FTP/SFTP server. | - |
| user=? | User allowed by the FTP/SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password of a user allowed by the FTP/SFTP server. | The value contains 1 to 64 characters. |
| type=? | Certificate type. | Possible values are: <br>"key_management_center": key management center.<br>"domain_authentication": domain authentication.<br>"hypermetro_arbitration": HyperMetro arbitration.<br>"https_protocol": HTTPS protocol.<br>"ftps_protocol": FTPS protocol.<br>"syslog_authentication": Syslog server authentication.<br>"ntp_authentication": NTP server authentication.<br>"call_home_authentication": Call Home server authentication.<br>"email_authentication": email server authentication.<br>"disk_authentication": disk authentication.<br>"devicemanager_authentication": DeviceManager authentication.<br>"sso_authentication": SSO authentication.<br>"OTP_email_authentication": OTP email server authentication.<br>"file_service_domain_authentication": file service domain authentication.<br>"certification_authority": CA server authentication. |
| cert_file=? | Path for storing the certificate file on the FTP/SFTP server. | The value is a character string that ends with file name extension ".crt" or ".pem" (case-insensitive). |
| ca_cert_file=? | Path for storing the CA certificate file on the FTP/SFTP server. | The value is a character string that ends with file name extension ".crt" or ".pem" (case-insensitive). |
| key_file=? | Path for storing the private key on the FTP/SFTP server. | The value is a character string that ends with file name extension ".key" or ".pem" (case-insensitive). |
| port=? | Port of the FTP/SFTP server. | The value is an integer from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |
| protocol=? | Protocol used for transmitting the new certificate and private key. | The value can be FTP or SFTP. The default value is SFTP. To ensure data transmission security, you are advised to use the SFTP protocol. |
| use=? | Use of a certificate. | The value contains 1 to 127 characters including letters, digits, underscores (_), hyphens (-), and periods (.). |

##### Usage Guidelines

-   This command can be used to import the signed certificate and CA certificate into a storage system from the FTP or SFTP server connected to the storage system for certificate replacement. This command can also be used to import the private key, certificate, and CA certificate into the storage system for certificate replacement.
-   This command allows importing certificates, CA certificates, and private key files for a specified scenario (Both certificate and CA certificate are mandatory for key management server, HyperMetro quorum server, and CA server authentication. A CA certificate is mandatory for domain authentication, Syslog server authentication, NTP server authentication, Call Home server authentication, disk authentication, Email authentication, OTP Email authentication, SSO authentication, and File service domain authentication. A certificate is mandatory when the HTTPS or FTPS protocol is used, as well as for DeviceManager authentication).
-   The certificate type supported by this command can be "key_management_center", "domain_authentication", "https_protocol", "ftps_protocol", "hypermetro_arbitration", "syslog_authentication", "ntp_authentication", "call_home_authentication", "email_authentication", "disk_authentication", "devicemanager_authentication", "sso_authentication", "OTP_email_authentication", "file_service_domain_authentication", or "certification_authority".

 

Prerequisites:

-   Storage systems can correctly access the FTP server or SFTP server over the network.
-   The FTP or SFTP service has been enabled on the server.
-   A directory has been created on the server for storing security certificates.

If a storage system serves as a server in the file transfer with external systems, the storage system supports SFTP only. If a storage system serves as a client, the storage system supports both FTP and SFTP.

##### Example

Import a certificate and a CA certificate into the storage array and activate them to replace the old certificates after the certificate request is signed.

```text
admin/>import certificate ip=10.133.194.20 user=admin password=****** type=hypermetro_arbitration cert_file=cert.crt ca_cert_file=ca_cert.crt protocol=SFTP port=22
WARNING: You are about to replace the SSL certificate. This operation will replace the previous certificate file and may cause the SSL connection to be reconnected.
Suggestion: Before you perform this operation, please acknowledge the aforementioned risks and ensure that the certificate file to be imported is correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Obtain the private key, certificate, and CA certificate of a scenario, import them into the storage array, and activate them to replace the old certificates.

```text
admin/>import certificate ip=10.133.194.20 user=admin password=****** type=hypermetro_arbitration key_file=key.pem cert_file=cert.pem ca_cert_file=ca_cert.pem protocol=SFTP
WARNING: You are about to replace the SSL certificate. This operation will replace the previous certificate file and may cause the SSL connection to be reconnected.
Suggestion: Before you perform this operation, please acknowledge the aforementioned risks and ensure that the certificate file to be imported is correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
