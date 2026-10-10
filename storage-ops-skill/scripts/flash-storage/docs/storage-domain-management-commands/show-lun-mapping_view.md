# show lun mapping_view


##### Function

The **show lun mapping_view** command is used to query information about a mapping view related to a specified LUN.

##### Format

**show lun mapping_view** { lun_id=? \| lun_name=? }

##### Parameters

| Parameter  | Description | Value                                        |
|------------|-------------|----------------------------------------------|
| lun_id=?   | LUN ID.     | To obtain the value, run "show lun general". |
| lun_name=? | LUN name.   | To obtain the value, run "show lun general". |

##### Usage Guidelines

None

##### Example

Query information about a mapping view related to LUN "0".

```text
admin:/>show lun mapping_view lun_id=0

Mapping View ID  Mapping View Name
---------------  -----------------
0                MappingTest
```

##### System Response

The following table describes the parameter meanings.

| Parameter         | Meaning                 |
|-------------------|-------------------------|
| Mapping View ID   | ID of a mapping view.   |
| Mapping View Name | Name of a mapping view. |
