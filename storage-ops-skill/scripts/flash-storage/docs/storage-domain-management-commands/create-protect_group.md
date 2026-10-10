# create protect_group


##### Function

The **create protect_group** command is used to create a protection group.

##### Format

**create protect_group** name=? \[ protect_group_id=? \] { lun_id_list=? \| lun_group_id=? } \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Protection group name. | The value contains 1 to 255 characters including digits, letters, underscores (_), hyphens (-), and periods (.). |
| lun_id_list=? | ID list of LUNs added to a protection group. | To obtain the LUN ID list, run the "show lun general" command. When multiple LUNs are added to a protection group, you can: <br>Use commas (,) to separate IDs of multiple LUNs. For example, "lun_id_list=1,2,3,4,5".<br>Use hyphens (-) to specify a LUN ID range. For example, "lun_id_list=1-5,7,9-11". |
| lun_group_id=? | LUN group ID. | To obtain the LUN group ID, run the "show lun_group general" command. |
| protect_group_id=? | Protection group ID. | The value is an integer from 0 to 16383. If this parameter is not specified, the system automatically assigns an ID to the new protection group. |
| description=? | Description. | - |

##### Usage Guidelines

To query the maximum number of protection groups that can be created and the maximum number of LUNs of LUN groups that can be added to a protection group, visit https://support-it.huawei.com/spec/#/home.

##### Example

Create protection group named "pg1".

```text
admin:/>create protect_group name=pg1
Create protect group successfully.
```

Create protection group named "pg" and add LUNs whose IDs are "0", "1", and "2" to this group.

```text
admin:/>create protect_group name=pg lun_id_list=0,1,2
Create protect group successfully.
Adding LUNs to PG or LUN group (pg) in background.
Run the "show task general task_id=1" command to query the execution result.
```

##### System Response

None
