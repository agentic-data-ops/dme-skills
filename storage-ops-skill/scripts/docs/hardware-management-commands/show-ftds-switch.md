# show ftds switch


##### Function

The **show ftds switch** command is used to check whether the Flow Tracing & Diagnosing System (FTDS) function is enabled.

##### Format

**show ftds switch**

##### Parameters

None

##### Usage Guidelines

Running this command checks whether the FTDS function is enabled. "On" indicates that the function is enabled. "Off" indicates that the function is disabled.

##### Example

Show the switch status of FTDS in guest view.

```text
admin:/>show ftds switch
Switch: On
Trace Switch: Off
Phase Switch: On
Delay Switch: On
Count Switch: On
```

Show the switch status of FTDS in developer view.

```text
developer:/>show ftds switch
Switch: On
Trace Switch: Off
Phase Switch: On
Delay Switch: On
Count Switch: On
Workload Switch: Off
```

##### System Response

The following table describes the parameter meanings.

| Parameter       | Meaning                     |
|-----------------|-----------------------------|
| Switch          | Main switch.                |
| Trace Switch    | Tracing switch.             |
| Phase Switch    | Phase switch.               |
| Delay Switch    | Delay switch.               |
| Count Switch    | Count switch.               |
| Workload Switch | Workload collection switch. |
