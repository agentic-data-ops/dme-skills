# change fs_hyper_metro_domain priority


##### Function

The change fs_hyper_metro_domain command is used to change the preferred site of a HyperMetro domain cluster.

##### Format

**change fs_hyper_metro_domain priority** domain_id=?

##### Parameters

| Parameter   | Description                | Value                                                                      |
|-------------|----------------------------|----------------------------------------------------------------------------|
| domain_id=? | ID of a HyperMetro domain. | To obtain the value, run the "show fs_hyper_metro_domain general" command. |

##### Usage Guidelines

None

##### Example

Modify the preferred site of HyperMetro domain "1".

```text
admin:/>change fs_hyper_metro_domain priority domain_id=1
WARNING: You are about to perform a preferred site switchover. This operation will change the arbitration priority of the file system HyperMetro domain when the communication between storage arrays is interrupted.
If no quorum server is available or the quorum server is unavailable, and the communication between storage arrays is interrupted during the priority switchover, the arbitration between the two storage arrays may fail and services may be interrupted.
Suggestion: Before performing this operation, split the file system HyperMetro domain if no quorum server is available or the quorum server is unavailable.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
