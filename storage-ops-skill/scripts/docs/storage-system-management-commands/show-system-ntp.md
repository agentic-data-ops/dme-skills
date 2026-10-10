# show system ntp


##### Function

The **show system ntp** command is used to query the Network Time Protocol (NTP) settings.

##### Format

**show system ntp**

##### Parameters

None

##### Usage Guidelines

This command is invisible to adapt to the NTP authentication feature.

##### Example

Query the NTP settings, run the following command. The command output varies depending on cli interface.

```text
admin:/>show system ntp

NTP Switch             : Enable
Server IP Address      : 192.168.5.3
Synch Schedule         : 0 day(s),12 hour(s),0 minute(s),0 second(s)
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                                                 |
|-------------------|---------------------------------------------------------|
| NTP Switch        | NTP synchronization switch(Default value:"disable").    |
| Server IP Address | NTP server address.                                     |
| Synch Schedule    | NTP synchronization period(Default value:"60 seconds"). |
