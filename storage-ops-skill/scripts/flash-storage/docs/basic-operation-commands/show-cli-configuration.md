# show cli configuration


##### Function

The **show cli configuration** command is used to query command line interface (CLI) settings.

##### Format

**show cli configuration**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

Query CLI settings.

```text
admin:/>show cli configuration

More enabled(display page by page) : Yes
Silent enabled                     : No
Capacity Mode                      : Automatic
Timeout                            : 100 min
Monitor Style                      : Steady
Separator                          : None
```

##### System Response

The following table describes the parameter meanings.

| Parameter                          | Meaning                                               |
|------------------------------------|-------------------------------------------------------|
| More enabled(display page by page) | Whether to enable the more function.                  |
| Silent enabled                     | Whether to display the high-risk prompt of a command. |
| Capacity Mode                      | Capacity display mode.                                |
| Timeout                            | Timeout period for the CLI.                           |
| Monitor Style                      | Performance statistics display mode.                  |
