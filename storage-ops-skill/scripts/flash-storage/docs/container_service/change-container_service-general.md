# change container_service general


##### Function

The **change container_service general** command is used to change the status of a container service.

##### Format

**change container_service general** status=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| status=? | Change the container service status. | The value can be: <br>"start": starts the container service.<br>"stop": stops the container service. |

##### Usage Guidelines

This command cannot be used in the following situations:

1\. Run the show container_service general command. If the value of Enabled is Off, the container is not activated.

2\. The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Start the container service.

```text
admin:/>change container_service general status=start
CAUTION: You are about to enable the container service. This operation takes about 10 minutes at most.
Suggestion: Before performing this operation, ensure that the license has been imported and the container service has been activated.
Do you wish to continue?(y/n)y
Start Container Service (--) in background.
Run the "show task general task_id=1" command to query the execution result.
```

Stop the container service.

```text
admin:/>change container_service general status=stop
DANGER: You are about to stop the container service. After this operation, the container service will be unavailable.
Suggestion: Before performing this operation, ensure that the containerized application has been stopped.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Stop Container Service (--) in background.
Run the "show task general task_id=1" command to query the execution result.
```

##### System Response

None
