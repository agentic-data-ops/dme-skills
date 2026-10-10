# show ca_server


##### Function

The **show ca_server** command is used to query the CA server configuration.

##### Format

**show ca_server**

##### Parameters

None

##### Usage Guidelines

Run the "**show ca_server**" command to query the CA server configuration.

##### Example

Query the CA server configuration.

```text
admin:/>show ca_server
Auto Update Enabled       : Yes
CA Server Addr            : 192.168.3.3
CA Server Port            : 80
Update Lead Time          : 30
Update Endpoint           : /autoupdate
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning                                                              |
|---------------------|----------------------------------------------------------------------|
| Auto Update Enabled | Whether automatic certificate update is enabled or disabled.         |
| CA Server Addr      | Address of the CA server.                                            |
| CA Server Port      | Port of the CA server.                                               |
| Update Lead Time    | Time before which the certificate is automatically updated, in days. |
| Update Endpoint     | Endpoint for automatic certificate update (URI).                     |
