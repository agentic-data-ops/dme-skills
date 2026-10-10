# show domain nis


##### Function

The **show domain nis** command is used to query NIS domain authentication configurations.

##### Format

**show domain nis**

##### Parameters

None

##### Usage Guidelines

None

##### Example

Query NIS domain authentication configurations.

```text
admin:/>show domain nis

Name : nisdomain
IP Address List : 10.40.25.10,10.40.25.11,10.40.25.12
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IP Address List | IP addresses or host name of the NIS server. A maximum of three IP addresses can be specified, and they must be separated from each other using commas (,). |
| Name            | Full domain name.                                                                                                                                           |
