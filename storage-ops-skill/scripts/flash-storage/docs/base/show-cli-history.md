# show cli history


##### Function

The **show cli history** command is used to query the history of executed commands.

##### Format

**show cli history** \[ N=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| N=? | Number of most recently executed commands that you want to query. | The value ranges from 1 to 1024. NOTE: Given the storage system can record a maximum of 1024 executed commands, a value that is equal to 1024 could display all of the memorized commands. |

##### Usage Guidelines

This command is only used to query the history of executed commands on the current controller.

-   Run the "**show cli history**" command to query all commands recorded by the storage system.
-   Run the "**show cli history** N=?" command to query the N (a numeral) commands that you have executed in most recent.

##### Example

Query all executed commands that have been recorded.

```text
admin:/>show cli history
[2017-07-20 10:00:38] [admin] [192.168.8.211 2335] [show cli history ] [succeeded]
[2017-07-20 10:01:47] [admin] [192.168.8.211 2335] [show cli configuration ] [succeeded]
[2017-07-20 10:02:04] [admin] [192.168.8.211 2335] [show event ] [succeeded]
[2017-07-20 10:02:29] [admin] [192.168.8.211 2335] [show event number=10 ] [succeeded]
[2017-07-20 10:02:36] [admin] [192.168.8.211 2335] [show cli configuration ] [succeeded]
[2017-07-20 10:02:47] [admin] [192.168.8.211 2335] [change cli timeout=60 ] [failed]
[2017-07-20 10:03:01] [admin] [192.168.8.211 2335] [show safe_strategy ] [succeeded]
[2017-07-20 10:03:23] [admin] [192.168.8.211 2335] [change safe_strategy session_expired_time=60 ] [succeeded]
[2017-07-20 10:03:25] [admin] [192.168.8.211 2335] [show safe_strategy ] [succeeded]
[2017-07-20 10:03:36] [admin] [192.168.8.211 2335] [change cli timeout=60 ] [succeeded]
[2017-07-20 10:03:41] [admin] [192.168.8.211 2335] [show cli configuration ] [succeeded]
[2017-07-20 10:03:50] [admin] [192.168.8.211 2335] [show cli history N=10 ] [succeeded]
```

Query the latest 5 commands that have been executed.

```text
admin:/>show cli history N=5
[2012-03-31 14:16:03] [admin] [192.168.8.211 2335] [show cli configuration] [succeeded]
[2012-03-31 14:16:13] [admin] [192.168.8.211 2335] [change cli silent_enabled=no] [succeeded]
[2012-03-31 14:17:11] [admin] [192.168.8.211 2335] [show cli history ] [succeeded]
[2012-03-31 14:18:35] [admin] [192.168.8.211 2335] [show cli history ] [succeeded]
[2012-03-31 14:18:58] [admin] [192.168.8.211 2335] [show cli history ] [succeeded]
```

##### System Response

None
