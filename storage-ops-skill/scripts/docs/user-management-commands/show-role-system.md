# show role system


##### Function

The **show role system** command is used to query information about system roles.

##### Format

**show role system** \[ id=? \]

##### Parameters

| Parameter | Description | Value                                                                                                                                                                                                                                      |
|-----------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id=?      | Role ID.    | The value must be an integer from 1 to 1023. To obtain the value, run the "**show role system**" command without parameters. |

##### Usage Guidelines

-   Run the "**show role system**" command to query information about all system roles.
-   Run the "**show role system** id=?" command to query information about a specific system role.

##### Example

Query information about all system roles.

```text
admin:/>show role system

ID    Name                          Type        Group
----  ----------------------------  ----------  ----------
1     Super administrator           built-in      system
2     Administrator                 built-in      system
3     Security administrator        built-in      system
5     Network administrator         built-in      system
6     SAN resource administrator    built-in      system
8     Data protection administrator built-in      system
9     Backup administrator          built-in      system
11    Empty role                    built-in      system
12    Remote device administrator   built-in      system
65    testrole                      user-defined  system
```

Query information about the system role whose ID is "65".

```text
admin:/>show role system id=65

ID          : 65
Name        : testrole
Type        : user-defined
Group       : system
Description : test_description
Permit List : lun:lun_W,lun_R
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning                                               |
|-------------|-------------------------------------------------------|
| ID          | Role ID.                                              |
| Name        | Role name.                                            |
| Type        | Role type. The value can be built-in or user-defined. |
| Group       | Owning group of a role.                               |
| Description | Role description.                                     |
| Permit List | Role permission list.                                 |
