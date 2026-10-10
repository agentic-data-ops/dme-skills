# test kms key_backup


##### Function

The **test kms key_backup** command is used to test the key file backup server configurations of the internal key management service.

##### Format

**test kms key_backup** server_address=? path=? user=? password=? protocol=? port=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| server_address=? | Server address. | The value can be a domain name or an IPv4 or IPv6 address. The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| path=? | The storage path of the key file on the server. | The value contains 1 to 255 characters. The file save path cannot contain special characters including ':?"<>|* or start with a period (.) or space. The first character after the delimiter (/ or \) cannot be a period (.). |
| user=? | Server user name. | ASCII string without single quotation marks(length is from 1 to 63). |
| password=? | Server user password. | The value contains 1 to 63 ASCII characters. |
| protocol=? | Transfer protocol type. | The value can be "FTP" or "SFTP". To ensure the security of data transfer, you are advised to use Secure File Transfer Protocol (SFTP). |
| port=? | Server port number. | The value is an integer ranging from 1 to 65535. |

##### Usage Guidelines

-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.

##### Example

Test the key file backup server configurations of the internal key management service. The address of the SFTP server is "192.168.8.211", folder for storing key files is "/home/InnerKey", and user name and password for logging in to the SFTP server are "admin" and "12345678" respectively.

```text
admin:/>test kms key_backup server_address=192.168.8.211 path=/home/InnerKey user=admin password=********  protocol=SFTP port=22
Command executed successfully.
```

##### System Response

None
