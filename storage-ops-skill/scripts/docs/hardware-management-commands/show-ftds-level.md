# show ftds level


##### Function

The **show ftds level** command is used to query the trace level of the Flow Tracing & Diagnosing System (FTDS) function.

##### Format

**show ftds level**

##### Parameters

None

##### Usage Guidelines

Running this command queries the trace level of FTDS. The level can be "Subsystem", "Key_module", "Module", or "Debug".

##### Example

Query the trace level of FTDS.

```text
admin:/>show ftds level
Trace Level: Module
```

##### System Response

The following table describes the parameter meanings.

| Parameter   | Meaning      |
|-------------|--------------|
| Trace Level | Trace level. |
