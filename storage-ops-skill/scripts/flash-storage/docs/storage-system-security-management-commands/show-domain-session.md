# show domain session


##### Function

The **show domain session** command is used to show session information between a storage device and an AD domain.

##### Format

**show domain session** \[ controller=? \]

##### Parameters

| Parameter    | Description    | Value                                                                                                                                                                        |
|--------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| controller=? | Controller ID. | The value format can be "XA", "XB", "XC" and "XD", where the value of X can be an integer ranging from 0 to 3. To obtain the value, run the show controller general command. |

##### Usage Guidelines

-   The **show domain session** command is executed to show session information between a storage device and an AD domain on the primary controller.
-   The **show domain session** controller=? command is executed to show session information between a storage device and an AD domain on a specified controller.

##### Example

Show session information between a storage device and an AD domain.

```text
developer:/>show domain session controller=0A
IP Address    :  10.46.36.62
Session Info  :  WIN-AG3HC2JB5OU:1:1:0
```

##### System Response

The following table describes the parameter meanings.

| Parameter    | Meaning                                                        |
|--------------|----------------------------------------------------------------|
| IP Address   | IP address of the domain controller.                           |
| Session Info | Session information between a storage device and an AD domain. |
