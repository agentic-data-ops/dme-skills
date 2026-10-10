# delete snmp usm


##### Function

The **delete snmp usm** command is used to delete a USM user.

##### Format

**delete snmp usm** user_name=?

##### Parameters

| Parameter   | Description                                    | Value                                     |
|-------------|------------------------------------------------|-------------------------------------------|
| user_name=? | User name of USM user that you want to delete. | To obtain the value, run "show snmp usm". |

##### Usage Guidelines

Before deleting a USM user, ensure that the user name is not used in the trap server (you can run the "show notification trap" command to check whether the user name is used). Otherwise, the deletion fails.

##### Example

Delete the USM user whose name is "user".

```text
admin:/>delete snmp usm user_name=user
Command executed successfully.
```

##### System Response

None
