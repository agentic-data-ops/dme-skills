# create hyper_metro_pair verification_session


##### Function

The **create hyper_metro_pair verification_session** command is used to verify the configuration consistency of the primary and secondary devices of a HyperMetro pair.

##### Format

**create hyper_metro_pair verification_session** pair_id=?

##### Parameters

| Parameter | Description                | Value                                                                |
|-----------|----------------------------|----------------------------------------------------------------------|
| pair_id=? | ID of the HyperMetro pair. | Run the "show hyper_metro_pair general" command to obtain the value. |

##### Usage Guidelines

None

##### Example

Verify the configuration consistency of the primary and secondary devices of HyperMetro pair "1".

```text
admin:/>create hyper_metro_pair verification_session pair_id=1
Command executed successfully.
```

##### System Response

None
