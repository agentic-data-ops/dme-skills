# add kmc general


##### Function

The **add kmc general** command is used to add the configuration of an external key management server.

##### Format

**add kmc general** type=? port=? { kmc_server_ip=? \| kmc_server_domain_name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| kmc_server_ip=? | IP address of the external key management server. | - |
| kmc_server_domain_name=? | Domain name of the external key management server. | The domain name is a case-insensitive string of 1 to 255 characters, including letters, digits and hyphens (-). Domain names at various levels are separated by periods (.). Hyphens (-) cannot be the start or end of the domain name. |
| type=? | Type of the external key management server. | The value can be "Thales_kmip", "SafeNet_kmip", "Sansec_kmip", or "Utimaco_kmip", where: <br>"Thales_kmip": Thales external key management server.<br>"SafeNet_kmip": SafeNet external key management server.<br>"Sansec_kmip": Sansec external key management server.<br>"Utimaco_kmip": Utimaco external key management server. |
| port=? | Port number of the external key management server. | The value ranges from 1 to 65535. |

##### Usage Guidelines

-   Parameters "kmc_server_ip" and "kmc_server_domain_name" are mutually exclusive.

##### Example

Add a configuration of the external key management server.

```text
admin:/>add kmc general type=Thales_kmip port=5696 kmc_server_ip=192.168.20.10
Command executed successfully.
```

##### System Response

None
