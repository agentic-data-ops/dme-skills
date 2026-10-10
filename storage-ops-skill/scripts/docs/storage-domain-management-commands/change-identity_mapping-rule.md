# change identity_mapping rule


##### Function

The **change identity_mapping rule** command is used to change user mapping rules.

##### Format

**change identity_mapping rule** id = ? { from_identity=? \| to_identity=? \| mapping_type=? \| priority=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| id=? | Mapping rule ID. | The value is an integer ranging from 1 to 18446744073709551615. |
| from_identity=? | Pre-mapping identifier. | The * wildcard character is supported, but the ** is not. The value is a string containing 1 to 256 characters. The value cannot contain (/), (][), (:), (;), (|), (=), (,), (+), (?), (<>), (@), ("), and control characters. The last character cannot be (.). |
| to_identity=? | Post-mapping identifier. | The value is a string containing 1 to 256 characters. The value cannot contain (/), (][), (:), (;), (|), (=), (,), (+), (*), (?), (<>), (@), ("), and control characters. The last character cannot be (.). |
| mapping_type=? | Mapping type. | The value can be "Windows_to_Unix" and "Unix_to_Windows". Where: <br>Windows_to_Unix: map a Windows user as a Unix user.<br>Unix_to_Windows: map a Unix user as a Windows user. |
| priority=? | Priority of mapping rules. | The value ranges from 1 to 32. |

##### Usage Guidelines

None

##### Example

Change user mapping rules.

```text
admin:/>change identity_mapping rule id=1 from_identity=windowsusermodify

Command executed successfully.
```

##### System Response

None
