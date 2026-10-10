# show devicemanager tls_versions


##### Function

The "**show devicemanager tls_versions**" command is used to query version information of the TLS which is be used to the DeviceManager service on the storage system.

##### Format

**show devicemanager tls_versions**

##### Parameters

None

##### Usage Guidelines

None

##### Example

To query the version information of the TLS which is be used to DeviceManager on the storage system.

```text
admin:/>show devicemanager tls_versions
TLS Versions  : TLSv1.2 TLSv1.1 TLSv1
Controller ID  : 0A
------------------------------------------
TLS Versions  : TLSv1.2 TLSv1.1 TLSv1
Controller ID  : 0B

```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                                           |
|---------------|-----------------------------------------------------------------------------------|
| TLS Versions  | The version information of the TLS which is be used to the DeviceManager Service. |
| Controller ID | ID of a controller.                                                               |
