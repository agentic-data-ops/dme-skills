# show auth_diagnose


##### Function

The **show auth_diagnose** command is used to query the cause of an authentication failure.

##### Format

**show auth_diagnose** general

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| controller | Controller ID. | The value format is XA, XB, XC, or XD. X is an integer ranging from [0,7]. You can run the "show controller general" command to obtain the value. |
| domain_type | Type of the domain controller. | The value can be "LOCAL", "AD", "LDAP", or "NIS". The parameters are described as follows: <br>"LOCAL": Local authentication failure information is queried.<br>"AD": AD domain authentication failure information is queried.<br>"LDAP": LDAP domain authentication failure information is queried.<br>"NIS": NIS domain authentication failure information is queried. |

##### Usage Guidelines

None

##### Example

Query the cause of an AD domain authentication failure.

```text
admin:/>show auth_diagnose general controller=0A domain_type=AD
Occur Time                 User Name    Error Code  Error Message
------------------------   ----------   ----------  ----------------------------------------
Wed May 12 21:21:53 2021   ad\aduser1   -5026       The storage has not join the ad domain.
Wed May 12 21:21:58 2021   ad53\adsdsd  -5041       The netlogon user has not exist.
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                                  |
|---------------|----------------------------------------------------------|
| Occur Time    | Time when an authentication failure occurs.              |
| User Name     | User name used in the case of an authentication failure. |
| Error Code    | Error code returned when the authentication fails.       |
| Error Message | Authentication failure error information.                |
