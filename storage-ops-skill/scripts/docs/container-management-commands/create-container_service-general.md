# create container_service general


##### Function

The **create container_service general** command is used to create container service resources.

##### Format

**create container_service general** node_list=? image_repository_pool_id=? application_pool_id_list=? \[ compression_enabled=? \] \[ dedup_enabled=? \]

**create container_service general** node_list=? image_repository_pool_name=? application_pool_name_list=? \[ compression_enabled=? \] \[ dedup_enabled=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| node_list=? | Node ID of a controller. | If the value is set to all, it indicates all controller nodes.<br>If the value is not set to all, multiple controller nodes are separated by commas (,) and the primary controller node must be included. |
| image_repository_pool_id=? | ID of the container image storage pool. | You can run the "show storage_pool general" command to obtain the value. |
| application_pool_id_list=? | ID list of container application storage pools. | Use commas (,) to separate multiple IDs. |
| image_repository_pool_name=? | Name of a container image storage pool. | Name of a container image storage pool. |
| application_pool_name_list=? | Name list of container application storage pools. | Use commas (,) to separate container application storage pool names. |
| compression_enabled | Whether to enable compression for the mirror LUN. | The value can be "yes" or "no", where: <br>"yes": compression is enabled for mirror LUNs.<br>"no": compression is disabled for mirror LUNs. |
| dedup_enabled | Whether to enable or disable deduplication for a mirror LUN. | The value can be "yes" or "no", where: <br>"yes": Data deduplication is enabled for mirror LUNs.<br>"no": Data deduplication is disabled for mirror LUNs. |

##### Usage Guidelines

This command cannot be used in the following situations:

-   Run the show container_service general command. If the value of Enabled is Off, the container is not activated.
-   The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Create container resources for controllers 0A and 0B.

```text
admin:/>create container_service general node_list=0A,0B image_repository_pool_id=0 application_pool_id_list=1,2
Deploy Container Service (--) in background.
Run the "show task general task_id=1" command to query the execution result.
```

Create container resources for controllers 0A and 0B.

```text
admin:/>create container_service general node_list=0A,0B image_repository_pool_name=storage1 application_pool_name_list=app1,app2
Deploy Container Service (--) in background.
Run the "show task general task_id=1" command to query the execution result.
```

Create container resources for all controllers.

```text
admin:/>create container_service general node_list=all image_repository_pool_name=storage1 application_pool_name_list=app1,app2
Deploy Container Service (--) in background.
Run the "show task general task_id=1" command to query the execution result.
```

Create container resources for controllers 0A and 0B.

```text
admin:/>create container_service general node_list=0A,0B image_repository_pool_id=0 application_pool_id_list=1,2 compression_enabled=yes dedup_enabled=yes
Deploy Container Service (--) in background.
Run the "show task general task_id=1" command to query the execution result.
```

##### System Response

None
