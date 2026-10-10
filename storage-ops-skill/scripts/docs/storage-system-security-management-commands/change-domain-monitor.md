# change domain monitor


##### Function

The **change domain monitor** command is used to enable or disable the monitoring function for the external domain controller of the vStore and configure the monitoring period when the function is enabled.

##### Format

**change domain monitor** domaintype=? { interval=? \| enable=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domaintype=? | Type of the domain controller. | The value can be "DNS", "AD", "LDAP", or "NIS", where: <br>"DNS": configures the DNS server monitoring switch and monitoring period.<br>"AD": configures the AD server monitoring switch and monitoring period.<br>"LDAP": configures the monitoring switch and monitoring period of the LDAP server.<br>"NIS": configures the monitoring switch and monitoring period of the NIS server. |
| interval=? | Indicates the monitoring period. | The value is an integer ranging from 5 to 300. |
| enable=? | Indicates whether to monitor the domain controller. | The value can be "yes" or "no", where: <br>"yes": enables monitoring.<br>"no": disables monitoring. |
| timeout=? | Timeout interval between the storage array and domain controller. | The value is an integer ranging from 10 to 10000. |

##### Usage Guidelines

None

##### Example

Enable the function that monitors the AD domain controller and set the monitoring period to 5 seconds.

```text
admin:/>change domain monitor domaintype=AD interval=5
Command executed successfully.
```

##### System Response

None
