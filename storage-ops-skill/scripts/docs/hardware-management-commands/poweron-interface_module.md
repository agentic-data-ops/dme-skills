# poweron interface_module


##### Function

The **poweron interface_module** command is used to power on a specific interface module.

##### Format

**poweron interface_module** interface_module_id=?

##### Parameters

| Parameter             | Description                | Value                                                               |
|-----------------------|----------------------------|---------------------------------------------------------------------|
| interface_module_id=? | ID of an interface module. | To obtain the value, run "show interface_module" without parameter. |

##### Usage Guidelines

None

##### Example

Power on the interface module whose ID is "ENG0.A0". The ID and output vary depending on a specific product.

```text
admin:/>poweron interface_module interface_module_id=ENG0.A0
Command executed successfully.
```

##### System Response

None
