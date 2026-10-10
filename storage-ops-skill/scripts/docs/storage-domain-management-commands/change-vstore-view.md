# change vstore view


##### Function

The **change vstore view** command is used to enter the view of a vStore.

##### Format

**change vstore view** { id=? \| name=? }

##### Parameters

| Parameter | Description  | Value                                                                                                          |
|-----------|--------------|----------------------------------------------------------------------------------------------------------------|
| id=?      | vStore ID.   | The value ranges from 0 to 1023. To obtain the value, run the "show vstore" command without parameters.        |
| name=?    | vStore name. | The value contains 1 to 256 characters. To obtain the value, run the "show vstore" command without parameters. |

##### Usage Guidelines

Specify either "id" or "name".

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Enter the view of the vStore whose ID is "11".

```text
admin:/>change vstore view id=11
Command executed successfully.
```

Enter the view of the vStore whose name is "test".

```text
admin:/>change vstore view name=test
Command executed successfully.
admin@test:/>
```

##### System Response

None
