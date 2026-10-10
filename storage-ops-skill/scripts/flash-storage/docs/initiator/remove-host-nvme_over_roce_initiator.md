# remove host nvme_over_roce_initiator


##### Function

The **remove host nvme_over_roce_initiator** command is used to remove an NVMe over RoCE initiator from a host.

##### Format

**remove host nvme_over_roce_initiator** nvme_over_roce_nqn=? { host_id=? \| host_name=? }

##### Parameters

| Parameter            | Description                                                                   | Value                                                             |
|----------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------|
| host_id=?            | Host ID.                                                                      | To obtain the value, run "show host general".                     |
| host_name=?          | Host name.                                                                    | To obtain the value, run "show host general".                     |
| nvme_over_roce_nqn=? | NVMe Qualified Name (NQN) of the NVMe over RoCE initiator you want to remove. | To obtain the value, run "show nvme_over_roce_initiator general". |

##### Usage Guidelines

-   Running this command prevents a host from accessing the storage resources of the storage system through the removed initiator.
-   Before running this command, ensure that the selected initiator is exactly the one you want to remove.

##### Example

Remove an NVMe over RoCE initiator from the host whose ID is "0".

```text
admin:/>remove host nvme_over_roce_initiator nvme_over_roce_nqn=0000000000005678 host_id=0
DANGER: You are about to remove initiator from host. This operation will interrupt related ongoing services.
Before performing this operation, ensure that the selected host and initiators are correct and stop services on the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
