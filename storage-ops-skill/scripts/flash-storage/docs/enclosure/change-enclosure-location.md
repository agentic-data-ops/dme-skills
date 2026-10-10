# change enclosure location


##### Function

The **change enclosure location** command is used to change the location of an enclosure in a cabinet.

##### Format

**change enclosure location** enclosure_id=? location=?

##### Parameters

| Parameter    | Description                                 | Value                                                                    |
|--------------|---------------------------------------------|--------------------------------------------------------------------------|
| enclosure_id | ID of a disk enclosure with the prefix DAE. | To obtain the value, run the "show enclosure" command.                   |
| location     | Location of a disk enclosure in a cabinet.  | Cabinet ID and enclosure location in the cabinet, for example, SMB0.20U. |

##### Usage Guidelines

None

##### Example

Change the location of the enclosure DAE000 to SMB0.20U. The following output is used as an example only.

```text
admin:/>change enclosure location enclosure_id=DAE000 location=SMB0.20U
DANGER: You are about to change the location of an enclosure in the cabinet.
This operation will affect the enclosure location in the cabinet displayed on DeviceManager.
Suggestion: Before performing this operation, ensure that the operation is necessary.
Have you read danger alert message carefully?(y/n)Y
Are you sure you really want to perform the operation?(y/n)Y
Command executed successfully.
```

##### System Response

None
