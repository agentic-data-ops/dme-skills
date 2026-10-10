# create consistency_group synchronization


##### Function

The **create consistency_group synchronization** command is used to create a synchronous consistency group. You can centrally manage multiple synchronous remote replication pairs by running this command.

##### Format

**create consistency_group synchronization** name=? { recovery_policy=? \| synchronization_rate=? \| bandwidth=? \| remote_device_id=? \| remote_io_timeout_period=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| name=? | Name of a consistency group. | The value contains 1 to 255 ASCII characters including digits, letters, underscores (_), hyphens (-), and periods (.),can only start with a digit or a letter. |
| remote_device_id=? | Remote device ID. | To obtain the value, run "show remote_device general". |
| recovery_policy=? | Link recovery policy. This parameter defines a policy for recovering the links that were unexpectedly disconnected for the remote replication pairs in a consistency group. | The value can be "automatic" or "manual", where: <br>"automatic": When links are recovered, the remote replication tasks in the consistency group are resumed automatically.<br>"manual": When links are recovered, the remote replication tasks in the consistency group need to be resumed manually. The consistency group retains the state preserved at the time when links are interrupted, and does not resume the interrupted remote replication tasks automatically.<br> The default value is "automatic". |
| synchronization_rate=? | Synchronization speed. | The value can be "Low", "Middle", "High", or "Highest", where: <br>"Low": indicates the low rate.<br>"Middle": indicates the medium rate.<br>"High": indicates the high rate.<br>"Highest": indicates the highest rate.<br> The default value is "Middle". |
| bandwidth=? | Data synchronization speed between storage arrays. | The value ranges from 1 to 1024, expressed in MB/s. |
| remote_io_timeout_period=? | Timeout period of I/Os written to the secondary storage array during dual-write of synchronous remote replication. | The value ranges from 10 to 30, expressed in seconds. |

##### Usage Guidelines

-   A synchronous consistency group can only contain synchronous remote replication pairs.
-   For a synchronous remote replication pair, the storage system writes both the primary and secondary LUNs. In this condition, a host will be informed that the write request has been successfully responded only after writing both the primary and secondary LUNs has succeeded. This replication mode ensures data consistency between each pair of primary and secondary LUNs but suffers from a relatively low responsiveness to write requests.

##### Example

Create a synchronous consistency group whose name is "abc", recovery policy is "automatic", and synchronization speed is "Low".

```text
admin:/>create consistency_group synchronization name=abc recovery_policy=automatic synchronization_rate=low
Command executed successfully.
```

Create a synchronous consistency group whose name is "efg", synchronization speed is "Highest", and recovery policy is "automatic".

```text

admin:/>create consistency_group synchronization name=efg synchronization_rate=Highest
WARNING: You are about to select the "Highest" speed to create a consistency group. After the operation, remote replication pairs in the consistency group will be synchronized at the highest speed, which may cause overloaded services and disconnection of remote replication pairs.
Suggestion: Select the "High" speed. If you select the "Highest" speed, check the performance of the local and remote devices and whether the replication link bandwidth is sufficient to prevent the disconnection of remote replication pairs during synchronization.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
