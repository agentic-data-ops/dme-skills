# delete mapping_view


##### Function

The **delete mapping_view** command is used to delete mapping views.

##### Format

**delete mapping_view** { mapping_view_id=? \| mapping_view_name=? }

##### Parameters

| Parameter           | Description             | Value                                                 |
|---------------------|-------------------------|-------------------------------------------------------|
| mapping_view_id=?   | ID of a mapping view.   | To obtain the value, run "show mapping_view general". |
| mapping_view_name=? | Name of a mapping view. | To obtain the value, run "show mapping_view general". |

##### Usage Guidelines

-   Before running this command, ensure that the selected mapping view is exactly the one you want to delete and that no service associated with the hosts in the mapping view is running.
-   Before deleting a mapping view, remove all the host groups, LUN groups, and port groups from the mapping view.

##### Example

Delete the mapping view whose ID is "1".

```text
admin:/>delete mapping_view mapping_view_id=1
WARING: You are about to delete mapping view. This operation cannot be undone. This operation will delete the information about the mapping view from the system.
Suggestion: Before performing this operation, ensure that the selected mapping view is no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the mapping view whose name is "map01".

```text
admin:/>delete mapping_view mapping_view_name=map01
WARING: You are about to delete mapping view. This operation cannot be undone. This operation will delete the information about the mapping view from the system.
Suggestion: Before performing this operation, ensure that the selected mapping view is no longer necessary.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
