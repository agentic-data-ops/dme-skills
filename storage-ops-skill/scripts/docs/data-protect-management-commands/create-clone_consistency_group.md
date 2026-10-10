# create clone_consistency_group


##### Function

The **create clone_consistency_group** command is used to create a clone consistency group.

##### Format

**create clone_consistency_group** name=? { source_protect_group_id_list=? \| source_protect_group_name_list=? } \[ copy_speed=? \] \[ description=? \] \[ start_synchronize_after_create=? \] \[ is_create_dst_lun=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of the clone CG. | The value is a string of 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| source_protect_group_id_list=? | ID list of the protection groups for which a clone consistency group is to be created. | You can run the show protect_group general command to obtain the protection group ID list. To create clone consistency groups for multiple protection groups: <br>Multiple protection group IDs can be separated by commas (,). For example, source_protect_group_id_list=1,2,3,4,5.<br>You can specify the range of protection group IDs by hyphens (-). For example, source_protect_group_id_list=1-5,7,9-11. |
| source_protect_group_name_list=? | Name list of the protection groups for which a clone consistency group is to be created. | To obtain the value, run the "show protect_group general" command. If you need to create clone consistency groups for multiple protection groups at the same time, separate the protection group names with commas (,). |
| copy_speed=? | Copy rate. | The value can be "low", "middle", "high", or "highest", where: <br>"low": low speed.<br>"middle": medium speed.<br>"high": high speed.<br>"highest": highest speed.<br> The default value is "middle". |
| description=? | Description of the clone CG. | - |
| start_synchronize_after_create=? | Whether to start data synchronization after a clone CG is created. | The value can be "yes" or "no", where: <br>"yes": synchronization is started immediately after the creation.<br>"no": Synchronization is not started after the creation. |
| is_create_dst_lun=? | Whether to create a target LUN. | The value can be "yes" or "no", where: <br>"yes": Create a target LUN.<br>"no": Do not create a target LUN. |

##### Usage Guidelines

None

##### Example

Create a clone consistency group named "clone_cg".

```text
admin:/>create clone_consistency_group name=clone_cg source_protect_group_id_list=0
Create clone consistency group successfully.
```

##### System Response

None
