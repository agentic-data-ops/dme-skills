# show consistency_group available_remote_replication


##### Function

The **show consistency_group available_remote_replication** command is used to query for the remote replication tasks that can be added to a consistency group.

##### Format

**show consistency_group available_remote_replication** consistency_group_id=?

##### Parameters

| Parameter              | Description                | Value                                                      |
|------------------------|----------------------------|------------------------------------------------------------|
| consistency_group_id=? | ID of a consistency group. | To obtain the value, run "show consistency_group general". |

##### Usage Guidelines

None.

##### Example

To query for the remote replication tasks that can be added to consistency group "21001502030405060000000300000000", run the following command.

```text

admin:/>show consistency_group available_remote_replication consistency_group_id=21001502030405060000000300000000

ID                                Health Status  Running Status  Is Primary  Replication Mode  Compress Enable  Compress Valid
--------------------------------  -------------  --------------  ----------  ----------------  ---------------  --------------
21001502030405060000000200000002  Normal         Splitted        Yes         Asynchronous      No               No
21001502030405060000000200000003  Normal         Splitted        Yes         Asynchronous      No               No

```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                               |
|------------------|---------------------------------------|
| ID               | Remote replication ID.                |
| Health Status    | Health status.                        |
| Running Status   | Running status.                       |
| Is Primary       | Is primary of the remote replication. |
| Replication Mode | Remote replication mode.              |
| Compress Enable  | Is compression enabled.               |
| Compress Valid   | Is compression valid.                 |
