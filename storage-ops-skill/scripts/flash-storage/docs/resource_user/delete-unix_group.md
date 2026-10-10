# delete unix_group


##### Function

The **delete unix_group** command is used to delete a UNIX group.

##### Format

**delete unix_group** name=?

##### Parameters

| Parameter | Description             | Value                                                                                                                                                                     |
|-----------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?    | Name of the UNIX group. | The value contains 1 to 64 characters, including case-sensitive letters, digits, hyphens (-), periods (.), and underscores (\_). The name cannot start with a hyphen (-). |

##### Usage Guidelines

None

##### Example

Delete a UNIX group with the specified name.

```text
admin:/>delete unix_group name=group1
WARNING:You are going to delete UNIX group.This operation may cause access exceptions.
Suggestion:Before you perform this operation, determine whether the delete is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
