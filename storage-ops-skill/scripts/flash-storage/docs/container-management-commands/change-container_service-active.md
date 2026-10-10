# change container_service active


##### Function

The **change container_service active** command is used to activate the container service for the first time.

##### Format

**change container_service active** enabled=? password=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Whether to activate the container service. | The value is "on", indicating to activate the container service. |
| password=? | Password of a user. | The password contains 8 to 16 case-sensitive characters by default.<br>The password must contain special characters including` ~ ! @ # $ % ^ & * ( ) - _ = + | [ { } ] ; :' " , < . > / ? and space.<br>The password must meet the following complexity requirements: <br>When the password complexity requirement is common, the password must contain at least two of the following types: lowercase letters, uppercase letters, and digits.<br>When the password complexity requirement is high, the password must contain three types of characters: lowercase letters, uppercase letters, and digits.<br> <br>The password cannot be the same as the user name or the user name spelled backwards.<br>The password cannot contain three consecutive same characters.<br> NOTE: You can run the "change safe_strategy" command to modify the password policy and login policy of the storage system. |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Activate the container service.

```text
admin:/>change container_service active enabled=on password=******
WARNING: You are about to activate the container service. This operation will cause all controllers to be upgraded and restarted in batches, and the read/write performance may deteriorate.
Suggestion: Before performing this operation, ensure that the preceding risks are acceptable.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Activate Container Service (--) in background.
Run the "show task general task_id=1" command to query the execution result.
```

##### System Response

None
