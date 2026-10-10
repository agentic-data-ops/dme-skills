# add lun_consistency_group lun


##### Function

The **add lun_consistency_group lun** command is used to add a member LUN to a specified LUN consistency group. Use this command if consistency management is required for LUNs.

##### Format

**add lun_consistency_group lun** lun_consistency_group_id=? lun_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| lun_consistency_group_id=? | ID of the LUN consistency group to which a member LUN is to be added. | To obtain the value, run "show lun_consistency_group general". |
| lun_id_list=? | ID list of LUNs to be added to a LUN consistency group. | To obtain the LUN ID list, run "show lun general". If you want to concurrently add multiple LUNs to a LUN consistency group: <br>Separate multiple LUN IDs by commas (,). For example, "lun_id_list=1,2,3,4,5".<br>Specify a LUN ID range using a hyphen (-). For example, "lun_id_list=1-5,7,9-11". |

##### Usage Guidelines

-   A LUN can be added to only one LUN consistency group.
-   A LUN consistency group can add a maximum of 2048 member LUNs.
-   PE LUNs, heterogeneous LUNs (eDevLUNs), and VVol LUNs cannot be added to a LUN consistency group.
-   LUNs that have been added to a timing snapshot schedule cannot be added to a consistency group.
-   LUNs with a SmartMigration task created cannot be added to a consistency group.

##### Example

Add LUN "2" to LUN consistency group "2".

```text
admin:/>add lun_consistency_group lun lun_consistency_group_id=2 lun_id_list=2
Add LUN 2 to LUN consistency group successfully.
```

##### System Response

None
