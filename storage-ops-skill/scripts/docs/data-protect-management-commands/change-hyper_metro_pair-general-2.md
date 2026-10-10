# change hyper_metro_pair general


##### Function

The **change hyper_metro_pair general** command is used to change HyperMetro pair attributes.

##### Format

**change hyper_metro_pair general** pair_id=? { recovery_policy=? \| synchronization_rate=? \| bandwidth=? \| isolation_switch=? \| isolation_threshold=? \| lock_mode=? \| write_secondary_timeout=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pair_id=? | ID of the HyperMetro pair. | Run the "show hyper_metro_pair general" command without any parameters to obtain the value. |
| recovery_policy=? | Recovery policy. | The value is "automatic" or "manual", where: <br>"automatic": automatic recovery policy. Data will be automatically synchronized after faults are rectified.<br>"manual": manual recovery policy.<br> Data needs to be manually synchronized after faults are rectified. |
| bandwidth=? | Bandwidth. | The value is from 1 to 1024, expressed in MB/s. |
| synchronization_rate=? | Synchronization rate. | The value is "Low", "Middle", "High", or "Highest", where: <br>"Low": low rate.<br>"Middle": medium rate.<br>"High": high rate.<br>"Highest": the highest rate. |
| isolation_threshold=? | Isolation threshold. | The value ranges from 10 ms to 30s. The default value is "1s". |
| isolation_switch=? | Isolation switch. | The value is "open" or "close", where: <br>"open": The isolation switch will be turned on. After the isolation switch is turned on, the system will suspend the HyperMetro pair when the difference between the write I/O latency of the two storage arrays is greater than the isolation switch. The storage array with the longer write I/O latency will stop providing services.<br>"close": The isolation switch will be turned off. |

##### Usage Guidelines

None

##### Example

Change the pair synchronization rate to "Low" whose pair ID is "1".

```text
developer:/>change hyper_metro_pair general pair_id=1 synchronization_rate=Low
Command executed successfully.
```

Change the synchronization rate of HyperMetro pair "1" to "Highest".

```text
developer:/>change hyper_metro_pair general pair_id=1 synchronization_rate=Highest
WARNING: You are about to change the synchronization speed to the highest After the operation, the HyperMetro pair will be synchronized at the highest speed, which may cause host latency increase and disconnection of the HyperMetro pair.
Suggestion: Select a low synchronization speed or use the highest synchronization speed during off-peak hours.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Change the mirror write I/O timeout period of HyperMetro pair "1" to "20".

```text
developer:/>change hyper_metro_pair general pair_id=1 write_secondary_timeout=20
WARNING: You are about to change the I/O timeout period for mirror write.
After the change, if the mirror write I/O timeout period is shorter than the default value, the HyperMetro relationship is easily disconnected when the latency of writing the secondary end is long.
Suggestion: Select the default I/O timeout period for mirror write.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

Change the synchronization rate of HyperMetro pair "1" to "Highest", and change the mirror write I/O timeout period of HyperMetro pair "1" to "20".

```text
developer:/>change hyper_metro_pair general pair_id=1 synchronization_rate=Highest write_secondary_timeout=20
WARNING:
You are about to change the synchronization speed to the highest and change the I/O timeout period for mirror write.
After the change, data synchronization is performed at the highest speed during HyperMetro synchronization. If the highest speed is selected, host latency may increase and the HyperMetro pair is disconnected during the synchronization.
If the mirror write I/O timeout period is shorter than the default value, the HyperMetro relationship is easily disconnected when the latency of writing the secondary end is long.
Suggestion: Select a low synchronization speed or use the "Highest" synchronization speed during off-peak hours. Select the default I/O timeout period for mirror write.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
