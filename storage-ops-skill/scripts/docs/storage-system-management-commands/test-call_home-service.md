# test call_home service


##### Function

The **test call_home service** command is used to test whether the Call Home service is normal.

##### Format

**test call_home service**

##### Parameters

None

##### Usage Guidelines

This command is used to test whether the Call Home service is normal. Before running this command, confirm that basic information of the Call Home service has been correctly configured, including the configuration of the proxy server and the technical support center.

##### Example

Test whether the Call Home service is normal.

```text
admin:/>test call_home service

Controller ID  Status
-------------  -----------
0A        Unreachable
0B        Reachable
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                    |
|---------------|------------------------------------------------------------|
| Controller ID | Controller ID.                                             |
| Status        | Result of testing the Call Home service's redundant links. |
