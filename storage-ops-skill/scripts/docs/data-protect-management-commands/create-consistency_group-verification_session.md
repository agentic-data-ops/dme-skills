# create consistency_group verification_session


##### Function

The **create consistency_group verification_session** command is used to verify consistency groups.

##### Format

**create consistency_group verification_session** consistency_group_id=?

##### Parameters

| Parameter              | Description                | Value                                                      |
|------------------------|----------------------------|------------------------------------------------------------|
| consistency_group_id=? | ID of a consistency group. | To obtain the value, run "show consistency_group general". |

##### Usage Guidelines

After you run this command, the status of a consistency group becomes faulty if the group contains a remote replication task for which the configurations of the local and remote ends are inconsistent.

##### Example

Verify consistency group "1".

```text
admin:/>create consistency_group verification_session consistency_group_id=1
Command executed successfully.
```

##### System Response

None
