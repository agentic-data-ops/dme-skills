# show port nvme_over_roce_initiator


##### Function

The **show port nvme_over_roce_initiator** command is used to view the NVMe qualified name (NQN) information about all NVMe over RoCE initiators that are mapped to a port.

##### Format

**show port nvme_over_roce_initiator** port_id=?

##### Parameters

| Parameter | Description   | Value                                                             |
|-----------|---------------|-------------------------------------------------------------------|
| port_id=? | ID of a port. | Run "show port general" without parameters to obtain the port ID. |

##### Usage Guidelines

None

##### Example

View information about all NVMe over RoCE initiators that are mapped to port "CTE0.A.IOM0.P0".

```text
admin:/>show port nvme_over_roce_initiator port_id=CTE0.A.IOM0.P0
NQN            : nqn.2014-08.org.nvmexpress:uuid:6f3d7488-f86e-4f05-a82d-2e0eefabfa6f
Running Status : Online
Free           : No
Alias          : sdf
Host ID        : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                                       |
|----------------|---------------------------------------------------------------|
| NQN            | NQN of an NVMe over RoCE initiator.                           |
| Running Status | Running status of an initiator.                               |
| Free           | Usage status of an initiator.                                 |
| Alias          | Alias of an initiator.                                        |
| Host ID        | ID of the host to which an NVMe over RoCE initiator is added. |
