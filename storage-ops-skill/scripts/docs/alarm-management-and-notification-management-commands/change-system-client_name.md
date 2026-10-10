# change system client_name


##### Function

The **change system client_name** command is used to modify the address information about the storage system maintenance terminal.

##### Format

**change system client_name** client_name=?

##### Parameters

| Parameter     | Description                                                      | Value                                                                         |
|---------------|------------------------------------------------------------------|-------------------------------------------------------------------------------|
| client_name=? | Address information about a storage system maintenance terminal. | The value contains 1 to 511 characters, excluding single quotation marks ('). |

##### Usage Guidelines

None.

##### Example

Changing the address of the storage system maintenance terminal to CDHW.

```text
admin:/>change system client_name client_name=CDHW
Command executed successfully.
```

##### System Response

None
