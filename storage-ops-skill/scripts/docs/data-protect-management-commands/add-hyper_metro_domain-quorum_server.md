# add hyper_metro_domain quorum_server


##### Function

The add hyper_metro_domain command is used to add a quorum server to HyperMetro domains.

##### Format

**add hyper_metro_domain quorum_server** domain_id=? server_id=?

##### Parameters

| Parameter   | Description           | Value                                                                   |
|-------------|-----------------------|-------------------------------------------------------------------------|
| domain_id=? | HyperMetro domain ID. | To obtain the value, run the "show hyper_metro_domain general" command. |
| server_id=? | Quorum server ID.     | To obtain the value, run the "show quorum_server general" command.      |

##### Usage Guidelines

None

##### Example

Add the quorum server whose ID is "1" to the HyperMetro domain whose ID is "0".

```text
admin:/>add hyper_metro_domain quorum_server domain_id=0 server_id=1
CAUTION: You are about to add the quorum server to the HyperMetro domain.
This operation will change the HyperMetro arbitration mode.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent service exceptions.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
