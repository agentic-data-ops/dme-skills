# show iscsi target


##### Function

The **show iscsi target** command is used to query information about the target connected to iSCSI links.

##### Format

**show iscsi target** \[ iscsi_id=? \]

##### Parameters

| Parameter  | Description          | Value                                                                                                                                                                                 |
|------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| iscsi_id=? | ID of an iSCSI link. | To obtain the value, run "**show iscsi target**" without parameters. |

##### Usage Guidelines

-   To query information on all iSCSI targets, run **show iscsi target**.
-   To query information on a specific iSCSI target, run **show iscsi target** iscsi_id=?.

##### Example

Query information about the target connected to iSCSI links.

```text

developer:/>show iscsi target

ID  Name                                                                  Status   Local Control ID  Remote IP    Port  Recovery Policy  CHAP Enabled  Application Type  LogicalPortName
--  --------------------------------------------------------------------  -------  ----------------  -----------  ----  ---------------  ------------  ----------------  ---------------
0   iqn.2006-08.com.huawei:oceanstor:21004846fb8b90df::22004:10.10.10.21  Link Up  0A                10.10.10.21  3260  Automatic        No            Heterogeneity     CTE0.B.IOM1.P0.V4

```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                                                        |
|------------------|----------------------------------------------------------------|
| ID               | ID of the target.                                              |
| Name             | Name of the target.                                            |
| Status           | Connection status of the target.                               |
| Local Control ID | ID of the local controller connected to the target.            |
| Local Port ID    | Local port ID.                                                 |
| Remote IP        | IP address of the remote target.                               |
| Port             | TCP port ID of the target.                                     |
| Recovery Policy  | Recovery policy of the target.                                 |
| CHAP Enabled     | Whether CHAP authentication is enabled.                        |
| Application Type | Application type of this target: replication or heterogeneity. |
| LogicalPortName  | Logical port name.                                             |
