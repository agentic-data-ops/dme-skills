# show crl general


##### Function

The **show crl general** command is used to query certificate revocation list information on storage arrays in various scenarios.

##### Format

**show crl general** \[ type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Certificate revocation list type. | Possible values are: <br>"key_management_center": key management center.<br>"domain_authentication": domain authentication.<br>"hypermetro_arbitration": HyperMetro arbitration.<br>"call_home_authentication": Call Home authentication.<br>"sso_authentication": SSO authentication.<br>"email_authentication": email authentication.<br>"integrity_protection": integrity protection.<br>"OTP_email_authentication": OTP email authentication.<br>"file_service_domain_authentication": file service domain authentication. |

##### Usage Guidelines

-   This command can be used to query certificate revocation list status and related information on the storage array in different scenarios.
-   The "**show crl general**" command can be used to query information about all certificate revocation lists.
-   The "**show crl general** type=?" command can be used to query information about the certificate revocation list in a specific scenario.

##### Example

Query the information of all certificate revocation lists.

```text
admin:/>show crl general
Type                      ID    Status        Issuer Name            Expire Time
------------------------  ----  ------------  ---------------------  -------------
Key Management Center    1     Non-existent  --                      --
Key Management Center    1     Non-existent  --                      --
Domain Authentication    1     Valid         HUAWEI                  2017-10-03
Domain Authentication    2     Invalid       THALES                  2017-03-01
Hypermetro Arbitration   1     Valid         HUAWEI                  2017-10-03
Hypermetro Arbitration   2     Non-existent  --                      --
Call Home Authentication 1     Non-existent  --                      --
Call Home Authentication 2     Non-existent  --                      --
SSO Authentication       1     Non-existent  --                      --
SSO Authentication       2     Non-existent  --                      --
Email Authentication     1     Non-existent  --                      --
Email Authentication     2     Non-existent  --                      --
Integrity Protection     1     Non-existent  --                      --
Integrity Protection     2     Non-existent  --                      --
OTP Email Authentication 1     Non-existent  --                      --
OTP Email Authentication 2     Non-existent  --                      --
```

Query the information of the certificate revocation list in a specific scenario.

```text
admin:/>show crl general type=domain_authentication
Type                      ID    Status        Issuer Name            Expire Time
------------------------  ----  ------------  ---------------------  -------------
Domain Authentication    1     Valid         HUAWEI                  2015-10-03
Domain Authentication    2     Invalid       THALES                  2015-03-01
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                                                                                                                                                                                                                                                                                                        |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type        | Certificate revocation list type. The certificate revocation list type can be key_management_center, domain_authentication, hypermetro_arbitration, call_home_authentication, sso_authentication, email_authentication, integrity_protection, otp_email_authentication, or file_service_domain_authentication. |
| ID          | Certificate revocation list ID.                                                                                                                                                                                                                                                                                |
| Status      | Certificate revocation list status. The value can be "Non-existent", "Valid", or "Invalid".                                                                                                                                                                                                                    |
| Issuer Name | Certificate revocation list issuer name.                                                                                                                                                                                                                                                                       |
| Expire Time | Certificate revocation list expiration time. "--" is displayed if the certificate revocation list does not exist.                                                                                                                                                                                              |
