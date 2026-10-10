# create initiator fc


##### Function

The **create initiator fc** command is used to create Fibre Channel initiators. You can enable hosts to access storage resources of the storage system using created initiators.

##### Format

**create initiator fc** wwn=? \[ alias=? \| host_id=? \] \[ multipath_type=? \[ failover_mode=? \[ special_mode_type=? \] \] \[ path_type=? \] \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| wwn=? | World Wide Name (WWN) of a Fibre Channel initiator. | It is a hexadecimal value that contains 16 characters comprised of uppercase letters A to F, lowercase letters a to f, or digits 0 to 9, but cannot all be 0, F, or f. |
| alias=? | Alias of an initiator. | The value contains 1 to 31 characters including digits, letters, underscores (_), periods (.), and hyphens (-). |
| host_id=? | ID of a host. | To obtain the value, run "show host general". |
| multipath_type=? | Multipathing mode. | The value can be "default" or "third-party", where: <br>default: Huawei multipathing software is used.<br>third-party: Third-party multipathing software is used.<br> The default value is "default". |
| failover_mode=? | Failover mode of the initiator. | The value can be "old_alua", "common_alua", "no_alua", or "special_mode", where: <br>old_alua: ALUA of an earlier version.<br>common_alua: common ALUA.<br>no_alua: ALUA not used.<br>special_mode: special mode.<br> The default value is "common_alua". |
| path_type=? | Path type of the initiator. | The value can be "non-optimized" or "optimized", where: <br>optimized: optimized path.<br>non-optimized: non-optimized path.<br> The default value is "optimized". |
| special_mode_type=? | Special mode type of the initiator. | The value can be "mode0", "mode1", "mode2", and "mode3", where: <br>mode0: special mode 0.<br>mode1: special mode 1.<br>mode2: special mode 2.<br>mode3: special mode 3. |

##### Usage Guidelines

None.

##### Example

Create the Fibre Channel initiator whose WWN is "455856585f654578".

```text
admin:/>create initiator fc wwn=455856585f654578
Command executed successfully.
```

##### System Response

None
