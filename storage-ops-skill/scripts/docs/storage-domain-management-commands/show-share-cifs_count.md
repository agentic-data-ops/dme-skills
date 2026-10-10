# show share cifs_count


##### Function

The **show share cifs_count** command is used to query the number of CIFS shares.

##### Format

**show share cifs_count** \[ share_type=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| share_type | Share type. | The value can be "normal" or "homedir" or "all", where: <br>normal : normal CIFS share.<br>homedir : homedir CIFS share.<br>all : all CIFS share.<br> The default value is normal. |

##### Usage Guidelines

None

##### Example

Query the number of normal CIFS shares.

```text
admin:/>show share cifs_count
Number : 11
```

Query the number of all CIFS shares, including normal CIFS share and homedir CIFS share.

```text
admin:/>show share cifs_count share_type=all
Number : 43
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                |
|-----------|------------------------|
| Number    | Number of CIFS shares. |
