# show devicemanager ciphersuite


##### Function

The **show devicemanager ciphersuite** command is used to query the OpenSSL cipher suite used by DeviceManager service in the storage system.

##### Format

**show devicemanager ciphersuite**

##### Parameters

None

##### Usage Guidelines

The command output will show the OpenSSL cipher suite that is being used currently.

##### Example

Show the currently used cipher suite.

```text
admin:/>show devicemanager ciphersuite
Cipher suites : safe
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| Cipher Suite | The OpenSSL cipher suite that is being used currently. <br>"safe" indicates the used cipher suite is DHE-RSA-AES128-GCM-SHA256, DHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES128-CCM.<br>"compatible" indicates the used cipher suite is DHE-RSA-AES128-GCM-SHA256, DHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES128-CCM. |
