# show lun host


##### Function

The **show lun host** command is used to query the host to which a LUN is mapped.

##### Format

**show lun host** lun_name=?

##### Parameters

| Parameter  | Description | Value                                        |
|------------|-------------|----------------------------------------------|
| lun_name=? | LUN name.   | To obtain the value, run "show lun general". |

##### Usage Guidelines

None

##### Example

Query the host to which the LUN whose name is "lun01" is mapped.

```text
admin:/>show lun host lun_name=lun0010000

Host ID  Host Name
-------  ---------
0        host001

```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning    |
|-----------|------------|
| Host Name | Host name. |
| Host ID   | Host ID.   |
