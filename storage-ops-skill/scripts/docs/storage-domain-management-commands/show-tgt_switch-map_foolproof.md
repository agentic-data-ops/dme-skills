# show tgt_switch map_foolproof


##### Function

The **show tgt_switch map_foolproof** command is used to query whether the the function of checking whether an operation object has I/Os during mapping removal is enabled or disabled.

##### Format

**show tgt_switch map_foolproof**

##### Parameters

None

##### Usage Guidelines

If the returned value is "on", the function is enabled. If the return value is "off", the function is disabled.

##### Example

Query whether the the function of checking whether an operation object has I/Os during mapping removal is enabled or disabled

```text
admin:/>show tgt_switch map_foolproof
Switch Type   : Mapping Foolproof
Switch Status : On

```

##### System Response

The following table describes the parameter meanings.

| Parameter     | Meaning                                          |
|---------------|--------------------------------------------------|
| Switch Type   | Function status.                                 |
| Switch Status | Function status. The value can be "on" or "off". |
