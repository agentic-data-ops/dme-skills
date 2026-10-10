# change ftds level


##### Function

The **change ftds level** command is used to set the trace level of Flow Tracing & Diagnosing System (FTDS) function. The level includes subsystem level, key module level, module level, and debug level.

##### Format

**change ftds level** level=?

##### Parameters

| Parameter | Description          | Value                                                             |
|-----------|----------------------|-------------------------------------------------------------------|
| level=?   | Trace level of FTDS. | The value can be "Subsystem", "Key_module", "Module", or "Debug". |

##### Usage Guidelines

Running this command sets the trace level of FTDS.

##### Example

Set the trace level of FTDS.

```text
admin:/>change ftds level level=Module
Command executed successfully.
```

##### System Response

None
