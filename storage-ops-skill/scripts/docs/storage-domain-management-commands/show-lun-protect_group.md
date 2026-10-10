# show lun protect_group


##### Function

The **show lun protect_group** command is used to query the protection group associated with a LUN.

##### Format

**show lun protect_group** lun_id=?

**show lun protect_group** lun_name=?

##### Parameters

| Parameter | Description | Value                                                    |
|-----------|-------------|----------------------------------------------------------|
| lun_id=?  | LUN ID.     | To obtain the value, run the "show lun general" command. |
| lun_name  | LUN name.   | To obtain the value, run the "show lun general" command. |

##### Usage Guidelines

None

##### Example

Query information about the protection group associated with the LUN whose ID is 0.

```text
admin:/>show lun protect_group lun_id=0

Protect Group ID  Protect Group Name  LUN Group ID
----------------  ------------------  ------------
0                 ProtectGroup000      --
```

Query information about the protection group associated with the LUN whose name is to_pg.

```text

admin:/>show lun protect_group lun_name=to_pg
Protect Group ID Protect Group Name LUN Group ID
---------------- ------------------ ------------
0                PG0001             --
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                |
|--------------------|------------------------|
| Protect Group ID   | Protection group ID.   |
| Protect Group Name | Protection group name. |
| LUN Group ID       | LUN group ID.          |
