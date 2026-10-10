# delete crl general


##### Function

The **delete crl general** command is used to delete the certificate revocation list.

##### Format

**delete crl general** type=? \[ id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Certificate revocation list type. | Possible values are: <br>"key_management_center": key management center.<br>"domain_authentication": domain authentication.<br>"hypermetro_arbitration": HyperMetro arbitration.<br>"call_home_authentication": Call Home authentication<br>"sso_authentication": SSO authentication.<br>"email_authentication": email authentication.<br>"integrity_protection": integrity protection.<br>"OTP_email_authentication": OTP email authentication.<br>"file_service_domain_authentication": file service domain authentication. |
| id=? | Certificate revocation list ID. | The value can be 1 or 2. |

##### Usage Guidelines

-   This command supports that a certificate revocation list can be deleted based on application scenarios.
-   The certificate revocation list type supported by this command can be "key_management_center", "domain_authentication", "hypermetro_arbitration", "call_home_authentication", "sso_authentication", "email_authentication", "integrity_protection", "OTP_email_authentication", or "file_service_domain_authentication".

##### Example

Delete all certificate revocation list information in a specified scenario.

```text
admin/>delete crl general type=domain_authentication
WARNING: You are about to delete the certificate revocation list. This operation may cause the SSL connection between the storage system and the server that has an invalid certificate.
Suggestion:  Before performing this operation, ensure that you accept the aforementioned risks.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete certificate revocation list information for the specified index in the specified scenario.

```text
admin/>delete crl general type=domain_authentication id=1
WARNING: You are about to delete the certificate revocation list. This operation may cause the SSL connection between the storage system and the server that has an invalid certificate.
Suggestion:  Before performing this operation, ensure that you accept the aforementioned risks.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
