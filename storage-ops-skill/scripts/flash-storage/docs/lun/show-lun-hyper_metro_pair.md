# show lun hyper_metro_pair


##### Function

The **show lun hyper_metro_pair** command is used to query information about LUNs for which HyperMetro is configured.

##### Format

**show lun hyper_metro_pair** lun_mapped=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_mapped=? | Whether HyperMetro LUNs are mapped. | The value can be "yes" or "no", where: <br>"yes": The HyperMetro LUN has been mapped.<br>"no": The HyperMetro LUN has not been mapped. |

##### Usage Guidelines

This command can only be used to query information about HyperMetro LUNs on the local storage system.

##### Example

Query HyperMetro LUNs that are not mapped.

```text
admin:/>show lun hyper_metro_pair lun_mapped=no
ID  Name        Pool ID  Capacity  Health Status  Running Status  Type  WWN                               Is Add To Lun Group  Smart Cache Partition ID  DIF Switch
--  ----------  -------  --------  -------------  --------------  ----  --------------------------------  -------------------  ------------------------  ----------
0   LUN0010000  0        5.000GB   Normal         Online          Thin  60c45ba100a1f330000a451200000000  Yes                  --                        No
1   LUN0010001  0        5.000GB   Normal         Online          Thin  60c45ba100a1f330000a45b100000001  Yes                  --                        No
2   LUN0010002  0        5.000GB   Normal         Online          Thin  60c45ba100a1f330000a468a00000002  Yes                  --                        No
3   LUN0010003  0        5.000GB   Normal         Online          Thin  60c45ba100a1f330000a474100000003  Yes                  --                        No
4   LUN0010004  0        5.000GB   Normal         Online          Thin  60c45ba100a1f330000a481c00000004  Yes                  --                        No
5   LUN0010005  0        5.000GB   Normal         Online          Thin  60c45ba100a1f330000a48b400000005  Yes                  --                        No
6   LUN0010006  0        5.000GB   Normal         Online          Thin  60c45ba100a1f330000a497500000006  Yes                  --                        No
```

##### System Response

The following table describes the parameter meanings.

| Parameter                | Meaning                                      |
|--------------------------|----------------------------------------------|
| ID                       | LUN ID.                                      |
| Name                     | LUN name.                                    |
| Pool ID                  | Storage pool ID.                             |
| Capacity                 | Total capacity.                              |
| Health Status            | Health status.                               |
| Running Status           | Running status.                              |
| Type                     | LUN type.                                    |
| WWN                      | World Wide Name.                             |
| Is Add To Lun Group      | Whether a LUN has been added to a LUN group. |
| Smart Cache Partition ID | SmartCache partition ID.                     |
| DIF Switch               | Whether to enable the DIF function.          |
