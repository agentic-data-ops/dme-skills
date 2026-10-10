# show host host_group


##### Function

The **show host host_group** command is used to query information about the host group that is associated with a host.

##### Format

**show host host_group** { host_id=? \| host_name=? }

##### Parameters

| Parameter   | Description | Value                                         |
|-------------|-------------|-----------------------------------------------|
| host_id=?   | Host ID.    | To obtain the value, run "show host general". |
| host_name=? | Host name.  | To obtain the value, run "show host general". |

##### Usage Guidelines

None.

##### Example

Query information about the host group that is associated with host "0".

```text
admin:/>show host host_group host_id=0

Host Group ID  Host Group Name
-------------  ---------------
0              HostGroup000
```

Query information about the host group that is associated with host "HostGroup000".

```text
admin:/>show host host_group host_name=HostGroup000

Host Group ID  Host Group Name
-------------  ---------------
0              HostGroup000
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                 |
|-----------------|-------------------------|
| Host Group ID   | ID of the host group.   |
| Host Group Name | Name of the host group. |
