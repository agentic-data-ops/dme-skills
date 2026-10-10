# change interface_module


##### Function

The "**change interface_module**" command is used to configure an interface module mode.

##### Format

**change interface_module** id=? usage_type=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| id | ID of an interface module. | To obtain the value, run "show interface_module" without parameters. |
| usage_type | Usage mode of the interface module. | The value can be"storage","container_front_end", or "container_back_end", where: <br>"container_clear": array mode.<br>"container_front_end": front-end container mode.<br>"container_back_end": back-end container mode. |

##### Usage Guidelines

-   Before performing this operation, ensure that the services of all ports on the interface module are stopped.
-   After performing this operation, the interface module will only be used for container network communication.

##### Example

Configure the usage mode of interface module "CTE0.A.IOM5" to "container_back_end".

```text

admin:/>change interface_module id=CTE0.A.IOM5 usage_type=container_back_end

DANGER: You are about to change the mode of the interface module.
This operation may cause that the services of all ports on the interface module are interrupted.
Suggestion:
1. Before you perform this operation, ensure that the services of all ports on the interface module are stopped.
2. After performing this operation, the interface module can only be used for network communication of corresponding mode.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
