# remove hyper_metro_consistency_group pair


##### Function

The **remove hyper_metro_consistency_group pair** command is used to delete a pair from a HyperMetro consistency group.

##### Format

**remove hyper_metro_consistency_group pair** consistency_group_id=? \[ pair_id=? \] \[ pair_id_list=? \]

##### Parameters

| Parameter              | Description                             | Value                                                                                                    |
|------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------|
| consistency_group_id=? | ID of the HyperMetro consistency group. | Run the "show hyper_metro_consistency_group general" command without any parameters to obtain the value. |
| pair_id=?              | ID of the HyperMetro pair.              | Run the "show hyper_metro_consistency_group pair" command to obtain the value.                           |
| pair_id_list=?         | HyperMetro pair ID list.                | You can run the show hyper_metro_consistency_group pair command to obtain the value.                     |

##### Usage Guidelines

None

##### Example

Delete pair 21008038bc1e70e90000000000000000 from consistency group 21008038bc1e70e90000000100000000.

```text
admin:/>remove hyper_metro_consistency_group pair consistency_group_id=21008038bc1e70e90000000100000000 pair_id=21008038bc1e70e90000000000000000
WARNING: You are about to remove a pair from the HyperMetro consistency group.
After the pair is removed from the consistency group, the pair will use its own control policies. Its running status is not consistent with that of the consistency group.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete members 21008038bc1e70e90000000000000000 and 21008038bc1e70e90000000000000001 from the consistency group whose ID is 21008038bc1e70e90000000100000000.

```text
admin:/>remove hyper_metro_consistency_group pair consistency_group_id=21008038bc1e70e90000000100000000 pair_id_list=21008038bc1e70e90000000000000000,21008038bc1e70e90000000000000001
WARNING: You are about to remove a pair from the HyperMetro consistency group.
After the pair is removed from the consistency group, the pair will use its own control policies. Its running status is not consistent with that of the consistency group.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Remove pair 21008038bc1e70e90000000000000000 from hyper metro consistency successfully.
Remove pair 21008038bc1e70e90000000000000001 from hyper metro consistency successfully.
```

##### System Response

None
