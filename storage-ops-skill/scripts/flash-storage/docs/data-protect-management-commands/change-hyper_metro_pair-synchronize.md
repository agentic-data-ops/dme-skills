# change hyper_metro_pair synchronize


##### Function

The **change hyper_metro_pair synchronize** command is used to start synchronizing a HyperMetro pair.

##### Format

**change hyper_metro_pair synchronize** pair_id=?

**change hyper_metro_pair synchronize** pair_id_list=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pair_id=? | HyperMetro pair ID. | Run the "show hyper_metro_pair general" command to obtain the value. |
| pair_id_list=? | HyperMetro pair ID list. | "show Hyper_metro_pair general" is used to obtain all available HyperMetro pairs.<br>Use commas (,) to separate multiple pair IDs.<br>A maximum of 100 IDs can be entered. |

##### Usage Guidelines

None

##### Example

Start synchronizing HyperMetro pair "1".

```text
admin:/>change hyper_metro_pair synchronize pair_id=1
WARNING: You are going to start data synchronization.
Once data synchronization is started, the system synchronizes data in the default synchronization direction of HyperMetro. After data synchronization, the data cannot be restored.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent data loss.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Start to synchronize the IDs of multiple HyperMetro pairs.

```text
admin:/>change hyper_metro_pair synchronize pair_id_list=1,2
WARNING: You are going to start data synchronization.
Once data synchronization is started, the system synchronizes data in the default synchronization direction of HyperMetro. After data synchronization, the data cannot be restored.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent data loss.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Change hyper metro pair synchronize 1 successfully.
Change hyper metro pair synchronize 2 successfully.
```

##### System Response

None
