# change remote_support agreement


##### Function

The **change remote_support agreement** command is used to sign the letter of authorization.

##### Format

**change remote_support agreement** status=?

##### Parameters

| Parameter | Description                                  | Value                  |
|-----------|----------------------------------------------|------------------------|
| status    | Signing status of a letter of authorization. | The value is "signed". |

##### Usage Guidelines

The command is used to sign the letter of authorization. You can query the signing status by running the "show remote_support agreement" command.

##### Example

Configure the electronic signature for a letter of authorization.

```text
admin:/>change remote_support agreement status=signed
CAUTION: You are about to sign the eService authorization letter. The eService periodically sends storage array health data to the eService site, including fault diagnosis data, performance statistics, logs, and configurations, but does not send any service data or personal privacy data.
Suggestion: Before performing this operation, ensure that you have understood the content of the eService authorization letter.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
