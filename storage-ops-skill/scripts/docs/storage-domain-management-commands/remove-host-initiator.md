# remove host initiator


##### Function

The **remove host initiator** command is used to remove initiators from a host.

##### Format

**remove host initiator** initiator_type=? { wwn=? \| iscsi_iqn_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| initiator_type=? | Type of an initiator that you want to remove. | The value can be "iSCSI" or "FC", where: <br>"iSCSI": indicates Internet Small Computer System Interface (iSCSI) initiators.<br>"FC": indicates Fibre Channel initiators. |
| iscsi_iqn_name=? | The iSCSI qualified name (IQN) of an iSCSI initiator that you want to remove. | To obtain the value, run "show initiator". |
| wwn=? | World Wide Name (WWN) of a Fibre Channel initiator that you want to remove. | To obtain the value, run "show initiator". |

##### Usage Guidelines

-   Running this command prevents a host from accessing the storage resources of the storage system.
-   Before running this command, ensure that the selected initiator is exactly the one you want to remove.

##### Example

To remove the iSCSI initiator whose IQN is "iqn.01", run the following command.

```text
admin:/>remove host initiator initiator_type=iSCSI iscsi_iqn_name=iqn.01
DANGER: You are about to remove initiator from host. This operation will interrupt related ongoing services.
Suggestion: Before performing this operation, ensure that the selected host and initiators are correct and stop services on the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

To remove the Fibre Channel initiator whose WWN is "455856585f654578", run the following command.

```text
admin:/>remove host initiator initiator_type=FC wwn=455856585f654578
DANGER: You are about to remove initiator from host. This operation will interrupt related ongoing services.
Suggestion: Before performing this operation, ensure that the selected host and initiators are correct and stop services on the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
