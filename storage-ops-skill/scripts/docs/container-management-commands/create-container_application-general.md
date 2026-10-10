# create container_application general


##### Function

The **create container_application general** command is used to deploy an application.

##### Format

**create container_application general** app=? version=? \[ dynamic_config=? \| name=? \| namespace=? \| net_plane_name=? \| description=? \]

##### Parameters

| Parameter      | Description                             | Value                                                                                                                                                          |
|----------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app            | Application name.                       | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-).                                       |
| version        | Application version.                    | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-).                                       |
| dynamic_config | Application parameter.                  | The value contains 1 to 1024 ASCII characters, including digits letters \_.!#$%&'()\*+,-/:;\<=\>?@\[\]^{}\|\~.                                                 |
| description    | Application description.                | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-).                                       |
| name           | Name of the application to be deployed. | The value contains 1 to 255 ASCII characters, including lowercase letters, digits, hyphens (-), and periods (.). It must start and end with a letter or digit. |
| namespace      | Application namespace.                  | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-).                                       |
| net_plane_name | Network plane used by an application.   | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), commas (,), periods (.), hyphens (-), and colons (:).               |

##### Usage Guidelines

This command cannot be used in the following situations:

-   Run the show container_service general command. If the value of Enabled is Off, the container is not activated.
-   The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Create an application.

```text
admin:/>create container_application general app=app1 version=8.1.1 name=cs dynamic_config=s1=v1,s2=v2 namespace=dpa net_plane_name=p1,p2 description=appliction
Command executed successfully.
```

##### System Response

None
