# delete workload_type general


##### Function

The **delete workload_type general** command is used to delete an application type.

##### Format

**delete workload_type general** id_list=?

##### Parameters

| Parameter | Description               | Value                                                                                                                                                            |
|-----------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_list=? | Application type ID list. | To obtain the value, run "show workload_type general". Multiple IDs are separated by commas (,) or by hyphens (-) to represent an ID range, such as: "16,17-19". |

##### Usage Guidelines

-   Running this command will delete information about the application type from the storage system.
-   Before running this command, ensure that the selected application type is exactly the one you want to delete and no LUN or file system uses it.
-   An application type cannot be deleted when any one of the following conditions is met:
-   The application type is reserved in the system.
-   The application type has been used for LUNs or file systems.

##### Example

Delete application types whose IDs are "16" and "17".

```text
admin:/>delete workload_type general id_list=16,17
Delete workload type 16 successfully.
Delete workload type 17 successfully.
```

##### System Response

None
