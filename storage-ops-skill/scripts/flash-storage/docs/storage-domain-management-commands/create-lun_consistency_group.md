# create lun_consistency_group


##### Function

The **create lun_consistency_group** command is used to create a LUN consistency group.

##### Format

**create lun_consistency_group** name=? \[ lun_id_list=? \] \[ description=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a LUN consistency group. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.). |
| lun_id_list=? | LUN ID list. Parameter "lun_id=?" is specified. | To obtain the LUN ID list, run "show lun general". If you want to concurrently add multiple LUNs to a LUN consistency group: <br>Separate multiple LUN IDs by commas (,). For example, "lun_id_list=1,2,3,4,5".<br>Specify a LUN ID range using a hyphen (-). For example, "lun_id_list=1-5,7,9-11". |
| description=? | Description of a LUN consistency group. | - |

##### Usage Guidelines

To create a LUN consistency group, perform the following:

Manually specify the parameters of a LUN consistency group.

**create lun_consistency_group** name=? \[**lun_id_list=***?*\] \[**description=***?*\]

##### Example

Create a LUN consistency group, where its parameter is as follows: Name: lun_consistency1.

```text
admin:/>create lun_consistency_group name=lun_consistency1
Create LUN consistency group successfully.

```

Create a LUN consistency group, where its parameters are as follows:
-   Name: lun_consistency1.
-   LUN ID list: 1-5.

```text
admin:/>create lun_consistency_group name=lun_consistency1 lun_id_list=1-5
Create LUN consistency group successfully.
Add LUN 1 to LUN consistency group successfully.
Add LUN 2 to LUN consistency group successfully.
Add LUN 3 to LUN consistency group successfully.
Add LUN 4 to LUN consistency group successfully.
Add LUN 5 to LUN consistency group successfully.
```

##### System Response

None
