# add fs_hyper_metro_domain quorum_server


##### Function

The **add fs_hyper_metro_domain quorum_server** command is used to add a quorum server to a HyperMetro domain.

##### Format

**add fs_hyper_metro_domain quorum_server** domain_id=? server_id=?

##### Parameters

| Parameter   | Description           | Value |
|-------------|-----------------------|-------|
| domain_id=? | HyperMetro domain ID. | \-    |
| server_id=? | Quorum server ID.     | \-    |

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
