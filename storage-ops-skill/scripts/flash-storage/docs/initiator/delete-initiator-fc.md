# delete initiator fc


##### Function

The **delete initiator fc** command is used to delete Fibre Channel initiators. You can disable hosts from accessing the storage resources of the storage system by running this command.

##### Format

**delete initiator fc** wwn=?

##### Parameters

| Parameter | Description                                         | Value                                      |
|-----------|-----------------------------------------------------|--------------------------------------------|
| wwn=?     | World Wide Name (WWN) of a Fibre Channel initiator. | To obtain the value, run "show initiator". |

##### Usage Guidelines

-   Running this command will interrupt the services associated with a host.
-   Before running this command, ensure that the selected initiator is exactly the one you want to delete and no service is running on the host for the initiator. Otherwise, the command execution will fail.
-   An initiator that you want to delete must have been created and disconnected.

##### Example

To delete the Fibre Channel initiator whose WWN is "656de54589654569", run the following command.

```text
admin:/>delete initiator fc wwn=656de54589654569
CAUTION: You are about to delete the initiator. This operation will cause the initiator unavailable.
Suggestion: Before performing this operation, ensure that the initiator needs to be deleted.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
