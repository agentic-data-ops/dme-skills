# show identity_mapping rule


##### Function

The **show identity_mapping rule** command is used to check the identity_mapping rule.

##### Format

**show identity_mapping rule** { id=? }

##### Parameters

| Parameter | Description      | Value                                                           |
|-----------|------------------|-----------------------------------------------------------------|
| id=?      | Mapping rule ID. | The value is an integer ranging from 1 to 18446744073709551615. |

##### Usage Guidelines

None

##### Example

Check the identity_mapping rule of the specified ID.

```text
admin:/>show identity_mapping rule id=1
ID From Identity To Identity Mapping Type    Priority
-- ------------- ----------- --------------- --------
1  windowsuser   unixuser    Windows_to_Unix 10
```

Check all identity_mapping rules.

```text
admin:/>show identity_mapping rule
ID From Identity To Identity Mapping Type    Priority
-- ------------- ----------- --------------- --------
1  windowsuser   unixuser    Windows_to_Unix 10
2  winuser2      unixuser2   Windows_to_Unix 10
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                    |
|---------------|----------------------------|
| ID            | Mapping rule ID.           |
| From Identity | Pre-mapping identifier.    |
| To Identity   | Post-mapping identifier.   |
| Mapping Type  | Mapping type.              |
| Priority      | Priority of mapping rules. |
