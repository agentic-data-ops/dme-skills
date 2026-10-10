# delete container_application general


##### Function

The **delete container_application general** command is used to delete an application.

##### Format

**delete container_application general** name=?

##### Parameters

| Parameter | Description                             | Value                                                                                                                                                          |
|-----------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name      | Name of the application to be deployed. | The value contains 1 to 255 ASCII characters, including lowercase letters, digits, hyphens (-), and periods (.). It must start and end with a letter or digit. |

##### Usage Guidelines

This command cannot be used in the following situations:

-   Run the show container_service general command. If the value of Enabled is Off, the container is not activated.
-   The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Delete an application.

```text
admin:/>delete container_application general name=100p
DANGER: You are about to delete containerized application. After this operation, the containerized application will be deleted from the system, and the container service provided by the containerized application will be unavailable and cannot be restored.
Suggestion: Before performing this operation, ensure that the selected containerized application is correct and no longer needed.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
