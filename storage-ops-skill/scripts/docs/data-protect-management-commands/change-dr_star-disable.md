# change dr_star disable


##### Function

The **change dr_star disable** command is used to deactivate DR Star.

##### Format

**change dr_star disable** dr_star_id=? \[ is_local_execute=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| dr_star_id | DR Star ID. | To obtain the value, run "show dr_star general". |
| is_local_execute | Whether this command is executed at the local site. | The value can be "yes" or "no", where: <br>"yes": allows local execution.<br>"no": forbids local execution.<br> The default value is "no". |

##### Usage Guidelines

-   This operation will damage the ring relationship of DR Star and its two remote replication members cannot be switched when a fault occurs.
-   Before performing complete deactivation, check whether the replication links between the primary site and the other two sites are normal.
-   Before performing local deactivation, ensure that at least one of the replication links between the local site and the other two sites is disconnected.
-   When the members of DR Star are consistency groups, execute this command to deactivate the DR Star before adding or removing a consistency group member.
-   DR Star cannot be deactivated if its running status is "Invalid".

##### Example

Disable DR Star "200bc79b99520000".

```text
admin:/>change dr_star disable dr_star_id=200bc79b99520000
CAUTION: You are about to disable DR Star. This operation will change the running status of the DR Star to the disable state.
Suggestion: Before performing this operation, check the running status of the DR Star is enable or disable and ensure that the selected DR Star is correct.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
