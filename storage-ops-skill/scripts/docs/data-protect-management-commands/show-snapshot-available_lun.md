# show snapshot available_lun


##### Function

The **show snapshot available_lun** command is used to query the information on the logical unit numbers (LUNs) that can serve as snapshot source LUNs.

##### Format

**show snapshot available_lun**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the information on the LUNs that can serve as snapshot source LUNs.

```text
admin:/>show snapshot available_lun

ID  Name           Pool ID  Capacity   Health Status  Running Status  WWN  Type
--  -------------  -------  --------   -------------  --------------  ---  -----
2   newlun         1        100.000MB  Normal         Online          --   Thick
1   testlun        1        300.000MB  Normal         Online          --   Thick
3   newlun0020000  1         10.000GB  Normal         Online          --   Thick
4   newlun0020001  1         10.000GB  Normal         Online          --   Thick
5   newlun0020002  1         10.000GB  Normal         Online          --   Thick
6   newlun0020003  1         10.000GB  Normal         Online          --   Thick
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
