# create vstore general


##### Function

The **create vstore general** command is used to create a vStore.

##### Format

**create vstore general** name=? \[ description=? \]

##### Parameters

| Parameter     | Description         | Value                                                                                                              |
|---------------|---------------------|--------------------------------------------------------------------------------------------------------------------|
| name=?        | vStore name.        | The value contains 1 to 256 characters, including letters, digits, underscores (\_), periods (.), and hyphens (-). |
| description=? | vStore description. | The value contains a maximum of 255 characters.                                                                    |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Create a vStore with the name of "vstore1".

```text
admin:/>create vstore general name=vstore1 description=test
Command executed successfully.
admin:/>show vstore name=vstore1
ID                          : 3
Name                        : vstore1
Running Status              : Normal
Description                 : test
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
