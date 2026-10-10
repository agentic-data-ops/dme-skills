# delete share cifs


##### Function

The **delete share cifs** command is used to delete a CIFS share.

##### Format

**delete share cifs** { share_id=? \| share_name=? }

##### Parameters

| Parameter    | Description      | Value                                                                          |
|--------------|------------------|--------------------------------------------------------------------------------|
| share_id=?   | Share ID.        | The value is an integer ranging from 0 to 18,446,744,073,709,551,615.          |
| share_name=? | CIFS share name. | The value consists of 1 to 80 characters excluding \\"/\\\\\[\]:\|\<\>+;,?\*=. |

##### Usage Guidelines

-   Parameters "share_id" or "share_name" must be entered.
-   In HyperMetro scenarios, if a failure message is prompted when deleting a CIFS share, inconsistency between primary and secondary share permission lists may occur. You need to delete the CIFS share again until the operation succeeds to prevent inconsistency between primary and secondary share permission lists.

##### Example

Delete a CIFS share.

```text
admin:/>delete share cifs share_id=3
WARNING: You are going to delete protocol share. This operation may interrupt share services or cause access exceptions.
Suggestion: Before you perform this operation, determine whether the delete is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete a CIFS share with a specified name.

```text
admin:/>delete share cifs share_name=cifs0
WARNING: You are going to delete protocol share. This operation may interrupt share services or cause access exceptions.
Suggestion: Before you perform this operation, determine whether the delete is necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
