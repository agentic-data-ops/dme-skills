# show remote_lun status


##### Function

The **show remote_lun status** command is used to query a remote LUN in use.

##### Format

**show remote_lun status**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query a remote LUN in use.

```text
admin:/>show remote_lun status

LUN WWN Health Status Capacity Device ID Device SN Vendor Model
------------------------------------------------------------------ -------------- ---------- --------- ------------------------ -------- ----------
60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:00 Normal 64.000MB 513 2016BAAB3567DF12 HUAWEI S5600T
60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:01 Normal 64.000MB 513 2016BAAB3567DF12 HUAWEI S5600T
60:02:2a:11:00:bc:43:80:3d:b7:5d:b0:00:00:00:02 Normal 64.000MB 513 2016BAAB3567DF12 HUAWEI S5600T

```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning        |
|---------------|----------------|
| LUN WWN       | LUN WWN.       |
| Health Status | Health status. |
| Capacity      | Capacity.      |
| Device ID     | Device ID.     |
| Device SN     | Device SN.     |
| Vendor        | Vendor.        |
| Model         | Model.         |
