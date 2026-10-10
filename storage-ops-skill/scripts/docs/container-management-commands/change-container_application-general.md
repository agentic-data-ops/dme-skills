# change container_application general


##### Function

The **change container_application general** command is used to update an application.

##### Format

**change container_application general** name=? \[ app=? version=? \| namespace=? \| dynamic_config=? \| net_plane_name=? \| description=? \]

##### Parameters

| Parameter      | Description                             | Value                                                                                                                                                          |
|----------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name=?         | Name of the application to be deployed. | The value contains 1 to 255 ASCII characters, including lowercase letters, digits, hyphens (-), and periods (.). It must start and end with a letter or digit. |
| app=?          | Application name.                       | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-).                                       |
| version=?      | Application version.                    | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-).                                       |
| namespace=?    | Application namespace.                  | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-).                                       |
| dynamic_config | Application parameter.                  | The value contains 1 to 1024 ASCII characters, including digits letters \_.!#$%&'()\*+,-/:;\<=\>?@\[\]^{}\|\~.                                                 |
| net_plane_name | Network plane used by an application.   | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), commas (,), periods (.), hyphens (-), and colons (:).               |
| description    | Application description.                | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-).                                       |

##### Usage Guidelines

This command cannot be used in the following situations:

-   Run the show container_service general command. If the value of Enabled is Off, the container is not activated.
-   The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Update the application.

```text
admin:/>change container_application general name=cs app=app1 version=8.1.1 dynamic_config=s1=v1,s2=v2 namespace=dpa net_plane_name=p1,p2 description=appliction
DANGER: You are about to update containerized application. This operation will interrupt services provided by the containerized application during the update, and the services will be restored after the update is complete.
Suggestion: Before performing this operation, ensure that the preceding risk is acceptable.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
