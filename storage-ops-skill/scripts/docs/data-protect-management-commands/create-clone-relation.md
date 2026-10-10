# create clone relation


##### Function

The **create clone relation** command is used to create a clone pair.

##### Format

**create clone relation** { source_id_list=? \| source_name_list=? } { dst_id_list=? \| dst_name_list=? } \[ copy_speed=? \] \[ start_synchronize_after_create=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| source_id_list=? | Source LUN ID list or source snapshot ID list. | Use commas (,) to separate multiple source IDs, or use a hyphen (-) to specify an ID range, for example, "1,5-8". |
| source_name_list=? | Source LUN name list or source snapshot name list. | Use commas (,) to separate multiple source names. |
| dst_id_list=? | List of target LUN IDs. | Use commas (,) to separate multiple target IDs, or use a hyphen (-) to specify an ID range, for example, "1,5-8". |
| dst_name_list=? | List of target LUN names. | Use commas (,) to separate multiple target LUN names. |
| start_synchronize_after_create=? | Whether to start data synchronization after a clone pair is created. | The value can be "yes" or "no", where: <br>"yes": synchronization is started immediately after the creation.<br>"no": Synchronization is not started after the creation. |
| copy_speed=? | Copy rate. | The value can be "low", "middle", "high", or "highest", where: <br>"low": low speed.<br>"middle": medium speed.<br>"high": high speed.<br>"highest": highest speed. |

##### Usage Guidelines

None

##### Example

Create a clone pair for source LUN "6" and target LUN "7".

```text
admin:/>create clone relation source_id_list=6 dst_id_list=7
Create clone successfully.
```

##### System Response

None
