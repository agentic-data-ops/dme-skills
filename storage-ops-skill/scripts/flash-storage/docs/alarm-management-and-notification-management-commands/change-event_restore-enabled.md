# change event_restore enabled


##### Function

The **change event_restore enabled** command is used to enable or disable the policies for dumping events.

##### Format

**change event_restore enabled** enabled=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| enabled=? | Switch of the policies for dumping events. | The value can be "yes" or "no", where: <br>"yes": enables the event dumping function.<br>"no": disables the event dumping function. |

##### Usage Guidelines

None

##### Example

Enable the system event dumping function.

```text
admin:/>change event_restore enabled enabled=yes
Command executed successfully.
```

Query the result.

```text
admin:/>show event_restore
Enable  IP      FTP/SFTP Path  User Name  Protocol
------  -----------  -------------  ---------  --------
Yes   192.168.1.2  /         admin    FTP
```

##### System Response

None
