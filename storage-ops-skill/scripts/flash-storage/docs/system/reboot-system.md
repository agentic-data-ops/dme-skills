# reboot system


##### Function

The **reboot system** command is used to restart the storage system. Running this command causes service interruption.

##### Format

**reboot system** \[ force=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| force=? | Forcible reset flag. | The value can be "no" or "yes", where: <br>"no": Forcible reset will not be performed.<br>"yes": Forcible reset will be performed. |

##### Usage Guidelines

-   Before running this command, stop all the ongoing services on the storage system.
-   This command provides an interactive mode for entering passwords. The password will be displayed behind asterisks.
-   If the number of consecutively entered incorrect passwords reaches 3 within 5 minutes, the current session will be disconnected.

##### Example

Restart the storage system.

```text
admin:/>reboot system
DANGER: You are about to restart the storage system. This may take several minutes. This operation will interrupt all services on the storage system.
Suggestion: Before performing this operation, stop all services on the system.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Password:******
Command executed successfully.
```

Reset the system forcibly.

```text
developer:/>reboot system force=yes
DANGER: You are going to forcibly reset the system. This operation interrupts controller services and may cause configuration data loss.
Suggestion: Do not perform this operation when the controller is working.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Password:******
Command executed successfully.
```

##### System Response

None
