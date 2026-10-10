# show event_restore


##### Function

The **show event_restore** is used to query the configuration policies for dumping event.

##### Format

**show event_restore**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the configuration policies for dumping event.

```text
admin:/>show event_restore
Enable  IP             FTP/SFTP Path  User Name  Protocol
------  -------------  -------------  ---------  --------
Yes     192.168.22.40  /              admin      SFTP
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Enable        | Switch of the policies for dumping event.                                                                                             |
| IP            | IP address of the FTP server or SFTP server for dumping events.                                                                       |
| FTP/SFTP Path | Path of a File Transfer Protocol (FTP) server or a Secure File Transfer Protocol (SFTP) server to which system events will be dumped. |
| User Name     | Username of an FTP server or SFTP server.                                                                                             |
| Protocol      | Transfer protocol type.                                                                                                               |
