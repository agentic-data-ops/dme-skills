# change vstore info


##### Function

The **change vstore info** command is used to modify the basic information about a vStore.

##### Format

**change vstore info** { id=? \| vstore_name=? } { name=? \| description=? }

##### Parameters

| Parameter     | Description                                              | Value                                                                                                              |
|---------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| id=?          | ID of the vStore whose information you want to modify.   | The value ranges from 1 to 1023. To obtain the value, run the "show vstore" command.                               |
| vstore_name   | Name of the vStore whose information you want to modify. | The value contains 1 to 256 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |
| name=?        | New vStore name.                                         | The value contains 1 to 256 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |
| description=? | New vStore description.                                  | The value contains a maximum of 255 characters.                                                                    |

##### Usage Guidelines

Before running this command, ensure that the selected vStore is exactly the one you want to modify.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Modify the description and the name of the vStore whose ID is "1".

```text
admin:/>change vstore info id=1 name=test1 description=test1
Command executed successfully.
admin:/>show vstore id=1
ID                          : 1
Name                        : test1
Running Status              : Normal
Description                 : test1
FileSystem Capacity         : 256.000KB
FileSystem Used Capacity    : 50.000MB
FileSystem UnUsed Capacity  : 2.441GB
Lun Count                   : 0
Unmapped Lun Count          : 0
Mapped Lun Total Capacity   : 0.000B
Mapped Lun Count            : 0
Unmapped Lun Total Capacity : 0.000B
FileSystem Count            : 0
Lun Total Capacity          : 0.000B
admin:/>

```

Modify the description and the name of the vStore whose name is "test".

```text
admin:/>change vstore info vstore_name=test name=test1 description=test1
Command executed successfully.
admin:/>show vstore id=1
ID                          : 1
Name                        : test1
Running Status              : Normal
Description                 : test1
FileSystem Capacity         : 256.000KB
FileSystem Used Capacity    : 50.000MB
FileSystem UnUsed Capacity  : 2.441GB
Lun Count                   : 0
Unmapped Lun Count          : 0
Mapped Lun Total Capacity   : 0.000B
Mapped Lun Count            : 0
Unmapped Lun Total Capacity : 0.000B
FileSystem Count            : 0
Lun Total Capacity          : 0.000B
admin:/>
```

##### System Response

None
