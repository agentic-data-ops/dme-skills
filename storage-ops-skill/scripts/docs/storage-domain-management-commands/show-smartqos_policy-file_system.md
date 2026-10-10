# show smartqos_policy file_system


##### Function

The **show smartqos_policy file_system** command is used to query information about file systems in a specified SmartQoS policy.

##### Format

**show smartqos_policy file_system** smartqos_policy_id=?

##### Parameters

| Parameter            | Description              | Value                                                    |
|----------------------|--------------------------|----------------------------------------------------------|
| smartqos_policy_id=? | ID of a SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |

##### Usage Guidelines

None

##### Example

Query information about file systems in SmartQoS policy "0".

```text
admin:/>show smartqos_policy file_system smartqos_policy_id=0
ID Name Storage Pool ID   Capacity Health Status  Running Status
-- ---- ----------------  -------- ------------- --------------
0 FS000 0                 10.000GB Normal         Online
1 FS001 0                 10.000GB Normal         Online
2 FS002 0                 10.000GB Normal         Online
3 FS003 0                 10.000GB Normal         Online
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                                |
|-----------------|--------------------------------------------------------|
| ID              | File system ID.                                        |
| Name            | File system name.                                      |
| Storage Pool ID | ID of the storage pool to which a file system belongs. |
| Capacity        | File system capacity.                                  |
| Health Status   | Health status.                                         |
| Running Status  | Running status.                                        |
