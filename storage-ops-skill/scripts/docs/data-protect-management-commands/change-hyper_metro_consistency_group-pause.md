# change hyper_metro_consistency_group pause


##### Function

The **change hyper_metro_consistency_group pause** command is used to pause a HyperMetro consistency group.

##### Format

**change hyper_metro_consistency_group pause** consistency_group_id=? \[ stop_role=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| consistency_group_id=? | ID of the consistency group. | Run the "show hyper_metro_consistency_group general" command without parameters to obtain the value. |
| stop_role=? | Site whose services you want to stop (When the running status of a HyperMetro consistency group is "Synchronizing" or "To Be Synchronized", you cannot stop services at the site that uniquely provides host read and write services). | The value can be "Preferred" or "Non-preferred", where: <br>"Preferred": Preferred site.<br>"Non-preferred": Non-preferred site. |

##### Usage Guidelines

None

##### Example

Pause HyperMetro consistency group "21008038bc1e70e90000000100000000".

```text
admin:/>change hyper_metro_consistency_group pause consistency_group_id=21008038bc1e70e90000000100000000
CAUTION: You are about to pause the HyperMetro consistency group.
Once the HyperMetro consistency group is paused, real-time mirroring across sites stops and the member LUNs in the HyperMetro consistency groups can only be accessed in one direction.
Suggestion: Before performing this operation, ensure that the two sites are properly connected to hosts to prevent service exceptions.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
