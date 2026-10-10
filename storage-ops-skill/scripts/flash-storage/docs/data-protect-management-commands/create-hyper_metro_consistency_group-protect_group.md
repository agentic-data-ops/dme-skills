# create hyper_metro_consistency_group protect_group


##### Function

The **create hyper_metro_consistency_group protect_group** command is used to create a HyperMetro consistency group for a protection group.

##### Format

**create hyper_metro_consistency_group protect_group** protect_group_id=? domain_id=? remote_storage_pool_id=? \[ synchronization_mapping=? mapping_info=? \| recovery_policy=? \| synchronization_rate=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| protect_group_id=? | ID of the protection group. | The value ranges from 0 to 16383. |
| domain_id=? | ID of the HyperMetro domain. | To obtain the value, run the "show hyper_metro_domain general" command without parameters. |
| remote_storage_pool_id=? | Remote storage pool ID. | To obtain the value, run the "show storage_pool general" command on the remote storage system. |
| recovery_policy=? | Recovery policy. | The value can be "automatic" or "manual", where: <br>"automatic": automatic recovery policy. Data will be automatically synchronized after faults are rectified.<br>"manual": manual recovery policy. Data needs to be manually synchronized after faults are rectified.<br> The default value is "automatic". |
| synchronization_rate=? | Synchronization speed. | The value is "Low", "Middle", "High", or "Highest", where: <br>"Low": low speed.<br>"Middle": medium speed.<br>"High": high speed.<br>"Highest": the highest speed.<br> The default value is "Middle". |
| synchronization_mapping | Whether mappings are synchronized. | The value is "1", indicating that mappings are synchronized. NOTE: If this parameter is not specified, mappings are not synchronized by default. |
| mapping_info | Mapping information. | The values are in JOSN format, where: <br>The value of "host_id" ranges from 0 to 24575.<br>The value of "host_group_id" ranges from 0 to 8191. |

##### Usage Guidelines

After this command is executed, the system automatically creates LUNs in the storage pool of the specified remote device and those LUNs have the same attributes as all member LUNs in the local protection group. In addition, the system creates HyperMetro pairs and a HyperMetro consistency group, adds all HyperMetro pairs to the HyperMetro consistency group, and synchronizes the consistency group.

##### Example

Create a HyperMetro consistency group for a protection group.

```text
admin:/>create hyper_metro_consistency_group protect_group protect_group_id=0 domain_id=1b02030405060100 remote_storage_pool_id=0 synchronization_mapping=yes mapping_info=host_id:0
Enabling protection for PG or LUN group (PG0001) in background.
Run the "show task general task_id=4" command to query the execution result.
```

##### System Response

None
