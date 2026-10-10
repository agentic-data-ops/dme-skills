# show workload_type general


##### Function

The **show workload_type general** command is used to query information about existing application types of the storage system.

##### Format

**show workload_type general** \[ id=? \| name=? \]

##### Parameters

| Parameter | Description            | Value                                                                                                                                                                                                |
|-----------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id=?      | Application type ID.   | To obtain the value, run "**show workload_type general**" without parameters. |
| name=?    | Application type name. | To obtain the value, run "**show workload_type general**" without parameters. |

##### Usage Guidelines

-   Run the "**show workload_type general**" command to query information about all application types of the storage system.
-   Run the "**show workload_type general** id=?" command to query information about a specified application type by ID.
-   Run the "**show workload_type general** name=?" command to query information about a specified application type by name.

##### Example

Query information about all application types of the storage system.

```text

admin:/>show workload_type general
ID  Name                  IO Size  Type
--  --------------------  -------  --------
0   Default               8KB      Reserved
1   Oracle_OLAP           32KB     Reserved
2   Oracle_OLTP           8KB      Reserved
3   Oracle_OLAP&OLTP      8KB      Reserved
4   SQL_Server_OLAP       32KB     Reserved
5   SQL_Server_OLTP       8KB      Reserved
6   SQL_Server_OLAP&OLTP  8KB      Reserved
7   SAP_HANA              8KB      Reserved
8   Vmware_VDI            8KB      Reserved
9   Hyper-V_VDI           8KB      Reserved
10  FusionAccess_VDI      8KB      Reserved
11  NAS_Default           16KB     Reserved
12  NAS_Virtual_Machine   16KB     Reserved
13  NAS_Database          8KB      Reserved
14  NAS_Large_File        32KB     Reserved
15  Office_Automation     16KB     Reserved
1025  NAS_EDA             16KB     Reserved

developer:/>show workload_type general
ID  Name                  IO Size  Type
--  --------------------  -------  --------
0   Default               8KB      Reserved
1   Oracle_OLAP           32KB     Reserved
2   Oracle_OLTP           8KB      Reserved
3   Oracle_OLAP&OLTP      8KB      Reserved
4   SQL_Server_OLAP       32KB     Reserved
5   SQL_Server_OLTP       8KB      Reserved
6   SQL_Server_OLAP&OLTP  8KB      Reserved
7   SAP_HANA              8KB      Reserved
8   Vmware_VDI            8KB      Reserved
9   Hyper-V_VDI           8KB      Reserved
10  FusionAccess_VDI      8KB      Reserved
11  NAS_Default           16KB     Reserved
12  NAS_Virtual_Machine   16KB     Reserved
13  NAS_Database          8KB      Reserved
14  NAS_Large_File        32KB     Reserved
15  Office_Automation     16KB     Reserved
1025  NAS_EDA             16KB     Reserved

```

Query information about the application type whose name is "Oracle_OLTP".

```text
admin:/>show workload_type general name=Oracle_OLTP
ID : 2
Name : Oracle_OLTP
IO Size : 8KB
Type : Reserved

developer:/>show workload_type general name=Oracle_OLTP
ID : 2
Name : Oracle_OLTP
IO Size : 8KB
Type : Reserved

```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                          |
|-----------|----------------------------------|
| ID        | Application type ID.             |
| Name      | Application type name.           |
| IO Size   | Application request size.        |
| Type      | Category of an application type. |
