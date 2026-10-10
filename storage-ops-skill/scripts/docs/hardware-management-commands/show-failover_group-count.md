# show failover_group count


##### Function

The **show failover_group count** command is used to query the number of failover groups on the storage system.

##### Format

**show failover_group count** \[ service_type=? \]

##### Parameters

| Parameter    | Description                       | Value |
|--------------|-----------------------------------|-------|
| service_type | Service type of a failover group. | \-    |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the number of failover groups.

```text
admin:/>show failover_group count
Failover Group Number : 9
```

Query the number of failover groups whose service type is NAS.

```text
admin:/>show failover_group count service_type=NAS
Failover Group Number : 6
```

##### System Response

The following table describes the parameter meanings.

| Parameter             | Meaning                    |
|-----------------------|----------------------------|
| Failover Group Number | Number of failover groups. |
