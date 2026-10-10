# show recycle_bin_view general


##### Function

The **show recycle_bin_view general** command is used to query object information in the recycle bin view.

##### Format

**show recycle_bin_view general** \[ delete_type=? { parent_id=? \| delete_id=? \| delete_name=? } \]

##### Parameters

| Parameter   | Description               | Value                                                                                                              |
|-------------|---------------------------|--------------------------------------------------------------------------------------------------------------------|
| delete_type | Type of a deleted object. | The value is "LUN".                                                                                                |
| delete_id   | ID of a deleted object.   | The value ranges from 1 to 65535.                                                                                  |
| delete_name | Name of a deleted object. | The value contains 1 to 255 characters, including digits, letters, underscores (\_), hyphens (-), and periods (.). |
| parent_id   | Parent object ID.         | The value ranges from 1 to 65535.                                                                                  |

##### Usage Guidelines

-   Run the "**show recycle_bin_view general**" command to query all object information in the recycle bin view.
-   Run the "**show recycle_bin_view general** delete_type=?" command to query information about objects of a specified type in the recycle bin view.
-   Run the "**show recycle_bin_view general** delete_type=? parent_id=?" command to query details of the sub-object of a specified ID in the recycle bin view.
-   Run the "**show recycle_bin_view general** delete_type=? delete_id=?" command to query details of the object of a specified type and ID in the recycle bin view.
-   Run the "**show recycle_bin_view general** delete_type=? delete_name=?" command to query details of the object of a specified type and name in the recycle bin view.

##### Example

Query all object information in the recycle bin view.

```text
admin:/>show recycle_bin_view general
Type  ID         Name    AllocCapacity  Capacity   WWN                               Parent Id  Parent Name  Childrens  Delete Time
----  ---------  ------  -------------  ---------  --------------------------------  ---------  -----------  ---------  -----------------------------
LUN   10         snap11         0.000B  100.000GB  6ac8d34100eea90a0023f74b0000000a  0          LUN001       0          2020-09-11/14:26:37 UTC+08:00
LUN   9          snap5          0.000B    3.000GB  6ac8d34100eea90a0023ea8e00000009  2          LUN003       0          2020-09-11/14:26:37 UTC+08:00
LUN   8          snap31         0.000B    4.000GB  6ac8d34100eea90a0023e2bd00000008  4          snap1        0          2020-09-11/14:26:37 UTC+08:00
LUN   4          snap1          0.000B    4.000GB  6ac8d34100eea90a0001199500000004  3          LUN004       1          2020-09-11/14:26:39 UTC+08:00
```

Query information about all objects whose type is "11" (LUN) and parent object ID is "5" in the recycle bin view.

```text
admin:/>show recycle_bin_view general delete_type=LUN parent_id=5
Type  ID         Name      AllocCapacity  Capacity   WWN                               Parent Id  Parent Name  Childrens  Delete Time
----  ---------  --------  -------------  ---------  --------------------------------  ---------  -----------  ---------  -----------------------------
LUN   6          gx_s_1           0.000B  100.000GB  6e4c2d1100ed4999003687ec00000006  5          gx           1022       2021-01-09/17:50:04 UTC+14:00
LUN   7          gx_s_2           0.000B  100.000GB  6e4c2d1100ed49990036926200000007  5          gx           0          2021-01-09/17:31:20 UTC+14:00
LUN   662        gx_clone         0.000B  100.000GB  6e4c2d1100ed49990039394700000296  5          gx           0          2021-01-09/17:43:45 UTC+14:00
```

Query information about the object whose type is "11" (LUN) and ID is "5" in the recycle bin view.

```text
admin:/>show recycle_bin_view general delete_type=LUN delete_id=95
Type          : LUN
ID            : 95
Name          : gx_snap86
AllocCapacity : 0.000B
Capacity      : 100.000GB
WWN           : 6e4c2d1100ed4999003810480000005f
Parent Id     : 6
Parent Name   : gx_s_1
Childrens     : 0
Delete Time   : 2021-01-09/17:31:45 UTC+14:00
```

##### System Response

The following table describes the parameter meanings.

| Parameter          | Meaning                                          |
|--------------------|--------------------------------------------------|
| Type               | Type of a deleted object.                        |
| ID                 | ID of a deleted object.                          |
| Name               | Name of a deleted object.                        |
| AllocCapacity      | Used capacity, in sectors.                       |
| Capacity           | Configured capacity, in sectors.                 |
| WWN                |                                                  |
| Parent Id          | Parent object ID.                                |
| Parent Name        | Parent object name.                              |
| Childrens          | Number of sub-objects.                           |
| Delete Object Time | Time when an object is moved to the recycle bin. |
