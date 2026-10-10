# show service ndmp_tape


##### Function

The **show service ndmp_tape** command is used to query information about an NDMP tape library.

##### Format

**show service ndmp_tape** \[ controller=? \]

##### Parameters

| Parameter    | Description    | Value                                                                                                              |
|--------------|----------------|--------------------------------------------------------------------------------------------------------------------|
| controller=? | Controller ID. | The value is in the format of XA, XB, XC, or XD, where X is an integer starting from 0, for example, "0A" or "1C". |

##### Usage Guidelines

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query information about an NDMP tape library.

```text
admin:/>show service ndmp_tape controller=0A
Type          Path
------------  ------------
robot         /dev/tape/by-id/scsi-1ADIC_Scalar_100_5EQQE00217
tape          /dev/tape/by-id/scsi-1IBM_ULTRIUM-TD1_5EQQE00218-nst
tape          /dev/tape/by-id/scsi-1IBM_ULTRIUM-TD1_5EQQE00219-nst
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning                        |
|-----------|--------------------------------|
| Type      | Type of the tape library.      |
| Path      | Full path of the tape library. |
