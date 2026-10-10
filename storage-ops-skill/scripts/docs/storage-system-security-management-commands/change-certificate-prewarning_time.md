# change certificate prewarning_time


##### Function

The **change certificate prewarning_time** command is used to change the expiration warning days of certificates.

##### Format

**change certificate prewarning_time** type=? prewarning_time=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Certificate type. | Possible values are: <br>"key_management_center": key management center.<br>"domain_authentication": domain authentication.<br>"hypermetro_arbitration": HyperMetro arbitration.<br>"syslog_authentication": Syslog server authentication.<br>"ntp_authentication": NTP server authentication.<br>"call_home_authentication": Call Home server authentication.<br>"email_authentication": Email server authentication.<br>"devicemanager_authentication": DeviceManager authentication.<br>"sso_authentication": SSO authentication.<br>"OTP_email_authentication": OTP email server authentication.<br>"file_service_domain_authentication": file service domain authentication.<br>"certification_authority": CA server authentication.<br>"https_protocol": HTTPS protocol.<br>"ftps_protocol": FTPS protocol.<br>"smart_container_authentication": container service authentication. |
| prewarning_time=? | Certificate expiration warning days. | The value ranges from 7 to 180, expressed in days. |

##### Usage Guidelines

Running this command to change the expiration warning days of certificates in all scenarios.

##### Example

Change the expiration warning days of certificates.

```text
admin/>change certificate prewarning_time type=domain_authentication prewarning_time=30
Command executed successfully.
```

##### System Response

None
