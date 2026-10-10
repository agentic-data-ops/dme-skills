# show clone_consistency_group clone


##### Function

The **show clone_consistency_group clone** command is used to query information about members in a clone consistency group.

##### Format

**show clone_consistency_group clone** { clone_consistency_group_id=? \| clone_consistency_group_name=? }

##### Parameters

| Parameter                      | Description                   | Value                                                                             |
|--------------------------------|-------------------------------|-----------------------------------------------------------------------------------|
| clone_consistency_group_id=?   | Clone consistency group ID.   | You can run the show clone_consistency_group general command to obtain the value. |
| clone_consistency_group_name=? | Clone consistency group name. | You can run the show clone_consistency_group general command to obtain the value. |

##### Usage Guidelines

None

##### Example

Query information about members in the clone consistency group whose ID is "1".

```text
admin:/>show clone_consistency_group clone clone_consistency_group_id=0

ID  Name                       Source ID  Source Type  Target ID  Health Status  Running Status  Copy Speed  Clone Consistency Group ID  Sync Start Time                Sync End Time
--  -------------------------  ---------  -----------  ---------  -------------  --------------  ----------  --------------------------  -----------------------------  -------------
5   lun0000_20070507455900005  0          LUN          5          Normal         Sync Paused     Middle      0                           2020-07-05/15:45:59 UTC+08:00  --
6   lun0001_20070507455900006  1          LUN          6          Normal         Sync Paused     Middle      0                           2020-07-05/15:45:59 UTC+08:00  --
7   lun0002_20070507455900007  2          LUN          7          Normal         Sync Paused     Middle      0                           2020-07-05/15:45:59 UTC+08:00  --
8   lun0003_20070507455900008  3          LUN          8          Normal         Sync Paused     Middle      0                           2020-07-05/15:45:59 UTC+08:00  --
9   lun0004_20070507455900009  4          LUN          9          Normal         Sync Paused     Middle      0                           2020-07-05/15:45:59 UTC+08:00  --
```

##### System Response

The following table describes the parameter meanings.

| Parameter                  | Meaning                                                           |
|----------------------------|-------------------------------------------------------------------|
| ID                         | Clone pair ID.                                                    |
| Name                       | Clone pair name.                                                  |
| Source ID                  | ID of a clone pair source object, including a LUN and a snapshot. |
| Source Type                | Source object type.                                               |
| Target ID                  | ID of a clone pair target object (only a is LUN supported).       |
| Health Status              | Health status of a clone pair.                                    |
| Running Status             | Running status of a clone pair.                                   |
| Copy Speed                 | Copy speed.                                                       |
| Clone Consistency Group ID | Clone consistency group ID.                                       |
| Sync Start Time            | Synchronization start time.                                       |
| Sync End Time              | Synchronization end time.                                         |
