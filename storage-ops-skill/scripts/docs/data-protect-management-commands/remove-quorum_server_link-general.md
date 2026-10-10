# remove quorum_server_link general


##### Function

The **remove quorum_server_link general** command is used to remove a specified link between a storage array and a quorum server.

##### Format

**remove quorum_server_link general** link_id=?

##### Parameters

| Parameter | Description | Value                                                       |
|-----------|-------------|-------------------------------------------------------------|
| link_id=? | Link ID.    | To obtain the value, run "show quorum_server_link general". |

##### Usage Guidelines

None

##### Example

Remove the link whose ID is "1" between the quorum server and array.

```text
admin:/>remove quorum_server_link general link_id=1
WARNING: You are about to remove a quorum server link.
After this operation is performed, reliability of quorum server links may be adversely affected.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
