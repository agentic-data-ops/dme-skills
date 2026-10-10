# delete initiator iscsi


##### Function

The **delete initiator iscsi** command is used to delete Internet Small Computer Systems Interface (iSCSI) initiators. You can disable hosts from accessing the storage resources of the storage system by running this command.

##### Format

**delete initiator iscsi** iscsi_iqn_name=?

##### Parameters

| Parameter        | Description                                           | Value                                      |
|------------------|-------------------------------------------------------|--------------------------------------------|
| iscsi_iqn_name=? | The iSCSI qualified name (IQN) of an iSCSI initiator. | To obtain the value, run "show initiator". |

##### Usage Guidelines

-   Before you perform this operation, ensure that you select the correct initiator and services running on the host to which the initiator is added are stopped. Otherwise, running **delete initiator iscsi** fails.
-   Disconnect the initiator from the host before you delete the initiator.

##### Example

To delete the iSCSI initiator whose IQN is "iqn.01", run the following command.

```text
admin:/>delete initiator iscsi iscsi_iqn_name=iqn.01
CAUTION: You are about to delete the initiator. This operation will cause the initiator unavailable.
Suggestion: Before performing this operation, ensure that the initiator needs to be deleted.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
