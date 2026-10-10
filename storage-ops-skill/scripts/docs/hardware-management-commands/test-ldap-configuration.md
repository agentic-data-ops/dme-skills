# test ldap configuration


##### Function

The **test ldap configuration** command is used to test LDAP server configuration information.

##### Format

**test ldap configuration** type=? base_dn=? bind_dn=? bind_password=? over_ssl=? \[ ip=? \] \[ port=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| type=? | Type of the LDAP server. | The value is case-insensitive and can be "LDAP" or "AD", where: <br>"LDAP": indicates the common OpenLDAP protocol.<br>"AD": indicates the Active Directory (AD) protocol. |
| base_dn=? | Basic distinguished name (DN). This parameter defines a start point for searching on an LDAP directory server. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| bind_dn=? | DN bound with an LDAP server. If anonymous binding is not available for an LDAP server, you must bind DNs before you can retrieve the information on users or user groups. | The value contains 1 to 255 characters. The value is in the format of cn=, ou=, dc=. |
| bind_password=? | Password for a bound DN. | The value contains 1 to 63 characters. |
| over_ssl=? | Whether to enable SSL communication for an LDAP server. | The value can be "yes" or "no", where: <br>"yes": The SSL function is used.<br>"no": The SSL function is not used.<br> The default value is "no". |
| ip=? | IP address of the LDAP server. | The IP address can be used to access the LDAP server. |
| port=? | Listening port number of LDAP. This parameter is optional. If this parameter is left blank, default LDAPS port 636 and default LDAP port 389 are used. | The value is an integer ranging from "1" to "65535". |

##### Usage Guidelines

The test will fail if you configure LDAP server information different from that on the server.

##### Example

Test LDAP server configuration information. LDAP server type: LDAP Base DN: dc=test,dc=com Bind DN: cn=Manager,dc=test,dc=com Bind password: 7654321 SSL encryption IP address: 10.123.123.123.

```text
admin:/>test ldap configuration type=LDAP base_dn=dc=test,dc=com bind_dn=cn=Manager,dc=test,dc=com bind_password=****** over_ssl=yes ip=10.123.123.123
Command executed successfully.
```

Test LDAP server configuration information. LDAP server type: LDAP Base DN: dc=test,dc=com Bind DN: cn=Manager,dc=test,dc=com Bind password: 7654321 SSL encryption IP address: 10.123.123.123 Port: 636.

```text
admin:/>test ldap configuration type=LDAP base_dn=dc=test,dc=com bind_dn=cn=Manager,dc=test,dc=com bind_password=****** over_ssl=yes ip=10.123.123.123 port=636
Command executed successfully.
```

##### System Response

None
