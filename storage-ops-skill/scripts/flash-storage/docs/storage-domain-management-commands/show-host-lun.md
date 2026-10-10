# show host lun


##### Function

The **show host lun** command is used to query all the LUNs that have been mapped to hosts in the storage system.

##### Format

**show host lun** { host_id=? \| host_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_id=? | Host ID. | To obtain the value, run "show host general". |
| host_name=? | Host name. | To obtain the value, run "show host general". |
| lun_name_list=? | Specifies multiple LUN names. | You can run the "show lun general" command to obtain the LUN name list. When multiple LUNs need to be specified: You can use commas (,) to separate multiple LUN names or snapshot names. For example, lun_name_list=lun1,lun2,lun3,lun4,lun5. |
| lun_id_list=? | List of specified LUN IDs. | You can run the "show lun general" command to obtain the LUN ID list. When multiple LUNs need to be specified: <br>Multiple LUN IDs can be separated by commas (,). For example, lun_id_list=1,2,3,4,5.<br>You can specify LUN ID ranges by hyphens (-). For example, lun_id_list=1-5,7,9-11. |

##### Usage Guidelines

None.

##### Example

Query all the LUNs that have been mapped to host "2".

```text
admin:/>show host lun host_id=2

LUN ID LUN Name Host LUN ID
------ -------- -----------
34 lun_0000 4
35 lun_0001 5
36 lun_0002 6
```

Query all the LUNs that have been mapped to host "HostGroup000".

```text
admin:/>show host lun host_name=HostGroup000

LUN ID LUN Name Host LUN ID
------ -------- -----------
34 lun_0000 4
35 lun_0001 5
36 lun_0002 6
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning          |
|-------------|------------------|
| LUN ID      | LUN ID.          |
| LUN Name    | Name of the LUN. |
| Host LUN ID | Host LUN ID.     |
