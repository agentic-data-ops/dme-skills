# delete vstore_pair general


##### Function

The **delete vstore_pair general** command is used to delete a vStore pair.

##### Format

**delete vstore_pair general** pair_id=? \[ is_local_delete=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pair_id=? | ID of a vStore pair. | You can run the "show vstore_pair general" command to obtain the value. |
| is_local_delete=? | Whether to locally delete a vStore pair. | The value can be "yes" or "no", where: <br>"yes": locally deleted.<br>"no": locally and remotely deleted.<br> The default value is "no". |

##### Usage Guidelines

None

##### Example

Locally delete vStore pair "1".

```text
admin:/>delete vstore_pair general pair_id=1 is_local_delete=yes
WARNING: You are about to delete a vStore pair. This operation cannot be undone. If you need the configuration later, you must create it again.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete vStore pair "1".

```text
admin:/>delete vstore_pair general pair_id=1
WARNING: You are about to delete a vStore pair. This operation cannot be undone. If you need the configuration later, you must create it again.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
