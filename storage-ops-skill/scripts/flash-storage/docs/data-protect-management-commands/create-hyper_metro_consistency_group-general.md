# create hyper_metro_consistency_group general


##### Function

The **create hyper_metro_consistency_group general** command is used to create a HyperMetro consistency group.

##### Format

**create hyper_metro_consistency_group general** domain_id=? name=? \[ description=? \| recovery_policy=? \| synchronization_rate=? \| bandwidth=? \| isolation_switch=? \| isolation_threshold=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id=? | ID of the HyperMetro domain. | To obtain the value, run the "show hyper_metro_domain general" command. |
| name=? | Name of the consistency group. | The value contains 1 to 255 ASCII characters including digits, letters, underscores (_), hyphens (-), and periods (.), and can only start with a digit or a letter. |
| description=? | Description of the HyperMetro consistency group. | The value contains 1 to 127 letters. |
| recovery_policy=? | Recovery policy. | The value can be "automatic" or "manual", where: <br>"automatic": automatic recovery policy. Data will be automatically synchronized after faults are rectified.<br>"manual": manual recovery policy. Data needs to be manually synchronized after faults are rectified.<br> The default value is "automatic". |
| bandwidth=? | Bandwidth. | The value ranges from 1 to 1024, expressed in MB/s. |
| synchronization_rate=? | Synchronization rate. | The value can be Low, Middle, High, or Highest, where: <br>"Low": low. The value ranges from 0 to 5 MB/s.<br>Middle: medium. The value ranges from 10 MB/s to 20 MB/s.<br>High: high. The value ranges from 20 MB/s to 70 MB/s.<br>Highest: highest. The value is 100 MB/s or higher.<br> The default value is Middle. |
| isolation_threshold=? | Isolation threshold. | The value ranges from 10 ms to 30s. The default value is 200 ms. |
| isolation_switch=? | Isolation switch. | The value can be "open" or "close", where: <br>"open": Service continuity is preferentially ensured. This value is applicable to scenarios where host services have high requirements on storage latency. When the average write latency difference between the two ends of a HyperMetro pair is greater than the disconnection threshold, the system disconnects the HyperMetro pair and the end with a lower write latency provides services.<br>"close": Service data reliability is preferentially ensured. This mode is applicable to scenarios with high data protection requirements and ensures real-time data synchronization between both ends. |

##### Usage Guidelines

None

##### Example

Create a HyperMetro consistency group.

```text
admin:/>create hyper_metro_consistency_group general domain_id=8038bc1e70e90100 name=xx
WARNING:
You are about to create a HyperMetro consistency group. If the host type is Windows, enable automatic LUN SN synchronization on both storage systems before configuring HyperMetro. Otherwise, one HyperMetro LUN may be identified as two disks on the host application side. For details, see "What Can I Do If the Host Identifies One HyperMetro LUN as Two Disks?" in the "HyperMetro Feature Guide for Block" of the desired product model.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent data overwriting.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Create a HyperMetro consistency group.

```text
admin:/>create hyper_metro_consistency_group general domain_id=8038bc1e70e90100 name=xx synchronization_rate=Highest
WARNING:
You are about to set the synchronization speed to the highest to create a HyperMetro consistency group. After this operation is performed, data of HyperMetro pairs in the consistency group is synchronized at the highest speed. If you select the highest speed, the host latency may increase and the HyperMetro pairs may be disconnected during the synchronization. If the host type is Windows, enable automatic LUN SN synchronization on both storage systems before configuring HyperMetro. Otherwise, one HyperMetro LUN may be identified as two disks on the host application side. For details, see "What Can I Do If the Host Identifies One HyperMetro LUN as Two Disks?" in the "HyperMetro Feature Guide for Block" of the desired product model.
Suggestion: Select a lower synchronization speed or select the highest synchronization speed during off-peak hours.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
