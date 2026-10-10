# create nvme_over_roce_initiator general


##### Function

The **create nvme_over_roce_initiator general** command is used to create an NVMe over RoCE initiator so that a host can access the storage system resources through the initiator.

##### Format

**create nvme_over_roce_initiator general** nvme_over_roce_nqn=? \[ alias=? \] \*

##### Parameters

| Parameter            | Description                          | Value                                                                                                            |
|----------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------|
| nvme_over_roce_nqn=? | NQN of the NVMe over RoCE initiator. | The value contains 1 to 223 characters (32 \< ASCII code \< 127) and must start with a letter or digit.          |
| alias=?              | Alias of the initiator.              | The value contains 1 to 31 characters including digits, letters, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

None

##### Example

Create the NVMe over RoCE initiator whose NVMe qualified name (NQN) is "455856585f654578".

```text
admin:/>create nvme_over_roce_initiator general nvme_over_roce_nqn=455856585f654578
Command executed successfully.
```

##### System Response

None
