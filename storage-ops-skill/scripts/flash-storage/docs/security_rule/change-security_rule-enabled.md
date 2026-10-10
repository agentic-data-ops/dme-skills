# change security_rule enabled


##### Function

The **change security_rule enabled** command is used to enable or disable security rules.

##### Format

**change security_rule enabled** enabled=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Switch of security rules. | The value can be "yes" or "no", where: <br>"yes": Security rules will be enabled. Only maintenance terminals in the white list can access the storage system.<br>"no": Security rules will be disabled. If the parameter value is set to "no", all maintenance terminals can access the storage system. |

##### Usage Guidelines

 

If a maintenance terminal has logged in the storage system using the command line interface (CLI) or the DeviceManager but the IP address of the maintenance terminal has not been added into security rules, running this command may disconnect the CLI or the DeviceManager and forbids future login attempts.

-   Only the maintenance terminal in security rules can access the storage system.
-   To add the white list, run "add security_rule".

##### Example

Enable security rules.

```text
admin:/>change security_rule enabled enabled=yes
WARNING: You are about to enable the IP address security rule. This operation will make the storage system accessible to only the IP addresses in the IP address white list.
Suggestion: Confirm that you need to enable the IP address security rule and the IP addresses in the white list are correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Disable security rules.

```text
admin:/>change security_rule enabled enabled=no
WARNING: You are about to disable the IP address security rule. After this operation, all users' login to the storage system will not be verified against the white list, and all IP addresses can access the storage system.
Suggestion: Confirm that you need to disable the IP address security rule.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
