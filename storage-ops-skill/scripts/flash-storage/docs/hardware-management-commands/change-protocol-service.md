# change protocol service


##### Function

The **change protocol service** command is used to perform operations on protocol objects, such as migrating LUN reservation information.

##### Format

**change protocol service** operation_code=? operation_object_type=? operation_object_id=?

##### Parameters

| Parameter               | Description            | Value                                            |
|-------------------------|------------------------|--------------------------------------------------|
| operation_code=?        | Operation code.        | This value must be set to "relocate".            |
| operation_object_type=? | Operation object type. | This value must be set to "lun_reservation".     |
| operation_object_id=?   | Operation object ID.   | The value is an integer ranging from 0 to 65535. |

##### Usage Guidelines

None.

##### Example

Migrate LUN reservation information.

```text
admin:/>change protocol service operation_code=relocate operation_object_type=lun_reservation operation_object_id=1
Command executed successfully.
```

##### System Response

None
