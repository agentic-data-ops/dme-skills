# show lun_group lun


##### Function

The **show lun_group lun** command is used to query information about LUNs in a specified LUN group.

##### Format

**show lun_group lun** { lun_group_id=? \| lun_group_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_group_id=? | LUN group ID. | To obtain the value, run "show lun_group general". |
| lun_group_name=? | LUN group name. | To obtain the value, run "show lun_group general". |
| lun_id_list=? | List of LUN IDs. | You can run the "show lun general" command to obtain the LUN ID list. When multiple LUNs need to be specified: <br>Multiple LUN IDs can be separated by commas (,). For example, lun_id_list=1,2,3,4,5.<br>You can specify LUN ID ranges by hyphens (-). For example, lun_id_list=1-5,7,9-11. |
| lun_name_list=? | List of LUN names. | You can run the "show lun general" command to obtain the LUN name list. When multiple LUNs need to be specified: You can use commas (,) to separate multiple LUN names or snapshot names. For example, lun_name_list=lun1,lun2,lun3,lun4,lun5. |

##### Usage Guidelines

None

##### Example

Query information about LUNs in LUN group "1".

```text
admin:/>show lun_group lun lun_group_id=1

ID  Name         Pool ID  Capacity    Health Status
--  -----------  -------  ----------  -------------
0   testlun0000  0           2.000GB  Normal

Running Status  Type   WWN
--------------  -----  --------------------------------
Online          Thin  6010203100040506000b780900000000
```

Query information about LUNs in LUN group "LunGroup1".

```text
admin:/>show lun_group lun lun_group_name=LunGroup1

ID  Name         Pool ID  Capacity    Health Status
--  -----------  -------  ----------  -------------
0   testlun0000  0           2.000GB  Normal

Running Status  Type   WWN
--------------  -----  --------------------------------
Online          Thin  6010203100040506000b780900000000
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                   |
|----------------|-------------------------------------------|
| ID             | LUN ID.                                   |
| Name           | LUN name.                                 |
| Pool ID        | ID of the storage pool where LUNs reside. |
| Capacity       | LUN capacity.                             |
| Health Status  | Health status.                            |
| Running Status | Running status.                           |
| Type           | LUN type.                                 |
| WWN            | World Wide Name (WWN) of the LUN.         |
