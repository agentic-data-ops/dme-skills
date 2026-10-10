# show vstore


##### Function

The **show vstore** command is used to query the states of vStores.

##### Format

**show vstore** \[ id=? \| name=? \]

##### Parameters

| Parameter | Description       | Value                                                                                                                                                                                                                         |
|-----------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id=?      | ID of a vStore.   | The value is an integer ranging from 0 to 1023. To obtain the value, run the "**show vstore**" command.            |
| name=?    | Name of a vStore. | The value contains 1 to 256 characters. To obtain the value, run the "**show vstore**" command without parameters. |

##### Usage Guidelines

-   Run the "**show vstore**" command to query the states of vStores.
-   Run the "**show vstore** id=?" command to query the state of a specified vStore.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the vStore whose ID is "1".

```text
admin:/>show vstore id=1
ID                          : 1
Name                        : test
Running Status              : Normal
Description                 : sdf
FileSystem Capacity         : 10.000GB
FileSystem Used Capacity    : 50.000MB
FileSystem UnUsed Capacity  : 2.441GB
Lun Count                   : 0
Unmapped Lun Count          : 0
Mapped Lun Total Capacity   : 0.000B
Mapped Lun Count            : 0
Unmapped Lun Total Capacity : 0.000B
FileSystem Count            : 0
Lun Total Capacity          : 0.000B
Audit Log Strategy Enabled  : No
admin:/>
```

Query information on existing vStores of the storage system.

```text
admin:/>show vstore
ID  Name           Running Status  Lun Count  Unmapped Lun Count  Mapped Lun Count  FileSystem Count Audit Log Strategy Enabled
--  -------------  --------------  ---------  ------------------  ----------------  ---------------- --------------------------
0   System_vStore  Normal          0          0                   0                 0                No
1   test           Normal          0          0                   0                 0                No
2   vs             Normal          0          0                   0                 0                No
admin:/>
```

Query the vStore whose name is "test".

```text
admin:/>show vstore name=test
ID                          : 1
Name                        : test
Running Status              : Normal
Description                 : sdf
FileSystem Capacity         : 10.000GB
FileSystem Used Capacity    : 50.000MB
FileSystem UnUsed Capacity  : 2.441GB
Lun Count                   : 0
Unmapped Lun Count          : 0
Mapped Lun Total Capacity   : 0.000B
Mapped Lun Count            : 0
Unmapped Lun Total Capacity : 0.000B
FileSystem Count            : 0
Lun Total Capacity          : 0.000B
Audit Log Strategy Enabled  : No
admin:/>
```

##### System Response

The following table describes the parameter meanings.

| Parameter                   | Meaning                                           |
|-----------------------------|---------------------------------------------------|
| ID                          | vStore ID.                                        |
| Name                        | vStore name.                                      |
| Description                 | vStore description.                               |
| Running Status              | Running status.                                   |
| FileSystem Capacity         | Configured capacity of a file system.             |
| FileSystem Used Capacity    | Used capacity of a file system.                   |
| FileSystem UnUsed Capacity  | Unused capacity of a file system.                 |
| Lun Count                   | Number of LUNs.                                   |
| Unmapped Lun Count          | Number of unmapped LUNs.                          |
| Mapped Lun Total Capacity   | Total capacity of mapped LUNs.                    |
| Mapped Lun Count            | Number of mapped LUNs.                            |
| Unmapped Lun Total Capacity | Total capacity of unmapped LUNs.                  |
| FileSystem Count            | Number of file systems.                           |
| Lun Total Capacity          | Total LUN capacity.                               |
| Audit Log Strategy Enabled  | Check whether the audit log policy is configured. |
