# show nvme_over_roce_initiator general


##### Function

The **show nvme_over_roce_initiator general** command is used to query information about NVMe over RoCE initiators added to hosts in the storage system.

##### Format

**show nvme_over_roce_initiator general** \[ nvme_over_roce_nqn=? \| isfree=? \| host_id=? \| host_name=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_id=? | Host ID. | To obtain the value, run "show host general". |
| host_name=? | Host name. | To obtain the value, run "show host general". |
| isfree=? | Whether an initiator is idle. | The value can be "yes" or "no", where: <br>"yes": the initiator is idle and can be added to a host.<br>"no": the initiator has been engaged by a host and cannot be added to another host. |
| nvme_over_roce_nqn=? | NVMe qualified name (NQN) of an NVMe over RoCE initiator. | To obtain the value, run "show nvme_over_roce_initiator general". |

##### Usage Guidelines

None

##### Example

Query information about NVMe over RoCE initiators.

```text

admin:/>show nvme_over_roce_initiator general

NQN               Running Status  Free  Alias  Host ID  Host IP
----------------  --------------  ----  -----  -------  -------
100000109b56d2cd  Offline         No    112    1        1.1.1.1

```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                             |
|----------------|-------------------------------------|
| NQN            | NQN of an NVMe over RoCE initiator. |
| Running Status | Running status of an initiator.     |
| Free           | Whether an initiator is idle.       |
| Alias          | Initiator alias.                    |
| Host ID        | Host ID.                            |
| Host IP        | Host IP address.                    |
