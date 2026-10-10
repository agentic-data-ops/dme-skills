# add kmc test


##### Function

The **add kmc test** command is used to test the connectivity of an external key management server.

##### Format

**add kmc test** port=? { kmc_server_ip=? \| kmc_server_domain_name=? } \[ type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| kmc_server_ip=? | IP address of the external key management server. | - |
| kmc_server_domain_name=? | Domain name of the external key management server. | The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| port=? | Port number of the external key management server. | The value ranges from 1 to 65535. |
| type | Type of the external key management server. | The value can be "Thales_kmip", "SafeNet_kmip", "Sansec_kmip", or "Utimaco_kmip". The default value is "Thales_kmip". The parameters are described as follows: <br>"Thales_kmip": Thales external key management server.<br>"SafeNet_kmip": SafeNet external key management server.<br>"Sansec_kmip": Sansec external key management server.<br>"Utimaco_kmip": Utimaco external key management server. |

##### Usage Guidelines

-   Parameters "kmc_server_ip" and "kmc_server_domain_name" are mutually exclusive.

##### Example

Test the connectivity of an external key management server.

```text
admin:/>add kmc test port=5696 kmc_server_ip=192.168.8.211 type=Thales_kmip
Command executed successfully.
```

##### System Response

None
