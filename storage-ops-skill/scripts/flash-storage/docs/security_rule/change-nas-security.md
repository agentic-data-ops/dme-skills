# change nas security


##### Function

The **change nas security** command is used to modify the NAS security policy of a vStore.

##### Format

**change nas security** ntlm_level=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| ntlm_level=? | 0 to The server verifies the LM, NTLM, and NTLMv2 identities.<br>The server rejects the LM identity authentication and accepts the NTLM and NTLMv2 identity authentication.<br>The server rejects the LM and NTLM identity authentication and accepts only the NTLMv2 identity authentication.<br>Disable NTLM identity authentication. | The value of this parameter ranges from 0 to 6. |

##### Usage Guidelines

None

##### Example

Change the NTLM authentication level.

```text
admin:/>change nas security ntlm_level=2
Command executed successfully.
```

##### System Response

None
