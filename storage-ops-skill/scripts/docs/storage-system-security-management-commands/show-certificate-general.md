# show certificate general


##### Function

The show certificate command is used to query certificate information on storage arrays in various scenarios.

##### Format

**show certificate general** \[ type=? \] \[ detail=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Certificate type. | Possible values are: <br>"key_management_center": key management center.<br>"device_management": device management.<br>"domain_authentication": domain authentication.<br>"hypermetro_arbitration": HyperMetro arbitration.<br>"syslog_authentication": Syslog server authentication.<br>"ntp_authentication": NTP server authentication.<br>"call_home_authentication": Call Home server authentication.<br>"email_authentication": email server authentication.<br>"disk_authentication": disk authentication.<br>"sso_authentication": SSO authentication.<br>"OTP_email_authentication": OTP email server authentication.<br>"file_service_domain_authentication": file service domain authentication.<br>"certification_authority": CA server authentication.<br>"https_protocol": HTTPS protocol.<br>"ftps_protocol": FTPS protocol.<br>"smart_container_authentication": container service authentication. |
| detail=? | Queries detailed information. | The value is "yes", indicating to query detailed information. |

##### Usage Guidelines

-   This command is used to query certificate status and related information (such as, expiry date) on storage arrays in different scenarios.
-   The "**show certificate general**" command is used to query information about all certificates.
-   The "**show certificate general** type=?" command is used to query information about certificates in a specified scenario.
-   The "**show certificate general** type=? detail=yes" command is used to query information about the certificate and CA certificate in a specified scenario.

##### Example

Query information about all certificates.

```text
admin:/>show certificate general

Type                         Status        Expire Time  Expiration Prewarning Time  CA Fingerprint                                               Use
--------------------------   ------------  -----------  --------------------------  -----------------------------------------------------------  ----
Domain Authentication        Valid         2035-10-19   29                          BE:C4:A3:62:41:37:DA:28:6A:47:3F:8E:40:56:6D:DC:C8:91:72:08  --
HyperMetro Arbitration       Valid         2025-06-05   30                          2F:73:81:36:78:77:BA:D4:8E:4D:01:36:E6:CA:F4:E4:39:63:04:21  --
HTTPS Protocol               Valid         2028-05-20   30                          --                                                           --
FTPS Protocol                Valid         2028-05-20   30                          --                                                           --
Syslog Authentication        Non-existent  --           30                          --                                                           --
Ntp Authentication           Non-existent  --           30                          --                                                           --
Call Home Authentication     Non-existent  --           30                          4E:B6:D5:78:49:9B:1C:CF:5F:58:1E:AD:56:BE:3D:9B:67:44:A5:E5  --
DeviceManager Authentication Non-existent  --           30                          --                                                           --
Email Authentication         Non-existent  --           30                          --                                                           --
Disk Authentication          Non-existent  --           30                          --                                                           --
SSO Authentication           Non-existent  --           30                          --                                                           --
OTP Email Authentication     Non-existent  --           30                          --                                                           --
Certification Authority      Non-existent  --           30                          --                                                           --
SmartContainer               Non-existent  --           30                          --                                                           --
```

Query information about certificates in a specified scenario.

```text
admin:/>show certificate general type=domain_authentication
Type                   Status  Expire Time  Expiration Prewarning Time  CA Fingerprint                                               Use
---------------------  ------  -----------  --------------------------  -----------------------------------------------------------  ----
Domain Authentication  Valid   2035-10-19   29                          BE:C4:A3:62:41:37:DA:28:6A:47:3F:8E:40:56:6D:DC:C8:91:72:08  --
```

Query detailed information about the certificate and CA certificate in a specified scenario.

```text
admin:/>show certificate general type=ntp_authentication detail=yes
Type                       : Ntp Authentication
Expiration Prewarning Time : 30
Status                     : Valid
Expire Time                : 2028-06-08
Issuer                     : C=CN,O=Huawei,OU=Storage,CN=Storage
Subject                    : C=CN,O=Huawei,OU=Storage,CN=2102351JNN10H4000007
Signature Algorithm        : SHA256RSA
Key Algorithm              : RSA
Key Length                 : 2048
Fingerprint                : 91:21:1D:9C:AA:8B:F2:59:AC:F9:7A:E7:6C:54:97:47:49:08:E1:FC
CA Status                  : Valid
CA Expire Time             : 2036-05-31
CA Issuer                  : C=CN,O=Huawei,OU=Storage,CN=Storage
CA Subject                 : C=CN,O=Huawei,OU=Storage,CN=Storage
CA Signature Algorithm     : SHA256RSA
CA Key Algorithm           : RSA
CA Key Length              : 2048
CA Fingerprint             : 15:D9:F4:0C:DF:41:A8:64:32:E0:9D:49:2F:0F:2E:BD:C1:05:F3:6A
Use                        : --
Enable Auto Update         : Yes
Auto Update Common Name    : Storage
Auto Update Valid Period   : 30 Year
Auto Update subjectAltName : Storage
```

##### System Response

The following table describes the parameter meanings.

| Parameter                  | Meaning                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type                       | Certificate type. The value can be key_management_center, domain_authentication, hypermetro_arbitration, https_protocol, ftps_protocol, syslog_authentication, ntp_authentication, call_home_authentication, devicemanager_authentication, email_authentication, disk_authentication, sso_authentication, OTP_email_authentication, certification_authority, file_service_domain_authentication, or SmartContainer. |
| Status                     | Certificate status. The value can be "Non-existent", "Valid", or "Invalid".                                                                                                                                                                                                                                                                                                                                         |
| Expire Time                | Expiry date of a certificate. "--" is displayed if the certificate does not exist.                                                                                                                                                                                                                                                                                                                                  |
| Expiration Prewarning Time | Certificate expiration warning days. The default value is 30 and the value ranges from 7 to 180.                                                                                                                                                                                                                                                                                                                    |
| CA Fingerprint             | CA certificate fingerprint information.                                                                                                                                                                                                                                                                                                                                                                             |
| Issuer                     | Certificate issuer information.                                                                                                                                                                                                                                                                                                                                                                                     |
| Subject                    | Certificate user information.                                                                                                                                                                                                                                                                                                                                                                                       |
| Signature Algorithm        | Certificate signature algorithm.                                                                                                                                                                                                                                                                                                                                                                                    |
| Key Algorithm              | Certificate key algorithm.                                                                                                                                                                                                                                                                                                                                                                                          |
| Key Length                 | Certificate key length.                                                                                                                                                                                                                                                                                                                                                                                             |
| Fingerprint                | Certificate fingerprint.                                                                                                                                                                                                                                                                                                                                                                                            |
| CA Status                  | CA certificate status.                                                                                                                                                                                                                                                                                                                                                                                              |
| CA Expire Time             | CA certificate expiry date.                                                                                                                                                                                                                                                                                                                                                                                         |
| CA Issuer                  | CA certificate issuer.                                                                                                                                                                                                                                                                                                                                                                                              |
| CA Subject                 | CA certificate user.                                                                                                                                                                                                                                                                                                                                                                                                |
| CA Signature Algorithm     | CA certificate signature algorithm.                                                                                                                                                                                                                                                                                                                                                                                 |
| CA Key Algorithm           | CA certificate key algorithm.                                                                                                                                                                                                                                                                                                                                                                                       |
| CA Key Length              | CA certificate key length.                                                                                                                                                                                                                                                                                                                                                                                          |
| Use                        | Use of a certificate.                                                                                                                                                                                                                                                                                                                                                                                               |
| Auto Update Valid Period   | Validity period of a certificate after it is automatically updated.                                                                                                                                                                                                                                                                                                                                                 |
| Enable Auto Update         | Whether automatic certificate update is enabled or disabled.                                                                                                                                                                                                                                                                                                                                                        |
| Auto Update SubjectAltName | subjectAltName field for automatic certificate update.                                                                                                                                                                                                                                                                                                                                                              |
| Auto Update Common Name    | common name field for automatic certificate update.                                                                                                                                                                                                                                                                                                                                                                 |
