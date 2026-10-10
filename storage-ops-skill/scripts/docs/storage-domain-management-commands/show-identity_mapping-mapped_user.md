# show identity_mapping mapped_user


##### Function

The **show identity_mapping mapped_user** command is used to check whether the user can be found after a mapping.

##### Format

**show identity_mapping mapped_user** to_identity=? mapping_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| to_identity=? | Post-mapping identifier. | The value is a string containing 1 to 256 characters. The value cannot contain (/), (][), (:), (;), (|), (=), (,), (+), (*), (?), (<>), (@), ("), and control characters. The last character cannot be (.). |
| mapping_type=? | Mapping type. | The value can be "Windows_to_Unix" and "Unix_to_Windows". Where: <br>Windows_to_Unix: map a Windows user as a Unix user.<br>Unix_to_Windows: map a Unix user as a Windows user. |

##### Usage Guidelines

None

##### Example

Check whether the user can be found after the mapping.

```text
admin:/>show idengtity_mapping mapped_user to_identity=user1 mapping_type=Windows_to_Unix
User Can Find: Yes
```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                        |
|---------------|--------------------------------|
| User Can Find | Whether the user can be found. |
