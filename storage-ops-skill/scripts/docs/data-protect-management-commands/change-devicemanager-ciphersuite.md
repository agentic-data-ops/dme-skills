# change devicemanager ciphersuite


##### Function

The **change devicemanager ciphersuite** command is used to configure the OpenSSL cipher suite used by the DeviceManager service.

##### Format

**change devicemanager ciphersuite** suite=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| suite=? | OpenSSL cipher suite type (if the "safe" type is selected, the HTTPS key agreement algorithm uses ECDHE. The "safe" type is applicable to users requiring high security levels). | The value can be: <br>"safe".<br>"compatible". |

##### Usage Guidelines

After this operation, DeviceManager will be restarted and the session will be interrupted.

##### Example

Change the cipher suite type to "safe".

```text
admin:/>change devicemanager ciphersuite suite=safe
WARNING: You are about to change the cipher suite type of DeviceManager. The following risks may exist:
1.If you change the cipher suite type to "safe", data transmission security will increase, but DeviceManager may be inaccessible for clients with a lower encryption level.
2.If you change the cipher suite type to "compatible", data transmission security will decrease and user data may have security risks.
3.The preceding operations will restart the DeviceManager service. As a result, some requests may fail to be sent within a short period of time.
Suggestion: Confirm that you want to perform this operation.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
