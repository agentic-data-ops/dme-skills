# change system description


##### Function

The **change system description** command is used to change the storage system's description.

##### Format

**change system description** description=?

##### Parameters

| Parameter     | Description                                   | Value                                                                                                                                                                                                                                                                                                                                   |
|---------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| description=? | An updated description of the storage system. | The value contains 1 to 255 characters, only including letters, digits, spaces, and special characters (!\\"#&%$'()\*+-.;\<=\>?@\[\]^\_\`{\|}\~,/:). On the CLI, the following characters need to be represented with escape sequences: "\\\|" indicates "\|", "\\\\" indicates "\\", "\\q" indicates "?", and "\\s" indicates a space. |

##### Usage Guidelines

None

##### Example

Change the description of the storage system to newsystem.

```text
admin:/>change system description description=newsystem
Command executed successfully.
```

##### System Response

None
