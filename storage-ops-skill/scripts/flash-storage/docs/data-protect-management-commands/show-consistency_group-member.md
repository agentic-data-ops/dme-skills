# show consistency_group member


##### Function

The **show consistency_group member** command is used to query details on members of a consistency group task.

##### Format

**show consistency_group member** consistency_group_id=?

##### Parameters

| Parameter              | Description                | Value                                                      |
|------------------------|----------------------------|------------------------------------------------------------|
| consistency_group_id=? | ID of a consistency group. | To obtain the value, run "show consistency_group general". |

##### Usage Guidelines

None.

##### Example

To query details on the members of consistency group "2100ef02030405060000000300000000", run the following command.

```text

admin:/>show consistency_group member consistency_group_id=2100ef02030405060000000300000000

ID                                Health Status  Running Status  Is Primary  Replication Mode  Compress Enable  Compress Valid
--------------------------------  -------------  --------------  ----------  ----------------  ---------------  --------------
2100ef02030405060000000200000001  Normal         Normal          Yes         Asynchronous      No               No
2100ef02030405060000000200000002  Normal         Normal          Yes         Asynchronous      No               No

```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                                   |
|------------------|-------------------------------------------|
| ID               | Remote replication ID.                    |
| Health Status    | Health status.                            |
| Running Status   | Running status.                           |
| Is Primary       | Is primary end of the remote replication. |
| Replication Mode | Remote replication mode.                  |
| Compress Enable  | Is compression enabled.                   |
| Compress Valid   | Is compression valid.                     |
