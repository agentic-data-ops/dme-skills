# show performance strategy


##### Function

The **show performance strategy** command is used to query existing performance statistical policies for the storage system.

##### Format

**show performance strategy**

##### Parameters

None

##### Usage Guidelines

None

##### Example

To query existing performance statistical policies for the storage system, run the following command:

```text
admin:/>show performance strategy

Sampling Interval(s)   : 60
Archive Enabled        : Yes
Archive Time(S)        : 60
Auto Stop              : Yes
Duration(days)         : 7
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                                                       |
|----------------------|---------------------------------------------------------------|
| Sampling Interval(s) | Real-time sampling interval.                                  |
| Archive Enabled      | Status of the historical sampling switch.                     |
| Archive Time(s)      | Historical sampling interval.                                 |
| Auto Stop            | Status of the switch for automatically stopping the sampling. |
| Duration(days)       | Sampling duration.                                            |
