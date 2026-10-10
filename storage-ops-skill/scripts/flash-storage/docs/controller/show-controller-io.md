# show controller io


##### Function

**show controller io** command is used to query information about concurrent I/Os of a specified controller.

##### Format

**show controller io** io_type=? controller_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| io_type=? | Type of concurrent I/Os of a controller. | The value can be "frontEnd" or "backEnd", where: <br>"frontEnd": indicates front-end concurrent I/Os.<br>"backEnd": indicates back-end concurrent I/Os. |
| controller_id=? | Controller ID. | The value is in the format of "XA", "XB", "XC" or "XD", where the "X" is an integer ranging from 0 to 3. To obtain the value, run "show controller general". |

##### Usage Guidelines

None

##### Example

-   Query information about front-end concurrent I/Os of controller "0A".

```text
admin:/>show controller io io_type=frontEnd controller_id=0A
Controller Id   : 0A
Front End IO    : 0
Front End Limit : 128
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                   |
|-----------------|-------------------------------------------|
| Controller Id   | Controller ID.                            |
| Front End IO    | Front-end concurrent I/Os.                |
| Front End Limit | Upper limit of front-end concurrent I/Os. |
| Port Type       | Type of the back-end port.                |
| Port Id         | ID of the back-end port.                  |
| Back End IO     | Back-end concurrent I/Os.                 |
| Back End Limit  | Upper limit of back-end concurrent I/Os.  |
