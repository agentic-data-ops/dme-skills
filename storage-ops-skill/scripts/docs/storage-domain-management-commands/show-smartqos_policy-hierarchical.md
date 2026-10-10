# show smartqos_policy hierarchical


##### Function

The **show smartqos_policy hierarchical** command is used to query information about SmartQoS policies in a specified hierarchical SmartQoS policy.

##### Format

**show smartqos_policy hierarchical** hierarchical_smartqos_policy_id=?

##### Parameters

| Parameter                         | Description                           | Value                                                    |
|-----------------------------------|---------------------------------------|----------------------------------------------------------|
| hierarchical_smartqos_policy_id=? | ID of a hierarchical SmartQoS policy. | To obtain the value, run "show smartqos_policy general". |

##### Usage Guidelines

Run the "**show smartqos_policy hierarchical** hierarchical_smartqos_policy_id=?" command to query information about SmartQoS policies in a specified hierarchical SmartQoS policy.

##### Example

Query information about SmartQoS policies in hierarchical SmartQoS policy "0".

```text
admin:/>show smartqos_policy hierarchical hierarchical_smartqos_policy_id=0
ID Name Health Status Running Status IO Type Enabled LUN List Filesystem List Ctrl Type
-- ------- ------------- -------------- ---------- ------- -------- -------  -------

0 newqos Normal Inactive Read_write No -- --  Normal
3 newqos2 Normal Inactive Read_write No 0,1,2 --  Normal
2 newqos3 Normal Inactive Read_write No 7 --  Normal
4 newqos4 Normal Inactive Read_write No 6 --  Normal
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                               |
|-----------------|-------------------------------------------------------|
| Ctrl Type       | Type of the SmartQoS policy that you want to control. |
| Filesystem List | ID of file systems that you add to a SmartQoS policy. |
| LUN List        | ID of LUNs that you add to a SmartQoS policy.         |
| Health Status   | Health status.                                        |
| Running Status  | Running status.                                       |
| IO Type         | Type of the I/O that you want to control.             |
| Enabled         | State of a SmartQoS policy.                           |
| ID              | ID of a SmartQoS policy.                              |
| Name            | Name of a SmartQoS policy.                            |
