# add host nvme_over_roce_initiator


##### Function

The **add host nvme_over_roce_initiator** command is used to add an NVMe over RoCE initiator to a host.

##### Format

**add host nvme_over_roce_initiator** nvme_over_roce_nqn=? { host_id=? \| host_name=? }

##### Parameters

| Parameter            | Description                                             | Value                                              |
|----------------------|---------------------------------------------------------|----------------------------------------------------|
| host_id=?            | ID of the host to which you want to add an initiator.   | To obtain the value, run "show host general".      |
| nvme_over_roce_nqn=? | NQN of the NVMe over RoCE initiator.                    | You can specify only one NVMe over RoCE initiator. |
| host_name=?          | Name of the host to which you want to add an initiator. | To obtain the value, run "show host general".      |

##### Usage Guidelines

-   The host to which you want to add initiators has been created.
-   Initiators have been created on the storage system.
-   An initiator that you want to add must be in the idle state, which means the initiator has not been associated with any hosts.

##### Example

Add the NVMe over RoCE initiator whose NVMe qualified name (NQN) is "nqn.01" to the host whose ID is "2".

```text
admin:/>add host nvme_over_roce_initiator nvme_over_roce_nqn=nqn.01 host_id=2
DANGER: You are about to add the initiator to the host.
Suggestion: Before performing this operation, check whether the initiator that you have selected belongs to the host. After you successfully add the initiator, confirm that the multipathing configuration of the initiator is correct.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Add the NVMe over RoCE initiator whose NQN is "nqn.01" to the host whose name is "host1".

```text
admin:/>add host nvme_over_roce_initiator nvme_over_roce_nqn=nqn.01 host_name=host1
DANGER: You are about to add initiator to host.
Suggestion: Before performing this operation, determine whether the initiator that you have selected belongs to the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
