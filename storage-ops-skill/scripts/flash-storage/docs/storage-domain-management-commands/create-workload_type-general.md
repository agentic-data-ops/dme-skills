# create workload_type general


##### Function

The **create workload_type general** command is used to create an application type for LUNs or for file systems.

##### Format

**create workload_type general** name=? io_size=? \[ dedup_enabled=? \] \[ compression_enabled=? \] \[ template_type=? \[ fs_layer_distribution_algorithm=? \] \] \[ id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Application type name. | The value contains 1 to 31 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| io_size=? | Application request type. | The value can be "4KB", "8KB", "16KB", "32KB", "64KB", or "64KB". |
| id | Application type ID. | The value ranges from 16 to 1024. |
| fs_layer_distribution_algorithm | Data distribution algorithm of the file system. | "Performance Mode": performance mode. Directories and files are allocated to the access controller preferentially, to improve access performance of directories and files.<br>"Capacity Balance Mode": capacity balancing mode. Directories and files are evenly allocated to each controller by capacity.<br>"Directory Balance Mode": directory balancing mode. Directories are evenly allocated to each controller by quantity.<br>"Directory Shuffle Mode": directory polling mode. Directories are allocated to each controller based on the creation sequence. |
| template_type | Template type. | "LUN": logical volume.<br>"File System": file system. |

##### Usage Guidelines

Manually specify the parameters for an application type to be created. After the application type is created, it can be selected for created LUNs or file systems, achieving more reasonable space parameters of LUNs or file systems.

##### Example

Create an application type and set the parameters as follows:

-   Name: oracle_OLTP
-   Application request size: 8 KB.

```text
admin:/>create workload_type general name=oracle_OLTP io_size=8KB
Command executed successfully.
```

##### System Response

None
