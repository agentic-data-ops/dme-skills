# change iscsi target_name


##### Function

The **change iscsi target_name** command is used to change the name of the iSCSI target configured for the storage system.

##### Format

**change iscsi target_name** iscsi_name=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| iscsi_name=? | Last field of the new iSCSI target name. NOTE: The first six segments of the target name are fixed and cannot be modified. Only the last field of the target name can be modified. | The value contains 1 to 31 ASCII characters, including digits, letters, hyphens (-), colons (:), and periods (.). |

##### Usage Guidelines

-   Running this command interrupts all services associated with the specified target.
-   Before running this command, ensure that all connections to the specified target are disconnected.
-   Initiators and targets are relative. In the scenario where storage systems A and B connect to each other in iSCSI mode, from the perspective of storage system A, storage system A is the initiator and storage system B is the target. Likewise, from the perspective of storage system B, storage system B is the initiator and storage system A is the target.

##### Example

Change the last field of the name of an iSCSI target on the storage system to "iqn.2006-08:tgt".

```text

admin:/>change iscsi target_name iscsi_name=iqn.2006-08:tgt
DANGER: You are about to change the target name. This operation will interrupt all replication, heterogeneous, and host services associated with the target.
Suggestion: Before performing this operation, ensure that all replication, heterogeneous, and host services associated with the target are stopped.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
