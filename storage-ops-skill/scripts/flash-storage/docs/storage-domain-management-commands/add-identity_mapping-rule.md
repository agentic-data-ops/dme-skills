# add identity_mapping rule


##### Function

The **add identity_mapping rule** command is used to add user mapping rules.

##### Format

**add identity_mapping rule** from_identity=? to_identity=? mapping_type=? { priority=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| from_identity=? | Pre-mapping identifier. | The * wildcard character is supported, but the ** is not. The value is a string containing 1 to 256 characters. The value cannot contain (/), (][), (:), (;), (|), (=), (,), (+), (?), (<>), (@), ("), and control characters. The last character cannot be (.). |
| to_identity=? | Post-mapping identifier. | The value is a string containing 1 to 256 characters. The value cannot contain (/), (][), (:), (;), (|), (=), (,), (+), (*), (?), (<>), (@), ("), and control characters. The last character cannot be (.). |
| mapping_type=? | Mapping type. | The value can be "Windows_to_Unix" and "Unix_to_Windows". Where: 0. Windows_to_Unix: map a Windows user as a Unix user. 1. Unix_to_Windows: map a Unix user as a Windows user. |
| priority=? | Priority of mapping rules. | The value ranges from 1 to 32. The default value is 10. |

##### Usage Guidelines

None

##### Example

Add user mapping rules.

```text
admin:/>add identity_mapping rule from_identity=windowsuser to_identity=unixuser mapping_type=Windows_to_Unix priority=5
Command executed successfully.
```

##### System Response

None
