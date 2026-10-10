# change key_service general


##### Function

The **change key_service general** command is used to modify the key service configuration.

##### Format

**change key_service general** \[ service_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| service_type=? | Key service type. | The value can be "Disable", "KMS" or "KMC", where: <br>"Disable": Disable key management server.<br>"KMS": Internal key management service.<br>"KMC": External key management service. |

##### Usage Guidelines

None

##### Example

Modify the key service configuration.

```text

admin:/>change key_service general service_type=KMS
CAUTION: You are about to use the internal key management service.
Suggestion: In order to improve system reliability, you are advised to configure and open the key file backup server. The internal key management service automatically backs up the key file to the server.
Do you wish to continue?(y/n)y
Command executed successfully.

```

##### System Response

None
