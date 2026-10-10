# create hyper_metro_consistency_group verification_session


##### Function

The **create hyper_metro_consistency_group verification_session** command is used to verify the configuration consistency of the primary and secondary devices of a HyperMetro consistency group.

##### Format

**create hyper_metro_consistency_group verification_session** consistency_group_id=?

##### Parameters

| Parameter            | Description                                                                                          | Value |
|----------------------|------------------------------------------------------------------------------------------------------|-------|
| consistency_group_id | Run the "show hyper_metro_consistency_group general" command without parameters to obtain the value. | \-    |

##### Usage Guidelines

None

##### Example

Verify the configuration consistency of the primary and secondary devices of HyperMetro consistency group "1".

```text
admin:/>create hyper_metro_consistency_group verification_session consistency_group_id=1
Command executed successfully.
```

##### System Response

None
