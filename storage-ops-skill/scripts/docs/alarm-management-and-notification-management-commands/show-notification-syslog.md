# show notification syslog


##### Function

The **show notification syslog** command is used to query the settings of SYSLOG notification.

##### Format

**show notification syslog**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the settings of SYSLOG notification.

```text
admin:/>show notification syslog
Enabled                  : Yes
Alert Level              : Warning
Syslog Server IP         : 192.168.0.126
Enable Alarm             : Yes
Enable Recovery Alarm    : No
Enable Event             : No
Enabled Send System Name : Yes
Syslog Server Port       : 514
Sending Channel          : TLS
Enable Call Home         : Yes
Enable Security Log      : Yes
```

##### System Response

The following table describes the parameter meanings.

| Parameter               | Meaning                                                                                                                |
|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| Enabled                 | Indicates whether the SYSLOG notification function is enabled.                                                         |
| Alert Level             | Indicates the lowest alarm level required by SYSLOG notification to report an alarm.                                   |
| Syslog Server IP        | Indicates the IP address of the SYSLOG server.                                                                         |
| Enable Alarm            | Indicates whether the alarm syslog notification function is enabled. This function is enabled by default.              |
| Enable Recovery Alarm   | Indicates whether the recovery alarm syslog notification function is enabled. This function is disabled by default.    |
| Enable Event            | Indicates whether the event syslog notification function is enabled. This function is disabled by default.             |
| Enable Send System Name | Indicates whether the storage system name is included in syslogs.                                                      |
| Syslog Server Port      | Receiving port number of the syslog server.                                                                            |
| Sending Channel         | syslog sending channel.                                                                                                |
| Enable Call Home        | Indicates whether the call home service syslog notification function is enabled. This function is disabled by default. |
| Enable Security Log     | Indicates whether security log Syslog notification is enabled. This function is disabled by default.                   |
