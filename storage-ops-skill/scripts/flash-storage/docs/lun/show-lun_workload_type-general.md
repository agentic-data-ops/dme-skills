# show lun_workload_type general


##### Function

The **show lun_workload_type general** command is used to query information about application types in the storage system.

##### Format

**show lun_workload_type general** \[ id=? \| name=? \]

##### Parameters

| Parameter | Description            | Value                                                                                                                                                                                                        |
|-----------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id=?      | Application type ID.   | To obtain the value, run "**show lun_workload_type general**" without parameters. |
| name=?    | Application type name. | To obtain the value, run "**show lun_workload_type general**" without parameters. |

##### Usage Guidelines

-   Run the "**show lun_workload_type general**" command to query information about all application types of the storage system.
-   Run the "**show lun_workload_type general** id=?" command to query information about a specified application type by ID.
-   Run the "**show lun_workload_type general** name=?" command to query information about a specified application type by name.

##### Example

Query information about existing application types of the storage system.

```text

admin:/>show lun_workload_type general
ID  Name                  IO Size  Compression Enabled  Dedup Enabled  Type
--  --------------------  -------  -------------------  -------------  --------
0   Default               8KB      --                   --             Reserved
1   Oracle_OLAP           32KB     --                   --             Reserved
2   Oracle_OLTP           8KB      --                   --             Reserved
3   Oracle_OLAP&OLTP      8KB      --                   --             Reserved
4   SQL_Server_OLAP       32KB     --                   --             Reserved
5   SQL_Server_OLTP       8KB      --                   --             Reserved
6   SQL_Server_OLAP&OLTP  8KB      --                   --             Reserved
7   SAP_HANA              8KB      --                   --             Reserved
8   Vmware_VDI            8KB      --                   --             Reserved
9   Hyper-V_VDI           8KB      --                   --             Reserved
10  FusionAccess_VDI      8KB      --                   --             Reserved

developer:/>show lun_workload_type general
ID  Name                  IO Size  Compression Enabled  Dedup Enabled  Type
--  --------------------  -------  -------------------  -------------  --------
0   Default               8KB      --                   --             Reserved
1   Oracle_OLAP           32KB     --                   --             Reserved
2   Oracle_OLTP           8KB      --                   --             Reserved
3   Oracle_OLAP&OLTP      8KB      --                   --             Reserved
4   SQL_Server_OLAP       32KB     --                   --             Reserved
5   SQL_Server_OLTP       8KB      --                   --             Reserved
6   SQL_Server_OLAP&OLTP  8KB      --                   --             Reserved
7   SAP_HANA              8KB      --                   --             Reserved
8   Vmware_VDI            8KB      --                   --             Reserved
9   Hyper-V_VDI           8KB      --                   --             Reserved
10  FusionAccess_VDI      8KB      --                   --             Reserved

```

Query information about the application type whose name is "Oracle_OLTP".

```text

admin:/>show lun_workload_type general name=Oracle_OLTP

ID                  : 2
Name                : Oracle_OLTP
IO Size             : 8KB
Compression Enabled : --
Dedup Enabled       : --
Type                : Reserved
developer:/>show lun_workload_type general name=Oracle_OLTP
ID                  : 2
Name                : Oracle_OLTP
IO Size             : 8KB
Compression Enabled : --
Dedup Enabled       : --
Type                : Reserved

```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| ID | Application type ID. |
| Name | Application type name. |
| IO Size | Request size of the application type. |
| Compression Enabled | Whether the compression function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Dedup Enabled | Whether the deduplication function is enabled. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Type | Category of application types. |
