# change dr_star enable


##### Function

The **change dr_star enable** command is used to activate DR Star.

##### Format

**change dr_star enable** dr_star_id=?

##### Parameters

| Parameter  | Description | Value                                            |
|------------|-------------|--------------------------------------------------|
| dr_star_id | DR Star ID. | To obtain the value, run "show dr_star general". |

##### Usage Guidelines

-   This command is used to check whether DR Star members can form a ring. The ring relationship is a basic element of the DR Star solution.
-   Before performing activation, check whether the replication links between the primary site and the other two sites are normal.
-   DR Star cannot be activated if its running status is "Invalid".

##### Example

Activate DR Star "200bc79b99520000".

```text
admin:/>change dr_star enable dr_star_id=200bc79b99520000
Command executed successfully.
```

##### System Response

None
