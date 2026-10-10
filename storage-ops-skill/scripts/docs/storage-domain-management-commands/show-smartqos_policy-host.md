# show smartqos_policy host


##### Function

The **show smartqos_policy host** command is used to query information about hosts in a specified SmartQoS policy.

##### Format

**show smartqos_policy host** smartqos_policy_id=?

##### Parameters

| Parameter          | Description              | Value                            |
|--------------------|--------------------------|----------------------------------|
| smartqos_policy_id | ID of a SmartQoS policy. | The value ranges from 0 to 8191. |

##### Usage Guidelines

None

##### Example

Query information about hosts in SmartQoS policy "0".

```text
admin:/>show smartqos_policy host smartqos_policy_id=0

ID   Name        Operating System

---  ----------  ----------------
0    Host000     Windows
1    Host001     Windows
2    newhost001  Linux
3    newhost002  Linux
4    Host004     Windows
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning           |
|------------------|-------------------|
| ID               | ID of a host.     |
| Name             | Name of a host.   |
| Operating System | Operating system. |
