# delete performance file


##### Function

The **delete performance file** command is used to delete historical performance statistical files.

##### Format

**delete performance file** file=?

##### Parameters

| Parameter | Description                                                                | Value                                             |
|-----------|----------------------------------------------------------------------------|---------------------------------------------------|
| file=?    | Name of a historical performance statistical file that you want to delete. | To obtain the value, run "show performance file". |

##### Usage Guidelines

None

##### Example

Delete historical performance statistical files of the "PerfData_XXXXX_SN_210235G6EDZ0B4000010_SP0_0\_20120917113610.tgz".

```text
admin:/>delete performance file file=PerfData_XXXXX_SN_210235G6EDZ0B4000010_SP0_0_20120917113610.tgz
WARNING: You are going to delete the performance statistics file. This operation permanently deletes the performance statistics file.
Suggestion: Before you perform this operation, ensure that you have selected the correct file to be deleted.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
