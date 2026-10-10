# show lun_clone available_lun


##### Function

The **show lun_clone available_lun** command is used to query the information about all LUNs that can serve as clone source LUNs.

##### Format

**show lun_clone available_lun**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

Query information about all LUNs that can serve as clone source LUNs.

```text
admin:/>show lun_clone available_lun
ID     Name        Pool ID  Capacity   Health Status  Running Status  WWN                               Type
-----  ----------  -------  ---------  -------------  --------------  --------------------------------  ----
0      LUN0010000  0         10.000GB  Normal         Online          6707990100055f02000cf73200000000  Thin
1      LUN0010001  0         10.000GB  Normal         Online          6707990100055f02000cf78500000001  Thin
2      LUN0010002  0         10.000GB  Normal         Online          6707990100055f02000cf7cf00000002  Thin
3      LUN0010003  0         10.000GB  Normal         Online          6707990100055f02000cf81b00000003  Thin
4      LUN0010004  0         10.000GB  Normal         Online          6707990100055f02000cf87000000004  Thin
5      LUN0010005  0         10.000GB  Normal         Online          6707990100055f02000cf8b100000005  Thin
6      LUN0010006  0         10.000GB  Normal         Online          6707990100055f02000cf8fc00000006  Thin
7      LUN0010007  0         10.000GB  Normal         Online          6707990100055f02000cf98100000007  Thin
8      LUN0010008  0         10.000GB  Normal         Online          6707990100055f02000cf9c500000008  Thin
9      LUN0010009  0         10.000GB  Normal         Online          6707990100055f02000cfa0f00000009  Thin
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                        |
|----------------|--------------------------------|
| ID             | Indicates the LUN ID.          |
| Name           | Indicates the LUN name.        |
| Pool ID        | Indicates the storage pool ID. |
| Capacity       | Indicates the total capacity.  |
| Health Status  | Indicates the health status.   |
| Running Status | Indicates the running status.  |
| WWN            | Indicates the World Wide Name. |
| Type           | Indicates the LUN type.        |
