# delete quorum_server general


##### Function

The **delete quorum_server general** command is used to delete a third-place quorum server.

##### Format

**delete quorum_server general** server_id=?

##### Parameters

| Parameter   | Description              | Value                                                             |
|-------------|--------------------------|-------------------------------------------------------------------|
| server_id=? | ID of the quorum server. | Run the "show quorum_server general" command to obtain the value. |

##### Usage Guidelines

None

##### Example

To delete quorum server 1, run the following command:.

```text
admin:/>delete quorum_server general server_id=1
WARNING: You are going to delete the quorum server.
This operation may cause the HyperMetro domain that uses the quorum server to work improperly.
Suggestion: Before performing this operation, ensure that no service is using the quorum server to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
