# change container_application view


##### Function

The **change container_application view** command is used to enter the container OS.

##### Format

**change container_application view** pod_name=? namespace=?

##### Parameters

| Parameter   | Description            | Value                                                                                          |
|-------------|------------------------|------------------------------------------------------------------------------------------------|
| pod_name=?  | Pod name.              | The value contains 1 to 255 ASCII characters, including digits, letters, and underscores (\_). |
| namespace=? | Application namespace. | The value contains 1 to 255 ASCII characters, including digits, letters, and underscores (\_). |

##### Usage Guidelines

This command cannot be used in the following situations:

-   Run the show container_service general command. If the value of Enabled is Off, the container is not activated.
-   The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Log in to the container OS.

```text
admin:/>change container_application view pod_name=ftp-pod-0 namespace=ftp
/etc/ftp/conf #
```

##### System Response

None
