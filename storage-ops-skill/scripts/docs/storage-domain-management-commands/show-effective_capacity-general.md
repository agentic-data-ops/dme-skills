# show effective_capacity general


##### Function

The **show effective_capacity general** command is used to query information about the effective capacity.

##### Format

**show effective_capacity general**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query information about the effective capacity of a system.

```text
admin:/>show effective_capacity general

Total Effective Capacity    : 200.000TB
Used Effective Capacity     : 1.078MB
Free Effective Capacity     : 199.999TB
Insufficient Threshold(%)   : 80
Used Up Threshold(%)        : 90
Left Days                   : --
Lun Used Effective Capacity : 0.000B
Fs Used Effective Capacity  : 1.078MB
```

##### System Response

The following table describes the parameter meanings.

| Parameter                   | Meaning                                                 |
|-----------------------------|---------------------------------------------------------|
| Total Effective Capacity    | Total effective capacity.                               |
| Used Effective Capacity     | Used effective capacity.                                |
| Free Effective Capacity     | Free effective capacity.                                |
| Insufficient Threshold(%)   | Alarm threshold indicating the insufficient capacity.   |
| Used Up Threshold(%)        | Alarm threshold indicating the used up capacity.        |
| Left Days                   | Number of remaining days when the capacity can be used. |
| Lun Used Effective Capacity | Used available capacity of the LUN.                     |
| Fs Used Effective Capacity  | Used available capacity of the file system.             |
