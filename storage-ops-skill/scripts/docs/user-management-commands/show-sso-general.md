# show sso general


##### Function

The **show sso general** command is used to query the single sign-on (SSO) configuration.

##### Format

**show sso general**

##### Parameters

None

##### Usage Guidelines

After the command is executed successfully, the SSO configuration will be returned.

##### Example

Query the SSO configuration.

```text
admin:/>show sso general
Switch  : On
Address : 192.168.1.2
Port    : 31942
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                       |
|-----------|-------------------------------|
| Switch    | Switch for the SSO function.  |
| Address   | IP address of the SSO server. |
| Port      | Port of the SSO server.       |
