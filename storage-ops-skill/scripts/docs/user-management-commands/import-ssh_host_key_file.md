# import ssh_host_key_file


##### Function

The **import ssh_host_key_file** command is used to replace the public key file and private key file on the SSH server.

##### Format

**import ssh_host_key_file** key_type=? ip=? user=? password=? public_key_file=? private_key_file=? \[ protocol=? \] \[ port=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| key_type=? | Type of the encryption algorithm for the imported public key file and private key file. | Possible value of the "key_type" parameter is "ecdsa", "dsa", "rsa", or "ed25519", where: <br>"rsa":Rivest-Shamir-Adleman algorithm(RSA).<br>"dsa":Digital Signature Algorithm(DSA).<br>"ecdsa": Elliptic Curve Digital Signature Algorithm (ECDSA).<br>"ed25519": Edwards-Curve Digital Signature Algorithm (ED25519). |
| ip=? | IP address of the FTP/SFTP server. | - |
| user=? | User allowed by the FTP/SFTP server. | The value contains 1 to 64 characters without colons (:). |
| password=? | Password of a user allowed by the FTP/SFTP server. | The value contains 1 to 64 characters. |
| public_key_file=? | Path for storing the public key on the FTP/SFTP server. | - |
| private_key_file=? | Path for storing the private key on the FTP/SFTP server. | - |
| protocol=? | Protocol used for transmitting the new public and private key. | The value can be "FTP" or "SFTP". The default value is "SFTP". To ensure the security of data transfer, you are advised to use Secure File Transfer Protocol (SFTP). |
| port=? | Port of the FTP/SFTP server. | The value is an integer ranging from 1 to 65535. <br>If protocol=FTP, the default value is "21".<br>If protocol=SFTP, the default value is "22". |

##### Usage Guidelines

If you want to use your own SSH public key file and private key file, perform the following steps:

-   Use the ssh-keygen tool to generate a public key file and private key file encrypted with RSA, DSA, ECDSA, or ED25519 algorithm. The RSA, DSA, and ECDSA algorithms support only the PEM and PKCS8 formats, and the ED25519 algorithm supports only the RFC4716 format.
-   Run the **import ssh_host_key_file** command to import the public key file and private key file.

 

If a public key file or private key file is encrypted with a non-RSA, non-DSA, non-ECDSA, and non-ED25519 algorithm, or an illegal public key file and an illegal private key file are imported, the RSA, DSA, ECDSA, or ED25519 algorithm will not be used for connection encryption when an SSH connection is set up the next time.

##### Example

Replace the ECDSA public key file and private key file on the SSH server with the ECDSA public key file and private key file provided by the user.

```text
admin/>import ssh_host_key_file key_type=ecdsa ip=192.168.8.211 user=admin password=****** public_key_file=ssh_host_ecdsa_key.pub private_key_file=ssh_host_ecdsa_key protocol=FTP port=21
WARNING:You are about to replace the existing SSH public key file and private key file with a self-released SSH public key file and private key file. This operation may cause the Linux-based SSH client unable to connect to the storage array.
Suggestion:Before you perform this operation, implement the following steps:
1. Ensure that the existing SSH public key file and private key file need to be replaced.
2. If the SSH client cannot connect to the storage array, manually clear historical records in file /root/.ssh/known_hosts and reconnect to the storage array.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)Y
Command executed successfully.
```

##### System Response

None
