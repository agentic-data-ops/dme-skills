# show lun_group general


##### Function

The **show lun_group general** command is used to query information about LUN groups.

##### Format

**show lun_group general** \[ lun_group_id=? \| lun_group_name=? \] \[ lun_group_id_list=? \] \[ lun_group_name_list=? \]

##### Parameters

| Parameter             | Description              | Value                                                                                                                                                                                              |
|-----------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lun_group_id=?        | LUN group ID.            | To obtain the value, run "**show lun_group general**" without parameters. |
| lun_group_name=?      | LUN group name.          | To obtain the value, run "**show lun_group general**" without parameters. |
| lun_group_id_list=?   | List of LUN group IDs.   | Use commas (,) to separate multiple IDs or use a hyphen (-) to specify an ID range.                                                                                                                |
| lun_group_name_list=? | List of LUN group names. | Separate multiple LUN group names by commas (,) or use a hyphen (-) to specify a LUN group name range. The name formats and lengths before and after a hyphen (-) must be the same.                |

##### Usage Guidelines

None

##### Example

Query information about all LUN groups.

```text
admin:/>show lun_group general

ID  Name                IS Add To Mapping View  Smart Qos Policy ID
--  ----------------    ----------------------  -------------------
0   group1              Yes                     0
```

##### System Response

The following table describes the parameter meanings.

| Parameter              | Meaning                                               |
|------------------------|-------------------------------------------------------|
| ID                     | ID of a LUN group.                                    |
| Name                   | Name of a LUN group.                                  |
| IS Add To Mapping View | Whether to add the LUN group to the mapping view.     |
| Smart Qos Policy ID    | ID of the SmartQoS policy configured for a LUN group. |
