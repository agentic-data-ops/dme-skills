# swap dr_star


##### Function

The **swap dr_star** command is used to switch DR Star.

##### Format

**swap dr_star** dr_star_id=?

##### Parameters

| Parameter  | Description | Value                                            |
|------------|-------------|--------------------------------------------------|
| dr_star_id | DR Star ID. | To obtain the value, run "show dr_star general". |

##### Usage Guidelines

-   This operation switches the states of DR Star's two asynchronous remote replication members. After the operation, the asynchronous replication not in the "Standby" state is changed to the "Standby" state.
-   Before performing a switchover, ensure that there is an asynchronous remote replication member in the "Standby" state and the two remote replication members at a site have the same primary and secondary attributes.
-   DR Star cannot be switched if its running status is "Invalid" or "Disable".

##### Example

Switch DR Star "200bc79b99520000".

```text
admin:/>swap dr_star dr_star_id=200bc79b99520000
Command executed successfully.
```

##### System Response

None
