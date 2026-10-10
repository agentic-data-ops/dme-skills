# delete certificate general


##### Function

The **delete certificate general** command is used to delete CA certificate information from an array.

##### Format

**delete certificate general** type=? \[ use=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Certificate type. | The value can be: <br>"disk_authentication": disk authentication. |
| use=? | Use of a certificate. | The value contains 1 to 127 characters including letters, digits, underscores (_), hyphens (-), and periods (.). |

##### Usage Guidelines

None

##### Example

Delete the CA certificate in the disk authentication scenario.

```text
admin:/>delete certificate general type=disk_authentication use=test
WARNING: You are about to delete the certificate. This operation may cause an SSL connection setup failure.
Suggestion: Before performing this operation, ensure that the risk is acceptable.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
