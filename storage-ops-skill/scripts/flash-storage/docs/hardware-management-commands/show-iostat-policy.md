# show iostat policy


##### Function

**show iostat policy** command is used to view the I/O statistical policy.

##### Format

**show iostat policy**

##### Parameters

None

##### Usage Guidelines

None

##### Example

View the I/O statistical policy.

```text
admin:/>show iostat policy

Forward seek range  :   0,  20,  40,  60,  80
Backward seek range :   0,  20,  40,  60,  80
Read io size range  :   0,  64, 128, 256, 512
Write io size range :   0,  64, 128, 256, 512
Read io size        :   2,   4,   8,  16,  32,  64, 128, 256, 512
Write io size       :   2,   4,   8,  16,  32,  64, 128, 256, 512
Io delay range      :  50, 100, 200, 400, 800
```

##### System Response

The following table describes the parameter meanings.

| Parameter           | Meaning              |
|---------------------|----------------------|
| Forward seek range  | Forward seek range.  |
| Backward seek range | Backward seek range. |
| Read io size range  | Read I/O range.      |
| Write io size range | Write I/O range.     |
| Read io size        | Read I/O size.       |
| Write io size       | Write I/O size.      |
| Io delay range      | I/O latency range.   |
