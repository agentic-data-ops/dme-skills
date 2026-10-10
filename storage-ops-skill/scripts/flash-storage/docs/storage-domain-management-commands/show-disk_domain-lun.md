# show disk_domain lun


##### Function

The **show disk_domain lun** command is used to query information about LUNs in a specified disk domain.

##### Format

**show disk_domain lun** disk_domain_id=?

##### Parameters

| Parameter        | Description     | Value                                                |
|------------------|-----------------|------------------------------------------------------|
| disk_domain_id=? | Disk domain ID. | To obtain the value, run "show disk_domain general". |

##### Usage Guidelines

None.

##### Example

Query information about LUNs in disk domain "0".

```text
admin:/>show disk_domain lun disk_domain_id=0

LUN ID  LUN Name  Health Status  Running Status
------  --------  -------------  --------------
0       regina    Normal         Online
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                       |
|----------------|-------------------------------|
| LUN ID         | Indicates the LUN ID.         |
| LUN Name       | Indicates the LUN name.       |
| Health Status  | Indicates the health status.  |
| Running Status | Indicates the running status. |
