# show hyper_metro_consistency_group pair


##### Function

The **show hyper_metro_consistency_group pair** command is used to query the pairs in a HyperMetro consistency group.

##### Format

**show hyper_metro_consistency_group pair** consistency_group_id=?

##### Parameters

| Parameter              | Description                             | Value                                                                                                |
|------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------|
| consistency_group_id=? | ID of the HyperMetro consistency group. | Run the "show hyper_metro_consistency_group general" command without parameters to obtain the value. |

##### Usage Guidelines

None

##### Example

Query the pairs in the HyperMetro consistency group whose ID is "21009017acb3845f0000000100000000".

```text
admin:/>show hyper_metro_consistency_group pair consistency_group_id=21009017acb3845f0000000100000000

ID  Health   Running    Type    Role
Status   Status

--  ------   -------    -----   ------

1   Normal   Normal     LUN     Preferred

2   Normal   Normal     LUN     Preferred
```

##### System Response

The following table describes the parameter meanings.

| Parameter      | Meaning                                                                                    |
|----------------|--------------------------------------------------------------------------------------------|
| ID             | ID of the HyperMetro pair.                                                                 |
| Health Status  | Health status of a pair: NORMAL or FAULT.                                                  |
| Running Status | Running status: Normal, Synchronizing, To Be Synchronized, Pause, Forced Start or Invalid. |
| Type           | Resource type: LUN or File System.                                                         |
| Role           | Whether the end is the preferred end.                                                      |
