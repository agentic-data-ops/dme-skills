# add container_service general


##### Function

The **add container_service general** command is used to add container service resources.

##### Format

**add container_service general** node_list=?

##### Parameters

| Parameter   | Description               | Value                                             |
|-------------|---------------------------|---------------------------------------------------|
| node_list=? | List of controller nodes. | Use commas (,) to separate controller node names. |

##### Usage Guidelines

This command cannot be used in the following situations:

1\. Run the show container_service general command. If the value of Enabled is Off, the container is not activated.

2\. The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Select the 0A and 0B controller nodes.

```text
admin:/>add container_service general node_list=0A,0B
Add Node to Container Service (--) in background.
Run the "show task general task_id=1" command to query the execution result.
```

##### System Response

None
