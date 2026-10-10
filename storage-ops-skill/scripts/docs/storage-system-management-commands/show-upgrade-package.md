# show upgrade package


##### Function

The **show upgrade package** command is used to query details of the upgrade package.

##### Format

**show upgrade package**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

Query information of the upgrade package.

```text
admin:/>show upgrade package
Software Version
SN                    Name  IP          Current Version  History Version  Type
--------------------  ----  ----------  ---------------  ---------------  ----------
20130000021111111111  0A    10.94.80.72  VXXXRXXXCXX      --               Controller
20130000021111111111  0B    10.94.80.73  VXXXRXXXCXX      --               Controller
HotPatch Version
SN                    Name  IP          Current Version  History Version  Type
--------------------  ----  ----------  ---------------  ---------------  ----------
20130000021111111111  0A    10.94.80.72  --               --               Controller
20130000021111111111  0B    10.94.80.73  --               --               Controller
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning          |
|-----------------|------------------|
| SN              | Serial number.   |
| Name            | Node name.       |
| IP              | IP address.      |
| Current Version | Current version. |
| History Version | History version. |
| Type            | Node type.       |
