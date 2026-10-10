# clear identity_mapping cache


##### Function

The **clear identity_mapping cache** command is used to clear user mapping caches.

##### Format

**clear identity_mapping cache** controller=? { rule_id=? }

##### Parameters

| Parameter    | Description      | Value                                                                                                                                                                        |
|--------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| controller=? | Controller ID.   | The value format can be "XA", "XB", "XC" and "XD", where the value of X can be an integer ranging from 0 to 3. To obtain the value, run the show controller general command. |
| rule_id=?    | Mapping rule ID. | The value is an integer ranging from 1 to 18446744073709551615.                                                                                                              |

##### Usage Guidelines

None

##### Example

Clear mapping caches of all users in the specified controller.

```text
developer:/>clear identity_mapping cache controller=0A
Command executed successfully.
```

Clear mapping caches of the specified users in the specified controller.

```text
developer:/>clear identity_mapping cache controller=0A rule_id=100001
Command executed successfully.
```

##### System Response

None
