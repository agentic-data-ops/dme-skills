# show disk in_domain


##### Function

The **show disk in_domain** command is used to query information about member disks in a specific disk domain.

##### Format

**show disk in_domain** disk_domain_id=?

##### Parameters

| Parameter        | Description     | Value                                                |
|------------------|-----------------|------------------------------------------------------|
| disk_domain_id=? | Disk domain ID. | To obtain the value, run "show disk_domain general". |

##### Usage Guidelines

None

##### Example

Query information about member disks in disk domain "0". The ID and output vary depending on a specific product.

```text
admin:/>show disk in_domain disk_domain_id=0
ID        Health Status  Running Status  Type     Capacity   Logic Type   Disk Domain ID  Speed(RPM)
--------  -------------  --------------  -------  ---------  -----------  --------------  ----------
DAE000.0  Normal         Online          SSD SED  832.626GB  Member Disk  0               0
DAE000.1  Normal         Online          SSD SED  832.626GB  Member Disk  0               0
DAE000.2  Normal         Online          SSD SED  832.626GB  Member Disk  0               0
DAE000.3  Normal         Online          SSD SED  832.626GB  Member Disk  0               0
DAE000.4  Normal         Online          SSD SED  837.626GB  Member Disk  0               0
DAE000.5  Normal         Online          SSD SED  837.626GB  Member Disk  0               0
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                       |
|----------------|-------------------------------|
| Type           | Disk type.                    |
| ID             | Disk ID.                      |
| Health Status  | Health status.                |
| Running Status | Running status.               |
| Capacity       | Capacity.                     |
| Logic Type     | Logic type.                   |
| Disk Domain ID | Disk's owning disk domain ID. |
| Speed(RPM)     | Revolutions per minute (rpm). |
