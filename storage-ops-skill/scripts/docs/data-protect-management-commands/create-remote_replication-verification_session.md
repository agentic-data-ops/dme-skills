# create remote_replication verification_session


##### Function

The **create remote_replication verification_session** command is used to verify remote replication tasks.

##### Format

**create remote_replication verification_session** remote_replication_id=?

##### Parameters

| Parameter               | Description                      | Value                                                       |
|-------------------------|----------------------------------|-------------------------------------------------------------|
| remote_replication_id=? | ID of a remote replication task. | To obtain the value, run "show remote_replication unified". |

##### Usage Guidelines

If the key attributes of a remote replication task are inconsistent on the local and remote ends, the health status of the remote replication task is faulty and the replication pair state is mirror failed.

##### Example

Verify the data on both the local and remote ends for remote replication task "2100f102030405060000000200000000".

```text
admin:/>create remote_replication verification_session remote_replication_id=2100f102030405060000000200000000
Command executed successfully.
```

##### System Response

None
