# show ntp_server general


##### Function

The **show ntp_server general** command is used to query the time synchronization function settings.

##### Format

**show ntp_server general**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

Query the time synchronization function settings.

```text

admin:/>show ntp_server general
NTP Switch         : Enable
Server Address       : 192.168.5.3
Synch Schedule       : 0 day(s),12 hour(s),0 minute(s),0 second(s)
NTP Auth Switch      : Enable

```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                                   |
|-----------------|-----------------------------------------------------------|
| NTP Switch      | NTP synchronization switch (Default value: "disable").    |
| Server Address  | NTP server address.                                       |
| Synch Schedule  | NTP synchronization period (Default value: "60 seconds"). |
| NTP Auth Switch | NTP authentication switch (Default value: "disable").     |
