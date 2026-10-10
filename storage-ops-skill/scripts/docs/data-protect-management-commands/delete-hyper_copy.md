# delete hyper_copy


##### Function

The **delete hyper_copy** command is used to delete a HyperCopy pair.

##### Format

**delete hyper_copy** hyper_copy_id_list=?

##### Parameters

| Parameter          | Description        | Value                                               |
|--------------------|--------------------|-----------------------------------------------------|
| hyper_copy_id_list | HyperCopy pair ID. | To obtain the value, run "show hyper_copy general". |

##### Usage Guidelines

None

##### Example

Delete HyperCopy pair "1","7","8".

```text
admin:/>delete hyper_copy hyper_copy_id_list=1,7-8
WARNING: You are about to delete HyperCopy pair . The deletion is an irreversible operation. You must recreate a HyperCopy pair when you need it.
Suggestion: Before performing this operation, ensure that the operation and parameters are correct.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Delete HyperCopy 1 successfully.
Delete HyperCopy 7 successfully.
Delete HyperCopy 8 successfully.
```

##### System Response

None
