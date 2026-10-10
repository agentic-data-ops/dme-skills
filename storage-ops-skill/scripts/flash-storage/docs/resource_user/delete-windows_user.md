# delete windows_user


##### Function

The **delete windows_user** command is used to delete a Windows user.

##### Format

**delete windows_user** { rid=? \| name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rid=? | RID of a Windows user. | The value ranges from 1000 to 4,294,967,295. |
| name=? | Name of a Windows user. | The value consists of the minimal length of a user name (view the minimum length by running the show resource_user safe_strategy command) to 20 characters, and cannot contain spaces, control character or any of the following special characters: "/\][:;|=,+*?<>@. The last character cannot be a period (.). Run the "show windows_user general" command to query the windows users in the current system. |

##### Usage Guidelines

None

##### Example

Delete a Windows user.

```text
admin:/>delete windows_user rid=1001
WARNING: You are going to delete windows user. This operation may cause access exceptions.
Suggestion: Before you perform this operation, determine whether the delete is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
