# show lun lun_group


##### Function

The **show lun lun_group** command is used to query information about the LUN group that is associated with a LUN.

##### Format

**show lun lun_group** { lun_id=? \| lun_name=? }

##### Parameters

| Parameter  | Description | Value                                        |
|------------|-------------|----------------------------------------------|
| lun_id=?   | LUN ID.     | To obtain the value, run "show lun general". |
| lun_name=? | LUN name.   | To obtain the value, run "show lun general". |

##### Usage Guidelines

None.

##### Example

Query information about the LUN group that is associated with LUN "0".

```text
admin:/>show lun lun_group lun_id=0

LUN Group ID  LUN Group Name
------------  --------------
0             LUNGroup000
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                |
|----------------|------------------------|
| LUN Group ID   | ID of the LUN group.   |
| LUN Group Name | Name of the LUN group. |
