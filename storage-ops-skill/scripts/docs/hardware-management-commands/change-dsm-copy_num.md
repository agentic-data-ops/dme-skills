# change dsm copy_num


##### Function

The **change dsm copy_num** command is used to modify the number of DSM copies.

##### Format

**change dsm copy_num** num=?

##### Parameters

| Parameter | Description       | Value                |
|-----------|-------------------|----------------------|
| num=?     | Number of copies. | The value is 2 or 3. |

##### Usage Guidelines

Restriction:If HyperMetro-Inner has been configured, the number of DSM copies cannot be modified to 2.

##### Example

Modify the number of DSM copies to 3.

```text
developer:/>change dsm copy_num num=3
Command executed successfully.
```

##### System Response

None
