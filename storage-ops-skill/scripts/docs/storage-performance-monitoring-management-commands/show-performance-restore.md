# show performance restore


##### Function

The **show performance restore** command is used to query the configuration policies for dumping performance statistics.

##### Format

**show performance restore**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the configuration policies for dumping performance statistics on the storage system.

```text
admin:/>show performance restore
Enabled  : Yes
IP       : 192.168.8.211
Path     : /path
User     : admin
Protocol : FTP
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                                              |
|-----------|------------------------------------------------------|
| Enabled   | Status of the performance statistics dumping switch. |
| IP        | IP address of the server.                            |
| Path      | Server storage path.                                 |
| User      | Server user name.                                    |
| Protocol  | Server protocol.                                     |
