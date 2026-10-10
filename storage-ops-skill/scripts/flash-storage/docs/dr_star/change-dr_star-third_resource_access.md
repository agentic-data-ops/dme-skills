# change dr_star third_resource_access


##### Function

The **change dr_star third_resource_access** command is used to change the read and write permissions of secondary LUNs in remote replication at the DR Star third site.

##### Format

**change dr_star third_resource_access** dr_star_id=? third_resource_access=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| dr_star_id | DR Star ID. | To obtain the value, run "show dr_star general". |
| third_resource_access | Read and write permissions of secondary LUNs. | The value can be "read_only" or "read_write", where: <br>"read_only": readable only.<br>"read_write": readable and writable. |

##### Usage Guidelines

-   This operation needs to be performed at the site that has two asynchronous remote replication links.
-   Before you perform this operation, if the remote replication not in the "Standby" state has normal links, ensure that it is in the "Split" state; if it has faulty links, ensure that it is in the disconnected or "Split" state.
-   Before performing this operation, ensure that you have entered the correct DR Star ID.

##### Example

Change the read and write permissions of secondary LUNs in the third-site remote replication of DR Star whose ID is "200bc79b99520000" to readable and writable.

```text
admin:/>change dr_star third_resource_access dr_star_id=1a212d4a5e6b0000 third_resource_access=read_write
CAUTION: You are about to modify the read and write permissions on the common secondary LUN of asynchronous remote replication at the third site of DR Star.This operation will change the read and write permissions on the common secondary LUN of asynchronous remote replication at the third site of the DR Star.
Suggestion: Before performing this operation, check the read and write permissions on the common secondary LUN of asynchronous remote replication at the third site of the DR Star and ensure that the selected DR Star is correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
