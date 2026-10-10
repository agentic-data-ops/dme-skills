# delete lun_workload_type general


##### Function

The **delete lun_workload_type general** command is used to delete an application type.

##### Format

**delete lun_workload_type general** id_list=?

##### Parameters

| Parameter | Description                                               | Value                                                                                                                                                                    |
|-----------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id_list=? | ID list of the application types that need to be deleted. | To obtain the value, run "show lun_workload_type general". Multiple IDs are separated by commas (,), or an ID range is represented by a hyphen (-), such as: "16,17-19". |

##### Usage Guidelines

-   Running this command deletes information about the application type from the storage system.
-   Before running this command, ensure that the selected application type is exactly the one you want to delete and no LUN uses it.
-   An application type cannot be deleted when any one of the following conditions is met:
-   The application type is reserved by the system.
-   The applicatoin type has been used for LUNs.

##### Example

Delete application types whose IDs are "16" and "17".

```text
admin:/>delete lun_workload_type general id_list=16,17
Delete LUN workload type 16 successfully.
Delete LUN workload type 17 successfully.
```

##### System Response

None
