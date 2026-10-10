# change iscsi initiator_name


##### Function

The **change iscsi initiator_name** command is used to change the name of an iSCSI initiator configured for the storage system.

##### Format

**change iscsi initiator_name** controller=? iscsi_name=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller=? | ID of a controller. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0, for example, "0A" or "1C". |
| iscsi_name=? | Last field of the new name of an iSCSI initiator. NOTE: The first six fields of an initiator name cannot be changed. Only the last field can be modified. | The value contains 1 to 31 characters including digits, letters, hyphens (-), colons (:), and periods (.). |

##### Usage Guidelines

-   Running this command interrupts all services associated with the specified initiator.
-   Before running this command, ensure that all services associated with the specified initiator are stopped.
-   Initiators and targets are relative. In the scenario where storage systems A and B connect to each other in iSCSI mode, from the perspective of storage system A, storage system A is the initiator and storage system B is the target. Likewise, from the perspective of storage system B, storage system B is the initiator and storage system A is the target.
-   The first six fields of an initiator name cannot be changed.

##### Example

Change the last field of the name of an initiator on storage system controller 0A to "configa".

```text

admin:/>change iscsi initiator_name controller=0A iscsi_name=config
DANGER: You are about to change the initiator name. This operation will interrupt all replication and heterogeneous services associated with the initiator.
Suggestion: Before performing this operation, ensure that all replication and heterogeneous services associated with the initiator are stopped.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
