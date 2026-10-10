# show container_application dynamic_config


##### Function

The **show container_application dynamic_config** command is used to query the configuration items that can be configured for deploying a chart package.

##### Format

**show container_application dynamic_config** app=? version=?

##### Parameters

| Parameter | Description          | Value                                                                                                                    |
|-----------|----------------------|--------------------------------------------------------------------------------------------------------------------------|
| app       | Application name.    | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-). |
| version   | Application version. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (\_), periods (.), and hyphens (-). |

##### Usage Guidelines

This command cannot be used in the following situations:

-   Run the show container_service general command. If the value of Enabled is Off, the container is not activated.
-   The container cannot be used during activation.

OceanStor Dorado 18000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Query the list of available application parameters.

```text
admin:/>show container_application dynamic_config app=cs version=8.1.1

Config Name           Config Value
-----------------     -----------------
repeat_times          1
repeat_times2         12
```

##### System Response

The following table describes the parameter meanings.

| Parameter    | Meaning                        |
|--------------|--------------------------------|
| Config Name  | Configuration item name.       |
| Config Value | Value of a configuration item. |
