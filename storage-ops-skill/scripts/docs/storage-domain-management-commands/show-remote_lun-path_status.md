# show remote_lun path_status


##### Function

The **show remote_lun path_status** command is used to query the path that corresponds to the remote LUN in use.

##### Format

**show remote_lun path_status** \[ path_priority=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| path_priority=? | Path status of a remote LUN. | The value can be: <br>"active": available path.<br>"standby": standby path.<br>"unavailable": unavailable path.<br>"registration_failed": path registration reservation failed. |

##### Usage Guidelines

-   When an alarm indicating a registration reservation failure is reported, you can run the "**show remote_lun path_status**" command to view remote LUN path information.
-   You can add optional parameter "path_priority=registration_failed" to view the remote LUN path whose registration reservation failed.

##### Example

Query the path that corresponds to the remote LUN in use.

```text
admin:/>show remote_lun path_status
Path ID Path Type Local Controller Local Port ID Remote IP Remote Device WWN LUN WWN Status Path Priority
------- --------- ---------------- ------------- --------- ----------------- ----------------------------------------------- ------- -------------
0 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:00 Running Active
1 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:01 Running Active
2 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:01 Running Active
3 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:00 Running Active
4 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:02 Running Active
5 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:02 Running Active
```

Query the path that fails to be registered and corresponds to the remote LUN in use.

```text
admin:/>show remote_lun path_status path_priority=registration_failed
Path ID Path Type Local Controller Local Port ID Remote IP Remote Device WWN LUN WWN Status Path Priority
------- --------- ---------------- ------------- --------- ----------------- ----------------------------------------------- ------- -------------
0 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:00 Running Registration failed
1 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:01 Running Registration failed
2 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:01 Running Registration failed
3 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:00 Running Registration failed
4 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:02 Running Registration failed
5 FC Link 0A -- -- -- 60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:02 Running Registration failed
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                          |
|-------------------|----------------------------------|
| Path ID           | Path ID.                         |
| Path Type         | Path type: FC or iSCSI.          |
| Local Controller  | ID of the local controller.      |
| Local Port ID     | ID of the local port.            |
| Remote IP         | IP address of the remote device. |
| LUN WWN           | WWN of the owning LUN.           |
| Status            | Path status.                     |
| Path Priority     | Path priority.                   |
| Remote Device WWN | WWN of the remote device.        |
