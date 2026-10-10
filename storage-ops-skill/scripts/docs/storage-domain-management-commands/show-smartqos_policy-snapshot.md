# show smartqos_policy snapshot


##### Function

The **show smartqos_policy snapshot** command is used to query the snapshot information of the specified SmartQoS policy.

##### Format

**show smartqos_policy snapshot** smartqos_policy_id=?

##### Parameters

| Parameter            | Description                              | Value                                           |
|----------------------|------------------------------------------|-------------------------------------------------|
| smartqos_policy_id=? | Indicates the ID of the SmartQoS policy. | The value is an integer ranging from 0 to 8191. |

##### Usage Guidelines

Run "**show smartqos_policy snapshot** smartqos_policy_id=?" to query snapshot information of a specified SmartQoS policy.

##### Example

Query snapshot information about SmartQoS policy "1".

```text

admin:/>show smartqos_policy snapshot smartqos_policy_id=1
ID Name Source LUN ID Source LUN Name Health Status Running Status WWN Time Stamp
-- ------- ------------ ------------- ------------- -----------  ------  ----------
8  snap  0    lun0000   Normal  Inactive  6e09796100b4cda20117e31600000008  --
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                |
|-----------------|----------------------------------------|
| ID              | Snapshot ID.                           |
| Name            | Snapshot name.                         |
| Source LUN ID   | Source LUN ID.                         |
| Source LUN Name | Source LUN name.                       |
| Health Status   | Health status of the snapshot.         |
| Running Status  | Running status of the snapshot.        |
| WWN             | World Wide Name (WWN) of the snapshot. |
| Time Stamp      | Activation time of the snapshot.       |
