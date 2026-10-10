# show kms key_backup


##### Function

The **show kms key_backup** command is used to query the key file backup server configurations of the internal key management service.

##### Format

**show kms key_backup**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the key file backup server configurations of the internal key management service.

```text

admin:/>show kms key_backup
Enabled     : Yes
Server Address : 192.168.8.211
Path         : /path
User         : admin
Protocol     : FTP
Port         : 21

```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                               |
|----------------|---------------------------------------|
| Enabled        | Switch of the key file backup server. |
| Server Address | Server address.                       |
| Path           | Server storage path.                  |
| User           | Server user name.                     |
| Protocol       | Server protocol.                      |
| Port           | Server port.                          |
