# show ntp status


##### Function

The **show ntp status** command is used to query the NTP status.

##### Format

**show ntp status**

##### Parameters

None

##### Usage Guidelines

If the NTP configuration is modified, query the NTP status one minute later.

##### Example

Query NTP status.

```text
admin:/>show ntp status
NTP Server Address           : test.com,test1.com
Current Connected NTP Server : test.com(ip:192.168.1.66)
Offset                       : +35685.45077 second(s)
Status                       : Normal
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| NTP Server Address | NTP server address. |
| Current Connected NTP Server | Current connected NTP server. |
| Offset | Time difference between the disk array and the current connected NTP server. If "+xxx.xxx second (s)" is displayed, it indicates that the time of the disk array is xxx.xxx second (s) slower than that of the NTP server. If "-xxx.xxx second (s)" is displayed, it indicates that the time of the disk array is xxx.xxx second (s) faster than that of the NTP server. |
| Status | NTP status. |
