# change hyper_metro_consistency_group synchronize


##### Function

The **change hyper_metro_consistency_group synchronize** command is used to start the synchronization of a HyperMetro consistency group.

##### Format

**change hyper_metro_consistency_group synchronize** consistency_group_id=?

##### Parameters

| Parameter              | Description                             | Value                                                                                                |
|------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------|
| consistency_group_id=? | ID of the HyperMetro consistency group. | Run the "show hyper_metro_consistency_group general" command without parameters to obtain the value. |

##### Usage Guidelines

None

##### Example

Start the synchronization of HyperMetro consistency group "21008038bc1e70e90000000100000000".

```text
admin:/>change hyper_metro_consistency_group synchronize consistency_group_id=21008038bc1e70e90000000100000000
WARNING: You are about to start data synchronization.
Once data synchronization is started, the system will synchronize data based on the synchronization direction of the consistency group and the data at the synchronized end cannot be restored.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent data loss.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
