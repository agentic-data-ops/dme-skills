# show system dst


##### Function

The **show system dst** command is used to query the daylight saving time (DST) settings of the storage system.

##### Format

**show system dst** continent=? capital=?

##### Parameters

| Parameter   | Description                                                                      | Value                                                                                                                                            |
|-------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| continent=? | General area (continent or region) where the storage system resides.             | The value can be "Africa", "America", "Antarctica", "Arctic", "Asia", "Atlantic", "Australia", "Etc", "Europe", "Indian", "Pacific", or "other". |
| capital=?   | Specific area (major city, province, or state) where the storage system resides. | The value varies depending on the continent=? parameter. Refer to the information displayed in the CLI.                                          |

##### Usage Guidelines

The storage system automatically sets the DST based on the configured time zone. The DST is not applicable to some time zones.

##### Example

To query the DST settings of the storage system, run the following command. The command output varies depending on cli interface.

```text
admin:/>show system dst continent=Europe capital=London

Time Zone       : Europe/London
Begin Time      : 03-26 01:00:00
End Time       : 10-29 02:00:00
Adjust Time(Minutes) : 60
Config Mode      : Date
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                                             |
|----------------------|-----------------------------------------------------|
| Time Zone            | Time zone name.                                     |
| Begin Time           | Start time of daylight saving time.                 |
| End Time             | End time of daylight saving time.                   |
| Adjust Time(Minutes) | During the time of daylight saving time adjustment. |
| Config Mode          | Configuration method of daylight saving time.       |
