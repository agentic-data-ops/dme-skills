# change lun_migration_pause


##### Function

The **change lun_migration_pause** command is used to pause the LUN migration.

##### Format

**change lun_migration_pause** source_lun_id=?

##### Parameters

| Parameter       | Description                                                                                                                                                                                        | Value                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| source_lun_id=? | ID of a source LUN. This parameter is supported in OceanStor Dorado 18000 V6, Dorado 18000 V6, Dorado 18000 V6, Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems. | Run the "show lun general" command without parameters to obtain the value. |

##### Usage Guidelines

None

##### Example

Pause the LUN migration.

```text
admin:/>change lun_migration_pause source_lun_id=0
Command executed successfully.
```

##### System Response

None
