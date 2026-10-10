# delete kmc general


##### Function

The **delete kmc general** command is used to delete the configuration of an external key management server.

##### Format

**delete kmc general** id=?

##### Parameters

| Parameter | Description                                                                    | Value                        |
|-----------|--------------------------------------------------------------------------------|------------------------------|
| id=?      | ID of the external key management server configuration, which will be deleted. | The value can be "1" or "2". |

##### Usage Guidelines

This command is used to delete the configuration of an external key management server. User can view the existing configurations by "show kmc general" command and decide which configuration to be deleted according to its ID.

##### Example

Delete the configuration of an external key management server.

```text
admin:/>delete kmc general id=1
DANGER: You are about to delete the configuration of the external key management server which provides keys for the self-encrypting disk. Deleting the external key management server by mistake may lead to business interruption.
Suggestion: Before you perform this operation, make sure that the self-encrypting disk no longer uses the key provided by the external key management server.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
