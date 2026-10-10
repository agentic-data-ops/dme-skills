# create dr_star general


##### Function

The **create dr_star general** command is used to create DR Star.

##### Format

**create dr_star general** disaster_recovery_strategy=? member_type=? asynchronous_remote_replication_id=? { hyper_metro_id=? \| synchronous_remote_replication_id=? } name=? swap_strategy=? swap_silent_time=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| disaster_recovery_strategy | DR policy type. | The value can be "hyper_metro" or "synchronous_remote_replication", where: <br>"hyper_metro": HyperMetro network.<br>"synchronous_remote_replication": synchronous remote replication network.<br> Currently, only the HyperMetro network is supported. |
| member_type | Member type. | The value can be "pair" or "consistency_group", where: <br>"pair": pair.<br>"consistency_group": consistency group. |
| asynchronous_remote_replication_id | ID of an asynchronous remote replication member. | If member_type is pair, run "show remote_replication general" without parameters to obtain the value. Otherwise, run "show consistency_group general" without parameters to obtain the value. |
| hyper_metro_id | ID of a HyperMetro member. | If member_type is pair, run "show hyper_metro_pair general" without parameters to obtain the value. Otherwise, run "show hyper_metro_consistency_group general" without parameters to obtain the value. |
| synchronous_remote_replication_id | ID of a synchronous remote replication member. | If member_type is pair, run "show remote_replication general" without parameters to obtain the value. Otherwise, run "show consistency_group general" without parameters to obtain the value. |
| swap_strategy | Switchover policy. | The value can be "manual" or "automatic", where: <br>"manual": manual switchover.<br>"automatic": automatic switchover.<br> The default value is "automatic". |
| swap_silent_time | Switchover silence time. | The value ranges from 0 to 30, expressed in minutes. The default value is 30 minutes. |
| name | DR Star name. | The value contains 1 to 255 ASCII characters including digits, letters, hyphens (-), underscores (_), and periods (.), and can only start with a digit or a letter. |

##### Usage Guidelines

None

##### Example

Create DR Star and set the DR policy to "hyper_metro", member type to "pair", asynchronous remote replication member ID to "1a212d4a5e6b0003", and HyperMetro member ID to "1a212d4a5e6b0002".

```text
admin:/>create dr_star general disaster_recovery_strategy=hyper_metro member_type=pair asynchronous_remote_replication_id=1a212d4a5e6b0003 hyper_metro_id=1a212d4a5e6b0002 name=dr
Command executed successfully.
```

##### System Response

None
