# create role general


##### Function

The **create role general** command is used to create roles.

##### Format

**create role general** name=? group=? \[ description=? \] \[**permit_list=***?*\]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Role name. | The name contains 1 to 63 letters, digits, underscores (_), periods (.), and hyphens (-). |
| group=? | Owning group of a role. | The value is "system" indicating a system group. |
| description=? | Role description. | The description contains a maximum of 255 characters. |
| permit_list=? | Role permission. | The value contains a maximum of 6144 characters. The value is in the format of "Directory1:Object1_W,Object2_R;Directory2:Object2_W,Object3_R;Directory3:all", where: <br>"Directory1", "Directory2", and "Directory3" indicate directories for which the role will have permission.<br>"Object1", "Object2", "Object3", and "all" indicate objects in the directory. "Object1", "Object2", and "Object3" indicate a single object. An object with "_W" indicates that the object can be written by the role and that with "_R" indicates that the object can be read by the role, and "all" indicates that all objects in the directory can be read and written by the role. |

##### Usage Guidelines

None

##### Example

Create user-defined role "testrole".

```text
admin:/>create role general name=testrole group=system
Command executed successfully.
```

##### System Response

None
