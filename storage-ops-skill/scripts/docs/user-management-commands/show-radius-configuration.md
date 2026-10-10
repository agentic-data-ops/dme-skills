# show radius configuration


##### Function

The **show radius configuration** command is used to query the RADIUS configuration.

##### Format

**show radius configuration**

##### Parameters

None

##### Usage Guidelines

After this command is executed successfully, the system displays the RADIUS configuration.

##### Example

Query RADIUS configurations.

```text
admin:/>show radius configuration
Switch  : Off
Address : --
Port    : 1812
Scheme  : CHAP
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                               |
|-----------|---------------------------------------|
| Switch    | Whether to enable the RADIUS service. |
| Port      | Port number of the RADIUS server.     |
| Address   | RADIUS server address.                |
| Scheme    | RADIUS server authentication policy.  |
