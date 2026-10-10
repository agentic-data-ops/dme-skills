# change kms key_backup


##### Function

The **change kms key_backup** command is used to modify the key file backup server configurations of the internal key management service.

##### Format

**change kms key_backup** enabled=? server_address=? path=? user=? password=? protocol=? port=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Switch of the key file backup server. | The value can be "yes" or "no", where: <br>"yes": the key file backup will be enabled.<br>"no": the key file backup will be disabled. |
| server_address=? | Server address. | The value can be a domain name or an IPv4 or IPv6 address. The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| path=? | Storage path of the key file on the server. | The value contains 1 to 255 ASCII characters. The file save path cannot contain special characters including ':?"<>|* or start with a period (.) or space. The first character after the delimiter (/ or \) cannot be a period (.). |
| user=? | Server user name. | ASCII string without single quotation marks(the length is from 1 to 63 characters). |
| password=? | Server user password. | The value contains 1 to 63 ASCII characters. |
| protocol=? | Transfer protocol type. | The value can be "FTP" or "SFTP". To ensure the security of data transfer, you are advised to use Secure File Transfer Protocol (SFTP). |
| port=? | Server port number. | The value is an integer ranging from 1 to 65535. |

##### Usage Guidelines

-   If the storage system serves as a server in the file transfer with external systems, it supports the SFTP service only. If the storage system serves as a client, it supports both the FTP and SFTP services.
-   When the storage system uses the internal key management service, in order to improve the system reliability, it is recommended to enable the key file backup server, the internal key management service will automatically back up the key file to the server.

##### Example

Modify the key file backup server configurations of the internal key management service. The new address of the SFTP server is 192.168.8.211, port number is 22, the name of the folder for storing key file is /home/InternalKey, and the username and password for logging in to the SFTP server are "admin" and "12345678" respectively.

```text
admin:/>change kms key_backup enabled=yes server_address=192.168.8.211 path=/home/InternalKey user=admin password=******** protocol=SFTP port=22
Command executed successfully.

```

##### System Response

None
