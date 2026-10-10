# change identity_mapping config


##### Function

The **change identity_mapping config** command is used to change user mapping configurations.

##### Format

**change identity_mapping config** { provider=? \| idmu_base_dn=? \| idmu_timeout=? \| idmu_win_objectclass=? \| idmu_unix_objectclass=? \| default_windows_user=? \| default_unix_user=? \| same_name_switch=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| provider=? | Provider of user mapping rules. | The value can be "NOT_SUPPORT", "LOCAL", "IDMU", "IDMU_LOCAL", and "LOCAL_IDMU". The default value is "NOT_SUPPORT". Where: <br>NOT_SUPPORT: User mappings are not supported.<br>Local: Mapping provider is local.<br>IDMU: Mapping provider is IDMU.<br>IDMU_LOCAL: Mapping provider is IDMU and local.<br>LOCAL_IDMU: Mapping provider is local and IDMU. |
| idmu_base_dn=? | Base DN queried by the IDMU. | The value is a string containing 1 to 255 characters. |
| idmu_timeout=? | Timeout of IDMU query. | The value ranges from 5 to 120 seconds. The default value is 15. |
| idmu_win_objectclass=? | objectclass used by the Windows user searched by the IDMU. | The value is a string containing 1 to 255 characters. |
| idmu_unix_objectclass=? | objectclass used by the Unix user searched by the IDMU. | The value is a string containing 1 to 255 characters. |
| default_windows_user=? | Default windows user. | The value is a string containing 1 to 256 characters. |
| default_unix_user=? | Default unix user. | The value is a string containing 1 to 256 characters. |
| same_name_switch=? | The switch of use a mapping with the same name. | The value can be on or off. |

##### Usage Guidelines

None

##### Example

Change the mapping rule provider.

```text
admin:/>change identity_mapping config provider=LOCAL
Command executed successfully.
```

##### System Response

None
