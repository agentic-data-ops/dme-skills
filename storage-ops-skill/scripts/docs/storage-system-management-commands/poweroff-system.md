# poweroff system


##### Function

The **poweroff system** command is used to power off the storage system. Running this command causes service interruption.

##### Format

**poweroff system**

##### Parameters

None

##### Usage Guidelines

-   Running this command forcibly stops the ongoing services on the storage system, leading to service interruption.
-   Before running this command, stop all the ongoing services on the storage system.
-   This command provides an interactive mode for entering passwords. The password will be displayed behind asterisks.
-   If the number of consecutively entered incorrect passwords reaches 3 within 5 minutes, the current session will be offline.

##### Example

Power off the storage system.

```text
admin:/>poweroff system
DANGER: You are about to power off the storage system. This operation will interrupt all services on the storage system.
Suggestion: Before performing this operation, stop all services on the system.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Password:******
Command executed successfully.
```

##### System Response

None
