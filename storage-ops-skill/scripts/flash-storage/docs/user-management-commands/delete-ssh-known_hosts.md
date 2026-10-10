# delete ssh known_hosts


##### Function

The **delete ssh known_hosts** command is used to delete the server "known_hosts" file or a certain record in the file that is saved by the SSH client.

##### Format

**delete ssh known_hosts** type=? \[ record_address=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Deletes the "known_hosts" records that are saved by the SSH client. | "file": deletes the server public key file known_hosts saved on the SSH client. 2:"record": deletes a record from the known_hosts file saved on the SSH client. |
| record_address=? | IP address in the known_hosts file. This parameter is available only when "Type" is "record". | IPV4 or IPV6 address. |

##### Usage Guidelines

-   This command is used to delete the server "known_hosts" file or a certain record in the file that is saved by the SSH client.
-   When deleting the file, you do not need to enter the server IP address.
-   When deleting records in the file, you need to enter the server IP address.

##### Example

Delete the server "known_hosts" file or a certain record in the file that is saved by the SSH client.

```text

admin:/>delete ssh known_hosts type=file
WARNING: You are about to delete the "known_hosts" records saved by the SSH client.
This operation will lead to a result that the server public key is no longer saved in the "known_hosts" file of the client. Therefore, the client cannot detect whether the server is forged.
Suggestion: Before performing this operation, make sure that you have selected a correct record and the record is no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
