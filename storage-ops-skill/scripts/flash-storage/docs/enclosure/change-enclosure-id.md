# change enclosure id


##### Function

The **change enclosure id** command is used to modify the ID of a disk enclosure.

##### Format

**change enclosure id** old_id=? new_id=?

##### Parameters

| Parameter | Description                                 | Value                                                  |
|-----------|---------------------------------------------|--------------------------------------------------------|
| old_id=?  | ID of a disk enclosure with the prefix DAE. | To obtain the value, run the "show enclosure" command. |
| new_id    | ID of a disk enclosure with the prefix DAE. | Values range from DAE000 to DAEFFF.                    |

##### Usage Guidelines

None

##### Example

Change the disk enclosure ID from "DAE000" to "DAE001". The following output is used as an example only.

```text
admin:/>change enclosure id old_id=DAE000 new_id=DAE001
DANGER: You are about to modify the ID of a disk enclosure.
This operation will change the locations of all components in the disk enclosure.
Suggestion: Before performing this operation, determine whether the operation is necessary.
Have you read danger alert message carefully?(y/n)Y
Are you sure you really want to perform the operation?(y/n)Y
Command executed successfully.
```

##### System Response

None
