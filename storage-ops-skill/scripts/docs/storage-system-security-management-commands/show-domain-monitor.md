# show domain monitor


##### Function

The **show domain monitor** command is used to view the monitoring information of a domain controller.

##### Format

**show domain monitor** domaintype=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domaintype=? | Type of the domain controller. | The value can be "DNS", "AD", "LDAP", or "NIS", where: <br>"DNS": configures the monitoring switch and monitoring period of the DNS server.<br>"AD": configures the monitoring switch and monitoring period of the AD server.<br>"LDAP": configures the monitoring switch and monitoring period of the LDAP server.<br>"NIS": configures the monitoring switch and monitoring period of the NIS server. |

##### Usage Guidelines

None

##### Example

Query the monitoring information of the AD domain controller.

```text
admin:/>show domain monitor domaintype=AD
Controller Type     : AD
Monitoring Interval : 5
Monitoring Enable   : Yes
Monitoring Timeout  : 1000
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning                                                           |
|---------------------|-------------------------------------------------------------------|
| Controller Type     | Type of the domain controller.                                    |
| Monitoring Interval | Monitoring period of the domain controller.                       |
| Monitoring Enable   | Whether monitoring is enabled for the domain controller.          |
| Monitoring Timeout  | Timeout interval between the storage array and domain controller. |
