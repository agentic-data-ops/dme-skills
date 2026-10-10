# change lun_migration_split consistency


##### Function

The **change lun_migration_split consistency** command is used to split LUN migration tasks.

##### Format

**change lun_migration_split consistency** source_lun_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| source_lun_id_list=? | IDs of source LUNs. | To obtain the value, run "show lun_migration general". To split multiple source LUNs in a batch, separate the IDs of those LUNs by commas (,), or separate ID ranges by hyphens (-), such as: "0, 5-8". A maximum of 2048 source LUNs are allowed to split once. |

##### Usage Guidelines

None

##### Example

Split the LUN migration tasks whose source LUN IDs are "3" and "4".

```text
admin:/>change lun_migration_split consistency source_lun_id_list=3,4
CAUTION: You are about to split LUN migrations. Only source LUNs can be read and written after splitting.
Suggestion: Before performing this operation, ensure that the current service load is light.
Do you wish to continue?(y/n)y
Command executed successfully.
```

##### System Response

None
