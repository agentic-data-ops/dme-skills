# show service cifs_config


##### Function

The **show service cifs_config** command is used to query the CIFS common configuration.

##### Format

**show service cifs_config**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the CIFS common configuration.

```text
admin:/>show service cifs_config
Communication Thread Number   : 12
Work Thread Number            : 12
Max Block Size(byte)          : 131072
Listen IP                     : permit *
Client List                   : permit *
Communication Thread Priority : normal
Support SMB3 Protocol         : yes
Open Percent(%)               : 50
Slow I/O Percent(%)           : 50
Default UNIX User             : --
Flow Control Switch           : Disabled
Flow Control Percent(%)       : 50
Flow Control Timedelay(ms)    : 200
Antivirus Server IP           : 192.168.1.2,192.168.1.3
```

Query the CIFS common configuration.

```text
admin@vstore1:/>show service cifs_config
Default UNIX User             : --
Antivirus Server IP           : 192.168.1.2,192.168.1.3
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Communication Thread Number | Number of CIFS-based communication threads. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Work Thread Number | Number of CIFS-based working threads. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Max Block Size(byte) | CIFS MTU. |
| Listen IP | Whitelist and blacklist of CIFS listening IP addresses. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Client List | Whitelist and blacklist of CIFS clients. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Communication Thread Priority | Priority of CIFS-based communication threads. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Support SMB3 Protocol | Switch of the SMB3 protocol. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Open_Percent(%) | Percentage of the maximum times that a file can be opened. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Slow I/O Percent(%) | Percentage of slow I/O requests. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Default UNIX User | Default UNIX user of the CIFS user mapping. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Flow Control Switch | Switch of CIFS I/O flow control. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Flow Control Percent(%) | Percentage of the number of CIFS slow I/O requests to the total number of requests in flow control. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Flow Control Timedelay(ms) | Delay threshold of CIFS I/O flow control. NOTE: This field is not supported by the current version. The returned value is invalid. |
| Antivirus Server IP | IP address of the CIFS share antivirus server. The value must be a valid IP address. Use commas (,) to separate multiple IP addresses. |
