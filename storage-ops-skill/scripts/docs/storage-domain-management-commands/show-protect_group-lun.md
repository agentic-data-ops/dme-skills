# show protect_group lun


##### Function

The **show protect_group lun** command is used to query information about LUNs in a protection group.

##### Format

**show protect_group lun** protect_group_id=?

##### Parameters

| Parameter          | Description          | Value                                                              |
|--------------------|----------------------|--------------------------------------------------------------------|
| protect_group_id=? | Protection group ID. | To obtain the value, run the "show protect_group general" command. |

##### Usage Guidelines

None

##### Example

Query information about LUNs in a specified protection group.

```text
admin:/>show protect_group lun protect_group_id=1
ID  Name   Pool ID  Health Status  Running Status  Type  Is Add To Lun Group
--  -----  -------  -------------  --------------  ----  -------------------
0   l0000  0        Normal         Online          Thin  No
1   l0001  0        Normal         Online          Thin  No
2   l0002  0        Normal         Online          Thin  No
3   l0003  0        Normal         Online          Thin  No
4   l0004  0        Normal         Online          Thin  No
5   l0005  0        Normal         Online          Thin  No
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning                                |
|---------------------|----------------------------------------|
| ID                  | LUN ID.                                |
| Name                | LUN name.                              |
| Pool ID             | Storage pool ID.                       |
| Health Status       | Health status.                         |
| Running Status      | Running status.                        |
| Type                | LUN type.                              |
| Is Add To Lun Group | Whether a LUN is added to a LUN group. |
