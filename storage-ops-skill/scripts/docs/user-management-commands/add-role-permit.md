# add role permit


##### Function

The **add role permit** command is used to add permissions to roles.

##### Format

**add role permit** id=? permit_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| id=? | Role ID. The value must be an integer from 1 to 1023. | To obtain the value, run the "show role system" command. |
| permit_list=? | List of added permissions. | The value contains a maximum of 6144 characters. The value is in the format of "Directory1:Object1_W,Object2_R;Directory2:Object2_W,Object3_R;Directory3:all", where: <br>"Directory1", "Directory2", and "Directory3" indicate directories for which the role will have permission.<br>"Object1", "Object2", "Object3", and "all" indicate objects in the directory. "Object1", "Object2", and "Object3" indicate a single object. An object with "_W" indicates that the object can be written by the role and that with "_R" indicates that the object can be read by the role, and "all" indicates that all objects in the directory can be read and written by the role. |

##### Usage Guidelines

None

##### Example

Add permission "lun:lun_R" to the role whose ID is "65".

```text
admin:/>add role permit id=65 permit_list=lun:lun_R
Command executed successfully.
```

##### System Response

None
