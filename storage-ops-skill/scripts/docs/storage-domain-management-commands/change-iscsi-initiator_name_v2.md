# change iscsi initiator_name_v2


##### Function

The **change iscsi initiator_name_v2** command is used to change the name of an iSCSI initiator configured for the storage system.

##### Format

**change iscsi initiator_name_v2** iscsi_name=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| iscsi_name=? | An updated last field of an iSCSI initiator name. NOTE: The first six fields of an initiator name cannot be changed. Only the last field can be modified. | The value contains 1 to 31 characters including digits, letters, hyphens (-), colons (:), and periods (.). |

##### Usage Guidelines

-   Running this command interrupts all services associated with the specified initiator.
-   Before running this command, ensure that all services associated with the specified initiator are stopped.
-   Initiators and targets are relative. In the scenario where storage systems A and B connect to each other in iSCSI mode, from the perspective of storage system A, storage system A is the initiator and storage system B is the target. Likewise, from the perspective of storage system B, storage system B is the initiator and storage system A is the target.
-   The first six fields of an initiator name cannot be changed.

##### Example

To change the name's last field of the initiator configured for controller to config, run the following command.

```text

admin:/>change iscsi initiator_name_v2 iscsi_name=config
DANGER: You are about to change the initiator name. This operation will interrupt all replication and heterogeneous services associated with the initiator.
Suggestion: Before performing this operation, ensure that all replication and heterogeneous services associated with the initiator are stopped.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
