# change tgt_switch map_foolproof


##### Function

The **change tgt_switch map_foolproof** command is used to enable or disable the function of checking whether an operation object has I/Os during mapping removal.

##### Format

**change tgt_switch map_foolproof** switch=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| switch=? | After this function is enabled, the system checks whether the operation object has read and write I/Os when removing a mapping. | The value can be "on" or "off", where: <br>"on": enables the function.<br>"off": disables the function. |

##### Usage Guidelines

-   After this function is enabled, the system checks whether the operation object has I/Os when removing mappings.
-   After this function is enabled, mappings may fail to be removed. In this case, you can disable this function.

##### Example

Enable the mapping foolproof function.

```text
admin:/>change tgt_switch map_foolproof switch=on
Command executed successfully.
```

##### System Response

None
