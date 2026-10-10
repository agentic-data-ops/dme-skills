# import weak_password_dictionary


##### Function

The **import weak_password_dictionary** command is used to import and overwrite a complete weak password dictionary.

##### Format

**import weak_password_dictionary** ip=? user=? password=? file_path=? \[ protocol=? \] \[ port=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ip=? | IP address of the FTP or SFTP server. | Enter the correct IP address of the FTP or SFTP server. |
| user=? | User allowed by the FTP or SFTP server. | Enter a correct user name that is allowed by the FTP or SFTP server. The value is a string of 1 to 64 characters. |
| password=? | Password of the user allowed by the FTP or SFTP server. | The value is a string of 1 to 64 characters. |
| file_path=? | Path for storing weak password dictionary files on the FTP or SFTP server. | Enter the correct path for storing the weak password dictionary file on the FTP/SFTP server. |
| protocol=? | File transfer protocol used to transfer weak password dictionary files. | The value can be FTP or SFTP. The default value is SFTP. To ensure data transmission security, you are advised to use the SFTP protocol. |
| port=? | Port number of the FTP/SFTP server. | The value is an integer ranging from 1 to 65535. <br>If "protocol" is set to "FTP", the default value is "21".<br>If "protocol" is set to "SFTP", the default value is "22". |

##### Usage Guidelines

-   After the command is executed successfully, the system imports a weak password dictionary file from the specified SFTP or FTP server and overwrites the original weak password dictionary with the weak password in the file.
-   After running this command, the original weak password dictionary is cleared and the weak passwords in the imported weak password dictionary are saved.
-   The imported weak password dictionary file is in TXT format. Each weak password occupies a line and ends with a carriage return. The length of a weak password must contain 1 to 32 characters. Otherwise, the weak password cannot be imported.
-   Blank lines are allowed. Blank lines are not considered as weak passwords with a length of 0.
-   A weak password dictionary contains a maximum of 1000 weak passwords. If the number of non-blank lines in the imported weak password dictionary file exceeds 1000, the file is not imported.

##### Example

Import a weak password dictionary file that meets the specifications from the SFTP server. The IP address of the SFTP server where the weak password dictionary file is stored is "10.10.10.1", the user name is "admin", and the password is "123456". The imported weak password dictionary file is named "WeakPwdDict.txt" and stored in the root directory of the SFTP server.

```text
admin:/>import weak_password_dictionary ip=10.10.10.1 user=admin password=****** file_path=/WeakPwdDict.txt port=22 protocol=SFTP
WARNING: You are about to import a weak password dictionary. This operation will overwrite the original weak password dictionary in the storage system with the imported weak password dictionary. If the weak password dictionary function is enabled, the newly imported weak password dictionary takes effect immediately.
Suggestion:
1. Ensure that the weak passwords in the weak password dictionary file to be imported meet the security requirements of the application scenario.
2. Ensure that the number of weak passwords in the weak password dictionary to be imported does not exceed 1,000.
3. Ensure that each weak password contains 1 to 32 characters.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
