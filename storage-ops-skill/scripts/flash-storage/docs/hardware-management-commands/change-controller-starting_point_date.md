# change controller starting_point_date


##### Function

The **change controller starting_point_date** command is used to change the service start time of a controller.

##### Format

**change controller starting_point_date** controller_id=? date=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller_id=? | Controller ID. | To obtain the value, run "show controller general". |
| date | Service start time. | UTC time format: YYYY-MM-DD. <br>YYYY: The start year is converted from 1970.<br>MM: start month.<br>DD: start date. |

##### Usage Guidelines

The format of the service start time (UTC) of an electronic insurance policy is as follows:

YYYY-MM-DD

-   YYYY: The start year is converted from 1970.
-   MM: start month.
-   DD: start date.

##### Example

Change the service start time of the controller electronic insurance policy.

```text
admin:/>change controller starting_point_date controller_id=0A date=2020-12-12
CAUTION: You are about to modify the service start time of the controller. This operation may result in extra alarms or error messages.
Suggestion: To prevent extra alarms or errors, ensure that the entered information is consistent with the contract information and that the entered parameters are valid.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
