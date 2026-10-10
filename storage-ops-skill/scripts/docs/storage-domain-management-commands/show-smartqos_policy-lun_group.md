# show smartqos_policy lun_group


##### Function

The **show smartqos_policy lun_group** command is used to query information about LUN groups in a specified SmartQoS policy.

##### Format

**show smartqos_policy lun_group** smartqos_policy_id=?

##### Parameters

| Parameter          | Description              | Value                            |
|--------------------|--------------------------|----------------------------------|
| smartqos_policy_id | ID of a SmartQoS policy. | The value ranges from 0 to 8191. |

##### Usage Guidelines

None

##### Example

Query information about LUN groups in SmartQoS policy "0".

```text
admin:/>show smartqos_policy lun_group smarqos_policy_id=0
ID  Name       IS Add To Mapping View  Smart Qos Policy ID
--  ---------  ----------------------  -------------------
0   lungroup1  Yes                     0
```

##### System Response

The following table describes the parameter meanings.

| Parameter              | Meaning                                               |
|------------------------|-------------------------------------------------------|
| ID                     | ID of a LUN group.                                    |
| Name                   | Name of a LUN group.                                  |
| IS Add To Mapping View | Whether a LUN group is added to the mapping view.     |
| Smart Qos Policy ID    | ID of the SmartQoS policy configured for a LUN group. |
