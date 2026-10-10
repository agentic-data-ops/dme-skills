# change hyper_metro_pair priority


##### Function

The **change hyper_metro_pair priority** command is used to change the priority of the primary and secondary LUNs of a SAN HyperMetro pair.

##### Format

**change hyper_metro_pair priority** pair_id=?

##### Parameters

| Parameter | Description                | Value                                                                |
|-----------|----------------------------|----------------------------------------------------------------------|
| pair_id=? | ID of the HyperMetro pair. | Run the "show hyper_metro_pair general" command to obtain the value. |

##### Usage Guidelines

None

##### Example

Change the priority of the primary and secondary LUNs of HyperMetro pair "1".

```text
admin:/>change hyper_metro_pair priority pair_id=1
CAUTION: You are about to perform a preferred/non-preferred site switchover. This operation will modify the arbitration priority of member LUNs in a HyperMetro pair when the communication between two storage arrays is interrupted.
In static priority arbitration mode, if the communication between two storage arrays is interrupted upon a priority switchover, storage array arbitration fails at the two sites.
Suggestion: In static priority arbitration mode, before performing this operation, suspend the HyperMetro pair.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
