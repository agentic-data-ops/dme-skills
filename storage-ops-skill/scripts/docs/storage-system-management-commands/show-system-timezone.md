# show system timezone


##### Function

The **show system timezone** command is used to query the time zone where the storage system resides.

##### Format

**show system timezone**

##### Parameters

None

##### Usage Guidelines

None

##### Example

To query the time zone where the storage system resides in, run the following command. The command output varies depending on cli interface.

```text
admin:/>show system timezone

Time  Zone       :  +08:00
Time  Zone  Name   :  Asia/Shanghai
Style          :  Long Name Style
DST Enable       :  Disable
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                          |
|----------------|--------------------------------------------------|
| Time Zone      | Time zone.                                       |
| Time Zone Name | Time zone name.                                  |
| Style          | Time zone name display style.                    |
| DST Enable     | Whether the time zone uses daylight saving time. |
