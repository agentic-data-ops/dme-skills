# remove hyper_metro_domain quorum_server


##### Function

The **remove hyper_metro_domain quorum_server** command is used to remove a quorum server from HyperMetro domains.

##### Format

**remove hyper_metro_domain quorum_server** domain_id=? server_id=?

##### Parameters

| Parameter   | Description           | Value                                                                   |
|-------------|-----------------------|-------------------------------------------------------------------------|
| domain_id=? | HyperMetro domain ID. | To obtain the value, run the "show hyper_metro_domain general" command. |
| server_id=? | Quorum server ID.     | To obtain the value, run the "show quorum_server general" command.      |

##### Usage Guidelines

None

##### Example

Remove the quorum server whose ID is "1" from the HyperMetro domain whose ID is "0".

```text

admin:/>remove hyper_metro_domain quorum_server domain_id=0 server_id=1
WARNING: You are about to remove the quorum server from the HyperMetro domain.
This operation will change the HyperMetro arbitration mode.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
