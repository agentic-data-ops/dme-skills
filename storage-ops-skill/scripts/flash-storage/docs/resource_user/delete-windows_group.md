# delete windows_group


##### Function

The **delete windows_group** command is used to delete a Windows user group.

##### Format

**delete windows_group** { name=? \| rid=? }

##### Parameters

| Parameter | Description                     | Value                                                                                                                                                                                                  |
|-----------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?    | Name of the Windows user group. | The value consists of 1 to 256 characters, and cannot contain spaces, control character or any of the following special characters: /\\\]\[:;\|=,+\*?\<\>@. The last character cannot be a period (.). |
| rid=?     | RID of the Windows user group.  | The value ranges from 1000 to 4,294,967,295.                                                                                                                                                           |

##### Usage Guidelines

None

##### Example

Delete a Windows user group.

```text
admin:/>delete windows_group rid=100001
WARNING:You are going to delete windows group.This operation may cause access exceptions.
Suggestion:Before you perform this operation, determine whether the delete is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete a Windows user group.

```text
admin:/>delete resource_group name=group2
WARNING:You are going to delete resource group.This operation may cause access exceptions.
Suggestion:Before you perform this operation, determine whether the delete is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Query all Windows user groups.

```text
admin:/>show windows_group general
Windows Group RID Windows Group Name Group Type
----------------- ------------------- ----------
99999 Administrators BuiltIn
100000 default_group BuiltIn
```

##### System Response

None
