# show assistant_cooling_unit


##### Function

The **show assistant_cooling_unit** command is used to query details on assistant cooling units.

##### Format

**show assistant_cooling_unit** \[ id=? \]

##### Parameters

| Parameter | Description                       | Value                                                                                                                                                                                                  |
|-----------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id=?      | ID of the assistant cooling unit. | To obtain the value, run "**show assistant_cooling_unit**" without parameters. |

##### Usage Guidelines

-   To query details on all assistant cooling units, run "**show assistant_cooling_unit**".
-   To query details on a specific assistant cooling units, run "**show assistant_cooling_unit** id=?".

OceanStor Dorado 18000 V6 storage systems supports this command.

##### Example

Query details on all assistant cooling units. The command output varies depending on a specific product.

```text
admin:/>show assistant_cooling_unit
ID Health Status Running Status
------- ------------- -------------- --------------------------------
CTE0.C Normal Online
CTE0.D Normal Online
```

Query details on the assistant cooling unit whose ID is "CTE0.C". The ID and output vary depending on a specific product.

```text
admin:/>show assistant_cooling_unit id=CTE0.C
ID : CTE0.C
Health Status : Normal
Running Status : Online
PCB Version : VER.B
Electronic Label : fan_ctrl_elabel
```

##### System Response

The following table describes the parameter meanings.

| Parameter        | Meaning                                    |
|------------------|--------------------------------------------|
| ID               | Fan control board ID.                      |
| Health Status    | Health status of the fan control board.    |
| Running Status   | Running status of the fan control board.   |
| PCB Version      | PCB version of the fan control board.      |
| Electronic Label | Electronic label of the fan control board. |
