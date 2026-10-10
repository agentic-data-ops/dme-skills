# poweroff interface_module


##### Function

The **poweroff interface_module** command is used to power off a specific interface module.

##### Format

**poweroff interface_module** interface_module_id=?

##### Parameters

| Parameter             | Description                | Value                                                               |
|-----------------------|----------------------------|---------------------------------------------------------------------|
| interface_module_id=? | ID of an interface module. | To obtain the value, run "show interface_module" without parameter. |

##### Usage Guidelines

Before you perform this operation, ensure that the services of all ports on the interface module are stopped.

##### Example

To power off the interface module whose ID is CTE0.SMM0, run the following command. The ID and output vary depending on a specific product.

```text
admin:/>poweroff interface_module interface_module_id=CTE0.SMM0
DANGER: You are about to power off the interface module.
This operation will cause that the services of all ports on the interface module are interrupted.
Suggestion: Before you perform this operation, ensure that the services of all ports on the interface module are stopped.
Have you read danger alert message carefully?(y/n)Y
Are you sure you really want to perform the operation?(y/n)Y
Command executed successfully.
```

##### System Response

None
