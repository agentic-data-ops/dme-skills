# add host initiator


##### Function

The **add host initiator** command is used to add an initiator to a host.

##### Format

**add host initiator** { host_id=? \| host_name=? } initiator_type=? { wwn=? \| iscsi_iqn_name=? } \[ alias=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_id=? | ID of the host to which you want to add an initiator. | To obtain the value, run "show host general". |
| host_name=? | Name of the host to which you want to add an initiator. | To obtain the value, run "show host general". |
| initiator_type=? | Type of an initiator. | The value can be "iSCSI" or "FC", where: <br>"iSCSI": indicates iSCSI initiators.<br>"FC": indicates Fibre Channel initiators. |
| iscsi_iqn_name=? | iSCSI qualified name (IQN) of an iSCSI initiator. | You can specify only one iSCSI initiator. To obtain the value, run "show initiator". |
| wwn=? | World Wide Name (WWN) of a Fibre Channel initiator. | You can specify only one Fibre Channel initiator. To obtain the value, run "show initiator". |
| alias=? | Alias of an initiator. | To obtain the value, run "show initiator". |

##### Usage Guidelines

-   The host to which you want to add initiators has been created.
-   Initiators have been created on the storage system.
-   An initiator that you want to add must be in the idle state, which means the initiator has not been engaged by any hosts.

##### Example

Add an iSCSI initiator whose IQN is "iqn.01" to host "2".

```text
admin:/>add host initiator host_id=2 initiator_type=iSCSI iscsi_iqn_name=iqn.01
DANGER: You are about to add the initiator to the host.
Suggestion: Before performing this operation, check whether the initiator that you have selected belongs to the host. After you successfully add the initiator, confirm that the multipathing configuration of the initiator is correct.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Add an iSCSI initiator whose IQN is "iqn.01" to host "host1".

```text
admin:/>add host initiator host_name=host1 initiator_type=iSCSI iscsi_iqn_name=iqn.01
DANGER: You are about to add initiator to host.
Suggestion: Before performing this operation, determine whether the initiator that you have selected belongs to the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Add a Fibre Channel initiator whose WWN is "455856585f654578" to host "6".

```text
admin:/>add host initiator host_id=6 initiator_type=FC wwn=455856585f654578
DANGER: You are about to add the initiator to the host.
Suggestion: Before performing this operation, check whether the initiator that you have selected belongs to the host. After you successfully add the initiator, confirm that the multipathing configuration of the initiator is correct.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
