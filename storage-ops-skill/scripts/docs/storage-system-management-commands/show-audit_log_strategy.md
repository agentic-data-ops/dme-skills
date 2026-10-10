# show audit_log_strategy


##### Function

The **show audit_log_strategy** command is used to query audit log strategy.

##### Format

**show audit_log_strategy** \[ { vstore_id=? \| vstore_name=? } \]

**show audit_log_strategy**

##### Parameters

| Parameter     | Description  | Value                                                                                                                     |
|---------------|--------------|---------------------------------------------------------------------------------------------------------------------------|
| vstore_id=?   | vStore ID.   | To obtain the value, run the "show vstore" command.                                                                       |
| vstore_name=? | vStore name. | The value is a string of 1 to 256 characters. You can run the show vstore command without parameters to obtain the value. |

##### Usage Guidelines

Run the "**show audit_log_strategy**" command to query the audit log strategy.

##### Example

Query the audit log strategy of the vStore whose ID "1".

```text
admin:/>show audit_log_strategy vstore_id=1

Audit Enabled             : On
CIFS Login Logout         : On
File Access               : On
Audit Policy Change       : Off
Guarantee Mode            : Not-guarantee Mode
Single Logfile Size(MB)   : 50
Reserve Logfile Number(K) : 100
Occupied Capacity(GB)     : 0
File System ID            : 1
File System Name          : FileSystem001
Vstore Id                 : 1
Vstore Nmae               : vs1
```

Query the audit log strategy of a vStore.

```text
admin@vs1:/>show audit_log_strategy

Audit Enabled             : On
CIFS Login Logout         : On
File Access               : On
Audit Policy Change       : Off
Guarantee Mode            : Not-guarantee Mode
Single Logfile Size(MB)   : 50
Reserve Logfile Number(K) : 100
Occupied Capacity(GB)     : 0
File System ID            : 1
File System Name          : FileSystem001
Vstore Id                 : 1
Vstore Nmae               : vs1
```

##### System Response

The following table describes the parameter meanings.

| Parameter                 | Meaning                                               |
|---------------------------|-------------------------------------------------------|
| Audit Enabled             | Switch of starting and stopping audit log collection. |
| File System ID            | Audit log file system ID.                             |
| File System Name          | Audit log file system name.                           |
| Single Logfile Size(MB)   | Size of a single audit log.                           |
| Reserve Logfile Number(K) | Number of reserved audit logs.                        |
| Occupied Capacity(GB)     | Occupied capacity of the audit log file system.       |
| CIFS Login Logout         | Whether to log CIFS login and logout events.          |
| Guarantee Mode            | Whether to enable audit log guarantee mode.           |
| File Access               | Whether to log file access events.                    |
| Audit Policy Change       | Whether to log the changes to the audit policy.       |
| Vstore Id                 | vStore ID.                                            |
| Vstore name               | vStore name.                                          |
