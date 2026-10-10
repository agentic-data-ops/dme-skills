# show container_image general


##### Function

The **show container_image general** command is used to query information about application image packages imported by a user.

##### Format

**show container_image general**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

Query information about the application image packages imported to the storage system.

```text
admin:/>show container_image general

Application           Version     Upload Time          Size     Is Active
--------------------  ----------  -------------------  -------  ---------
OceanProtect          8.1.0       2020-09-27 15:00:49  1.5G     Yes
OceanProtect          8.1.1       2020-09-28 15:00:49  1.5G     No
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                                                                      |
|-------------|------------------------------------------------------------------------------|
| Application | Application name.                                                            |
| Version     | Version of the application image package.                                    |
| Upload Time | Time when the application image package is uploaded to the image repository. |
| Size        | Size of the application image package.                                       |
| Is Active   | Whether the image software package is in use.                                |
