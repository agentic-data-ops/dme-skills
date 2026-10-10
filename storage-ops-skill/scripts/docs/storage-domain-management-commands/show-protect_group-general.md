# show protect_group general


##### Function

The **show protect_group general** command is used to query information about a protection group.

##### Format

**show protect_group general** \[ protect_group_id=? \]

##### Parameters

| Parameter          | Description          | Value                                                                                                                                                                                           |
|--------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| protect_group_id=? | Protection group ID. | To obtain the value, run the "**show protect_group general**" command. |

##### Usage Guidelines

-   The "**show protect_group general**" command is used to query information about all protection groups in the system.
-   The "**show protect_group general** protect_group_id=?" command is used to query information about a specified protection group.

##### Example

Query information about all protection groups in the system.

```text
admin:/>show protect_group general
ID  Name  LUN Group ID  LUN Group Name LUN Num  Snapshot Clone HyperCDP Replication HyperMetro
--  ----  ------------  -------------- -------  -------- ----- -------- ----------- ----------
1   pg1   0             testlg1        0        0        0     0        0           0
```

Query information about the protection group whose ID is 1.

```text
admin:/>show protect_group general protect_group_id=1
ID            : 1
Name          : pg1
Description   :
LUN Group ID  : 0
LUN Group Name: testlg1
LUN Num       : 0
Snapshot Group Name    : sg1,sg2
Clone Group Name       : cg1,cg2
HyperCDP Group Num     : 0
Replication Group Name : rg1
HyperMetro Group Name  : hm1
```

##### System Response

The following table describes the parameter meanings.

| Parameter              | Meaning                                 |
|------------------------|-----------------------------------------|
| ID                     | Protection group ID.                    |
| Name                   | Protection group name.                  |
| Description            | Description.                            |
| LUN Group ID           | LUN group ID.                           |
| LUN Group Name         | LUN group name.                         |
| LUN Num                | Number of LUNs.                         |
| Replication Group Num  | Number of remote replication groups.    |
| Replication Group Name | Name list of remote replication groups. |
| Snapshot Group Name    | Name list of snapshot groups.           |
| Snapshot Group Num     | Number of snapshot groups.              |
| HyperCDP Group Num     | Number of HyperCDP groups.              |
| HyperMetro Group Num   | Number of HyperMetro groups.            |
| HyperMetro Group Name  | Name list of HyperMetro groups.         |
| Clone Groups Num       | Number of clone groups.                 |
| Clone Group Name       | Name list of clone groups.              |
