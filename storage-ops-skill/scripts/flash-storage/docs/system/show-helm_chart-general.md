# show helm_chart general


##### Function

The **show helm_chart general** command is used to query information about the application chart packages imported by a user.

##### Format

**show helm_chart general**

##### Parameters

None

##### Usage Guidelines

None.

##### Example

Query information about the application chart packages imported to the storage system.

```text
admin:/>show helm_chart general

Application           Version     Upload Time
--------------------  ----------  -------------------
OceanProtect          8.1.0       2020-09-27 15:00:49
OceanProtect          8.1.1       2020-09-28 15:00:49
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                                                                      |
|-------------|------------------------------------------------------------------------------|
| Application | Application name.                                                            |
| Version     | Version of the application chart package.                                    |
| Upload Time | Time when the application chart package is uploaded to the image repository. |
