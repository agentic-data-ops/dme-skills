# show fan


##### Function

The **show fan** command is used to query details on fan modules. Run this command if you need to query a fan module's status, running speed, running level, and electronic label.

##### Format

**show fan** \[ fan_id=? \]

##### Parameters

| Parameter | Description         | Value                                                                                                                                                            |
|-----------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fan_id=?  | ID of a fan module. | To obtain the value, run "**show fan**" without parameters. |

##### Usage Guidelines

-   To query details on all fan modules, run "**show fan**".
-   To query details on a specific fan module, run "**show fan** fan_id=?".

##### Example

Query details on all fan modules, run the following command. The command output varies depending on a specific product.

```text
admin:/>show fan
ID           Name   Health Status  Running Status  Running Level
-----------  -----  -------------  --------------  -------------
CTE0.A.FAN0  FAN 0  Normal         Running         Low
CTE0.A.FAN1  FAN 1  Normal         Running         Low
CTE0.A.FAN2  FAN 2  Normal         Running         Low
CTE0.B.FAN0  FAN 0  Normal         Running         Low
CTE0.B.FAN1  FAN 1  Normal         Running         Low
CTE0.B.FAN2  FAN 2  Normal         Running         Low
DAE000.PSU0  PSU 0  Normal         Running         Low
DAE000.PSU1  PSU 1  Normal         Running         Low
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                             |
|------------------|-------------------------------------|
| ID               | Fan module ID.                      |
| Name             | Fan module name.                    |
| Health Status    | Health status of the fan module.    |
| Running Status   | Running status of the fan module.   |
| Running Level    | Running level of the fan module.    |
| Electronic Label | Electronic label of the fan module. |
