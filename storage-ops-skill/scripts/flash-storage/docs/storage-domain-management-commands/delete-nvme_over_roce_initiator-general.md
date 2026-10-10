# delete nvme_over_roce_initiator general


##### Function

The **delete nvme_over_roce_initiator general** command is used to delete an NVMe over RoCE initiator. After the deletion, the host can no longer access the storage system resources through the initiator.

##### Format

**delete nvme_over_roce_initiator general** nvme_over_roce_nqn=?

##### Parameters

| Parameter            | Description                         | Value                                                             |
|----------------------|-------------------------------------|-------------------------------------------------------------------|
| nvme_over_roce_nqn=? | NQN of an NVMe over RoCE initiator. | To obtain the value, run "show nvme_over_roce_initiator general". |

##### Usage Guidelines

-   Running this command will interrupt the services associated with a host.
-   Before running this command, ensure that the selected initiator is exactly the one you want to delete and no service is running on the host for the initiator. Otherwise, the command execution will fail.
-   An initiator that you want to delete must have been created and disconnected.

##### Example

Delete the NVMe over RoCE initiator whose NVMe qualified name (NQN) is "656de54589654569".

```text
admin:/>delete nvme_over_roce_initiator general nvme_over_roce_nqn=656de54589654569
CAUTION: You are about to delete initiator. After this operation, the initiator will be unavailable.
Suggestion: Ensure that you want to perform this operation.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
