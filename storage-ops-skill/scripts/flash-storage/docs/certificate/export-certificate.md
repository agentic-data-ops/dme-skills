# export certificate


##### Function

The **export certificate** command is used to generate private keys and certificate request files based on application scenarios and export the certificate request files for subsequent signature and certificate import.

##### Format

**export certificate** ip=? user=? password=? type=? certificate_path=? \[ port=? \] \[ protocol=? \] \[ algorithm=? \] \[ country=? \] \[ state_province=? \] \[ locality=? \] \[ organization=? \] \[ organization_unit=? \] \[ common_name=? \] \[ subject_alt_name=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of the FTP/SFTP server. | - |
| user=? | User allowed by the FTP/SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password of a user allowed by the FTP/SFTP server. | The value contains 1 to 64 characters. |
| type=? | Certificate type. | The options are as follows: <br>"key_management_center": key management center.<br>"domain_authentication": domain authentication.<br>"hypermetro_arbitration": HyperMetro arbitration.<br>"email_authentication": email server authentication.<br>"devicemanager_authentication": DeviceManager authentication.<br>"OTP_email_authentication": one-off password authentication on the email server.<br>"file_service_domain_authentication": file service domain authentication.<br>"certification_authority": certificate issued by a CA server.<br>"https_protocol": HTTPS protocol.<br>"ftps_protocol": FTPS protocol. |
| certificate_path=? | Path for storing the certificate file on the FTP/SFTP server. | The value is a character string that ends with file name extension ".csr" (case-insensitive). |
| port=? | Port of the FTP/SFTP server. | The value is an integer from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |
| protocol=? | Protocol used for transmitting the new certificate and private key. | The value can be FTP or SFTP. The default value is SFTP. To ensure data transmission security, you are advised to use the SFTP protocol. |
| algorithm | Encryption algorithm. | The value can be: <br>RSA_2048: RSA encryption algorithm. The key contains 2048 bits.<br>RSA_4096: RSA encryption algorithm. The key contains 4096 bits.<br>ECC_256: ECC encryption algorithm. The key contains 256 bits.<br> The default value is "RSA_2048". |
| country | Value of "country" in the "subject" field when a certificate request file is generated. | The value is a string of two characters. Each character must be a letter (case-sensitive). |
| state_province | Value of "state or province name" in the "subject" field when a certificate request file is generated. | The value is a non-null character string of up to 128 characters, including case-insensitive letters, digits, commas (,), periods (.), spaces, underscores (_), hyphens (-), and asterisks (*). |
| locality | Value of "locality" in the "subject" field when a certificate request file is generated. | The value is a non-null character string of up to 128 characters, including case-insensitive letters, digits, commas (,), periods (.), spaces, underscores (_), hyphens (-), and asterisks (*). |
| organization | Value of "organization" in the "subject" field when a certificate request file is generated. | The value is a non-null character string of up to 64 characters, including case-insensitive letters, digits, commas (,), periods (.), spaces, underscores (_), hyphens (-), and asterisks (*). |
| organization_unit | Value of the "organization unit" parameter in the subject field when the certificate request file is generated. | The value is a non-empty string of a maximum of 64 characters. Each character must meet the following requirements: The value is a string of 26 letters (case-insensitive), digits (0 to 9), or one of the following characters: comma (,), period (.) ".", space (" "), underscore (_), hyphen ("-"), and asterisk ("*"). |
| common_name | Value of "common name" in the "subject" field when a certificate request file is generated. | The value is a non-null character string of up to 64 characters, including case-insensitive letters, digits, commas (,), periods (.), spaces, underscores (_), hyphens (-), asterisks (*), and at signs (@). |
| subject_alt_name | SAN field that can be extended when the CSR file is exported from X509. | The value is a non-null character string of up to 512 characters. The format is KEY:VALUE. Use commas (,) to separate multiple sets of KEY:VALUE. The value of a KEY can be "DNS", "IP", "URI", "RID", "email", "otherName", or "dirName". For details about the input format of this parameter, see the security configuration guide. |

##### Usage Guidelines

-   This command can be used to generate certificate private keys and certificate request files for device management arrays, domain authentication arrays, email authentication arrays, and OTP email authentication arrays.
-   This command can only be used to **export certificate** request files from a storage system to the FTP or SFTP server connected to the storage system.
-   The certificate type supported by this command can be "key_management_center", "domain_authentication", "hypermetro_arbitration", "https_protocol", "ftps_protocol", "devicemanager_authentication", "email_authentication", "OTP_email_authentication", "file_service_domain_authentication", or "certification_authority".

 

Prerequisites:

-   Storage systems can correctly access the FTP server or SFTP server over the network.
-   The FTP or SFTP service has been enabled on the server.
-   A directory has been created for storing security certificates.

If a storage system serves as a server in the file transfer with external systems, the storage system supports SFTP only. If a storage system serves as a client, the storage system supports both FTP and SFTP.

##### Example

Generate and export certificate request files based on application scenarios.

```text
admin:/>export certificate ip=10.133.194.20 user=admin password=****** type=domain_authentication certificate_path=/temp.csr protocol=SFTP port=22 algorithm=RSA_2048 country=CN state_province=Beijing locality=Shenzhen organization=Huawei organization_unit=Huawei\sStorage common_name=Dorado\sV6 subject_alt_name=DNS:*.huawei.com,IP:10.10.10.10,IP:10::30,URI:http://my.url.here/,RID:1.2.3.4,email:myAddress@huawei.com,otherName:5.6.7.8,dirName:dir_name\\n[dir_name]\\nO=CN\\nCN=huawei
Command executed successfully.
```

##### System Response

None
