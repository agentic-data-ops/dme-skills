# change host_group general


##### Function

The **change host_group general** command is used to change the name of a host group.

##### Format

**change host_group general** { host_group_id=? \| host_group_name=? } name=?

##### Parameters

| Parameter         | Description               | Value                                                                                        |
|-------------------|---------------------------|----------------------------------------------------------------------------------------------|
| host_group_id=?   | Host group ID.            | To obtain the value, run "show host_group general".                                          |
| host_group_name=? | Host group name.          | To obtain the value, run "show host_group general".                                          |
| name=?            | New name of a host group. | The value contains 1 to 255 digits, letters, underscores (\_), hyphens (-), and periods (.). |

##### Usage Guidelines

None.

##### Example

Change the name of host group "1" to "test110".

```text
admin:/>change host_group general host_group_id=1 name=test110
Command executed successfully.
```

Change the name of host group "HostGroupName1" to "HostGroupName2".

```text
admin:/>change host_group general host_group_name=HostGrouName1 name=HostGroupName2
Command executed successfully.
```

##### System Response

None
