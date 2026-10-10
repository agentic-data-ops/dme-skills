# show performance cifs_service


##### Function

The **show performance cifs_service** command is used to query performance statistics of a CIFS service. Running this command analyzes performance statistics of a CIFS service in real time.

##### Format

**show performance cifs_service**

##### Parameters

None

##### Usage Guidelines

-   You will be prompted with optional performance statistics categories upon running this command. In this condition, typing a number or multiple numbers (separated by commas (,)) for the selected categories and pressing "Enter" displays the performance statistics for those categories.
-   Performance statistics will be updated in real time.
-   Typing "q" on the command line interface (CLI) exits the active performance statistics display.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query performance statistics of a CIFS service.

```text
admin:/>show performance cifs_service
0.The cumulative count of file I/O operations for the object,including metadata I/O operations
1.The cumulative count of bytes transferred for all of the file I/O operations as defined in the "TotalIOs" property
Input item(s) number separated by comma:0
The cumulative count of file I/O operations for the oject,including metadata I/O operations : 0
```

##### System Response

The following table describes the parameter meanings.

| Parameter                                                                                                          | Meaning                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| The cumulative count of file I/O operations for the object,including metadata I/O operations                       | Cumulative count of file I/O operations for the object, including metadata I/O operations.                      |
| The cumulative count of bytes transferred for all of the file I/O operations as defined in the "TotalIOs" property | Cumulative count of bytes transferred for all of the file I/O operations as defined in the "TotalIOs" property. |
