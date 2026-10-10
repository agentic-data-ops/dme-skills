# show kmc general


##### Function

The **show kmc general** command is used to query the configurations of the external key management server.

##### Format

**show kmc general**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query the configurations of the external key management server.

```text
admin:/>show kmc general
ID  IP Address      Port  Type
--  --------------  ----  -----------
1   192.168.33.120  98    Thales Kmip
```

##### System Response

The following table describes the parameter meanings.

| Parameter  | Meaning                                                        |
|------------|----------------------------------------------------------------|
| ID         | ID of the configuration of the external key management server. |
| IP Address | IP address of the external key management server.              |
| Port       | Port number of the external key management server.             |
| Type       | Type of the external key management server.                    |
