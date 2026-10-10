# change hyper_metro_consistency_group general


##### Function

The **change hyper_metro_consistency_group general** command is used to change the information about a HyperMetro consistency group.

##### Format

**change hyper_metro_consistency_group general** consistency_group_id=? { synchronization_rate=? \| bandwidth=? \| name=? \| recovery_policy=? \| description=? \| isolation_switch=? \| isolation_threshold=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| consistency_group_id=? | ID of the HyperMetro consistency group. | To obtain the value, run the "show hyper_metro_consistency_group general" command without parameters. |
| synchronization_rate=? | Synchronization rate. | The value can be Low, Middle, High, or Highest, where: <br>"Low": low. The value ranges from 0 to 5 MB/s.<br>Middle: medium. The value ranges from 10 MB/s to 20 MB/s.<br>High: high. The value ranges from 20 MB/s to 70 MB/s.<br>Highest: highest. The value is 100 MB/s or higher.<br> The default value is Middle. |
| name=? | Name of the consistency group. | The value contains 1 to 255 ASCII characters, including digits, letters, underscores (_), hyphens (-), and periods (.), and can only start with a digit or a letter. |
| recovery_policy=? | Recovery policy. | The value can be "automatic" or "manual", where: <br>"automatic": automatic recovery policy. Data will be automatically synchronized after faults are rectified.<br>"manual": manual recovery policy. Data needs to be manually synchronized after faults are rectified. |
| description=? | Description of the HyperMetro consistency group. | The value contains 1 to 127 letters. |
| isolation_switch=? | Isolation switch. | The value can be "open" or "close", where: <br>"open": enables the array isolation function. After the isolation function is enabled, if the write I/O latency difference between the two storage arrays is greater than the isolation threshold, the system suspends the HyperMetro pairs in the consistency group. The storage array with a larger write I/O latency stops providing services.<br>"close": disables the array isolation function. |
| isolation_threshold=? | Isolation threshold. | The value ranges from 10 ms to 30s. The default value is 200 ms. |
| bandwidth=? | Bandwidth. | The value ranges from 1 to 1024, expressed in MB/s. |

##### Usage Guidelines

None

##### Example

Change the synchronization rate of HyperMetro consistency group 21009017acb3845f0000000100000000 to "Low".

```text
admin:/>change hyper_metro_consistency_group general consistency_group_id=21009017acb3845f0000000100000000 synchronization_rate=Low
Command executed successfully.
```

Change the synchronization rate of HyperMetro consistency group 21009017acb3845f0000000100000000 to "Highest".

```text
admin:/>change hyper_metro_consistency_group general consistency_group_id=21009017acb3845f0000000100000000 synchronization_rate=Highest
WARNING: You are about to change the synchronization speed to the highest. After the operation, the HyperMetro pairs will be synchronized at the highest speed, which may cause host latency increase and disconnection of HyperMetro pairs.
Suggestion: Select a low synchronization speed or use the highest synchronization speed during off-peak hours.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
