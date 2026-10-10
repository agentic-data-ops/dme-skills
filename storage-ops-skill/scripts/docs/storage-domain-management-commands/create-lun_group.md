# create lun_group


##### Function

The **create lun_group** command is used to create a LUN group.

##### Format

**create lun_group** name=? \[ lun_group_id=? \] \[ lun_id_list=? \] \[ lun_name_list=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | LUN group name. | The value contains 1 to 255 digits, letters, underscores (_), hyphens (-), and periods (.). |
| lun_group_id=? | LUN group ID. | The value is an integer ranging from 0 to 16383. If you do not specify this parameter, the system automatically allocates an ID for a new LUN group. |
| lun_id_list=? | ID list of LUNs or snapshots that you want to add to a LUN group. | Run the "show lun general" command to obtain the LUN ID list or the "show snapshot general" command to obtain the snapshot ID list. If you want to add multiple LUNs or snapshots to a LUN group: <br>Separate LUN IDs or snapshot IDs with commas (,). For example, "lun_id_list=1,2,3,4,5".<br>Specify LUN ID ranges or snapshot ID ranges with hyphens (-). For example, "lun_id_list=1-5,7,9-11". |
| lun_name_list=? | Name list of LUNs or snapshots that you want to add to a LUN group. | To obtain the value, run "show lun general" or "show snapshot general". If multiple LUNs or snapshots need to be added to a LUN group, separate the LUN or snapshot names with commas (,). For example, lun_name_list=lun1,lun2,lun3,lun4,lun5. |

##### Usage Guidelines

A LUN group can be added with a maximum of 4096 LUNs.

##### Example

Create LUN group "LUNGroupTest" and add LUNs "0", "1", and "2" to this group.

```text
admin:/>create lun_group name=LUNGroupTest lun_id_list=0,1,2
Create LUN group successfully.
Add LUN 0 to LUN group successfully.
Add LUN 1 to LUN group successfully.
Add LUN 2 to LUN group successfully.
```

Create LUN group "LUNGroupTest" and add LUNs "Lun0", "Lun1", and "Lun2" to this group.

```text
admin:/>create lun_group name=LUNGroupTest lun_name_list=Lun0,Lun1,Lun2
Create LUN group successfully.
Add LUN Lun0 to LUN group successfully.
Add LUN Lun1 to LUN group successfully.
Add LUN Lun2 to LUN group successfully.
```

##### System Response

None
