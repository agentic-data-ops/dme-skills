# change hyper_metro_consistency_group priority


##### Function

The **change hyper_metro_consistency_group priority** command is used to change the priority of the primary and secondary devices of a HyperMetro consistency group.

##### Format

**change hyper_metro_consistency_group priority** consistency_group_id=?

##### Parameters

| Parameter              | Description                             | Value                                                                                                |
|------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------|
| consistency_group_id=? | ID of the HyperMetro consistency group. | Run the "show hyper_metro_consistency_group general" command without parameters to obtain the value. |

##### Usage Guidelines

None

##### Example

Swap the priority of the two sites of each pair in consistency group "1".

```text
admin:/>change hyper_metro_consistency_group priority consistency_group_id=1
CAUTION: You are about to execute a preferred site switchover. This operation will modify the arbitration priority when array communication is interrupted.
In static priority mode, if array communication is interrupted due to a preferred site switchover, the arbitration will fail.
Suggestion: Before performing this operation, suspend the HyperMetro consistency group in static priority mode.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
