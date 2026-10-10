# change service ndmp_user


##### Function

The **change service ndmp_user** command is used to change the NDMP user name and password.

##### Format

**change service ndmp_user** user_name=? password=? \[ new_password=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| user_name=? | NDMP user name. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The user name must comply with the resource user security policy rules. NOTE: To query the user security policies of the storage system, run the "show resource_user safe_strategy" command. |
| password=? | Old password. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The password must comply with the resource user security policy rules. NOTE: To query the user security policies of the storage system, run the "show resource_user safe_strategy" command. |
| new_password=? | New password. NOTE: This parameter is not supported in this version, and the execution result is invalid. | The password must comply with the resource user security policy rules. NOTE: To query the user security policies of the storage system, run the "show resource_user safe_strategy" command. |

##### Usage Guidelines

This command is not supported in this version, and the command output is invalid.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Change the NDMP user name and password.

```text
admin:/>change service ndmp_user user_name=ndmpadmin password=******** new_password=********
Command executed successfully.
```

##### System Response

None
