# show lun_consistency_group lun


##### Function

The **show lun_consistency_group lun** command is used to query information about LUNs in a LUN consistency group.

##### Format

**show lun_consistency_group lun** lun_consistency_group_id=?

##### Parameters

| Parameter                  | Description                                    | Value                                                                                         |
|----------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------|
| lun_consistency_group_id=? | ID of the LUN consistency group to be queried. | To obtain the value, run the "show lun_consistency_group general" command without parameters. |

##### Usage Guidelines

Run the "**show lun_consistency_group lun** lun_consistency_group_id=?" command to query information about member LUNs in a LUN consistency group.

##### Example

Query information about LUNs in a specified LUN consistency group.

```text
admin:/>show lun_consistency_group lun lun_consistency_group_id=1
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

| Parameter           | Meaning                             |
|---------------------|-------------------------------------|
| ID                  | ID of a LUN.                        |
| Name                | Name of a LUN.                      |
| Pool ID             | ID of a storage pool.               |
| Health Status       | Health status.                      |
| Running Status      | Running status.                     |
| Type                | Type of a LUN.                      |
| Is Add To Lun Group | Whether to be added to a LUN group. |
