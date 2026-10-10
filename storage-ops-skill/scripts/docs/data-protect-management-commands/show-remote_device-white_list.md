# show remote_device white_list


##### Function

The **show remote_device white_list** command is used to query the white list of heterogeneous disk arrays.

##### Format

**show remote_device white_list**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the white list of heterogeneous disk arrays.

```text
admin:/>show remote_device white_list

Record ID  Vendor       Product ID        Path Selector  Fail Back           Fail Over  ASL ID  Is User Added
---------  -----------  ----------------  -------------  ------------------  ---------  -----  -------------
7          EMC          CX4-240           ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     4      YES
8          HUASY        V1500             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
9          HUASY        V1800             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
10         HUASY        S2100             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
11         HUASY        S2300             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
12         HUASY        S2300E            ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
13         HUASY        S2600             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
14         HUASY        S5100             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
15         HUASY        S5300             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
16         HUASY        S5500             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
17         HUASY        S5600             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
18         HUASY        S6800E            ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
19         HUASY        S8000             ROUND_ROBIN    FAILBACK_IMMEDIATE  ENABLE     1      NO
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                                 |
|---------------|-------------------------------------------------------------------------|
| Record ID     | White list ID.                                                          |
| Vendor        | Vendor name.                                                            |
| Product ID    | Product model.                                                          |
| Path Selector | Algorithm used by a disk array to select a path.                        |
| Fail Back     | Failback mode.                                                          |
| Fail Over     | Whether failover is enabled.                                            |
| ASL ID        | ID of the support library of heterogeneous disk arrays.                 |
| Is User Added | Whether the white list of heterogeneous disk arrays is added by a user. |
