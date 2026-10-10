# change hyper_metro_pair general


##### Function

The **change hyper_metro_pair general** command is used to change HyperMetro pair attributes.

##### Format

**change hyper_metro_pair general** pair_id=? { recovery_policy=? \| synchronization_rate=? \| bandwidth=? \| isolation_switch=? \| isolation_threshold=? } \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pair_id=? | ID of the HyperMetro pair. | To obtain the value, run the "show hyper_metro_pair general" command without parameters. |
| recovery_policy=? | Recovery policy. | The value can be "automatic" or "manual", where: <br>automatic: Data synchronization is automatically restored after the fault is rectified.<br>"manual": Data synchronization is manually restored after the fault is rectified. |
| bandwidth=? | Bandwidth. | The value ranges from 1 to 1024, expressed in MB/s. |
| synchronization_rate=? | Synchronization rate. | The value can be Low, Middle, High, or Highest, where: <br>"Low": low. The value ranges from 0 MB/s to 5 MB/s.<br>Middle: medium. The value ranges from 10 MB/s to 20 MB/s.<br>High: high. The value ranges from 20 MB/s to 70 MB/s.<br>Highest: 100 MB/s or higher.<br> The default value is Middle. |
| bandwidth=? | Bandwidth. | The value ranges from 1 to 1024, expressed in MB/s. |
| isolation_threshold=? | Isolation threshold. | The value ranges from 10 ms to 30s. The default value is 200 ms. |
| isolation_switch=? | Isolation switch. | The value can be "open" or "close", where: <br>"open": Service continuity is preferentially ensured. This value is applicable to scenarios where host services have high requirements on storage latency. When the average write latency difference between the two ends of a HyperMetro pair is greater than the disconnection threshold, the system disconnects the HyperMetro pair and the end with a lower write latency provides services.<br>"close": Service data reliability is preferentially ensured. This mode is applicable to scenarios with high data protection requirements and ensures real-time data synchronization between both ends. |

##### Usage Guidelines

None

##### Example

Change the pair synchronization rate to "Low" whose pair ID is "1".

```text
admin:/>change hyper_metro_pair general pair_id=1 synchronization rate=Low
Command executed successfully.
```

Change the synchronization of HyperMetro pair "1" to "Highest".

```text
admin:/>change hyper_metro_pair general pair_id=1 synchronization_rate=Highest
WARNING: You are about to change the synchronization speed to the highest After the operation, the HyperMetro pair will be synchronized at the highest speed, which may cause host latency increase and disconnection of the HyperMetro pair.
Suggestion: Select a low synchronization speed or use the highest synchronization speed during off-peak hours.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
