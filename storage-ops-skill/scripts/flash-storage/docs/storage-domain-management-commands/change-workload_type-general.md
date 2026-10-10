# change workload_type general


##### Function

The **change workload_type general** command is used to modify parameters of an application type, including "name", "io_size", and so on.

##### Format

**change workload_type general** id=? { name=? \| io_size=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| id=? | Application type ID. | You can press Ctrl+A or run the show workload_type general command without parameters to obtain the value. The value ranges from 16 to 1024. |
| name=? | Application type name. | The value contains 1 to 31 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| io_size=? | Application request size. | The value can be "4KB", "8KB", "16KB", "32KB", "64KB", or "64KB". |
| template_type | Template type. | "LUN": logical volume.<br>"File System": file system. |

##### Usage Guidelines

-   Before performing this operation, ensure that the selected application type is exactly the one you want to modify.
-   Before performing this operation (excluding changing names), ensure that no LUN or file system uses the application type.

##### Example

Change "io_size" of the application type whose ID is "16" to "16KB".

```text
admin:/>change workload_type general id=16 io_size=16KB
Command executed successfully.
```

##### System Response

None
