# add hyper_metro_consistency_group pair


##### Function

The **add hyper_metro_consistency_group pair** command is used to add a HyperMetro pair to a HyperMetro consistency group.

##### Format

**add hyper_metro_consistency_group pair** consistency_group_id=? \[ pair_id=? \] \[ pair_id_list=? \]

##### Parameters

| Parameter              | Description                             | Value                                                                                                |
|------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------|
| consistency_group_id=? | ID of the HyperMetro consistency group. | Run the "show hyper_metro_consistency_group general" command without parameters to obtain the value. |
| pair_id=?              | ID of the HyperMetro pair.              | Run the "show hyper_metro_pair general" command without parameters to obtain the value.              |
| pair_id_list=?         | HyperMetro pair ID list.                | You can run the show hyper_metro_pair general command to obtain the value.                           |

##### Usage Guidelines

None

##### Example

Add HyperMetro pair 21008038bc1e70e90000000000000000 to HyperMetro consistency group 21008038bc1e70e90000000100000000.

```text
admin:/>add hyper_metro_consistency_group pair consistency_group_id=21008038bc1e70e90000000100000000 pair_id=21008038bc1e70e90000000000000000
CAUTION: You are about to add a pair to the HyperMetro consistency group.
After the pair is added to the consistency group, the pair will use the consistency group's control policies. You cannot operate the pair in this consistency group.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent service exceptions.
Do you wish to continue?(y/n)y
Command executed successfully.
```

Add the pair members 21008038bc1e70e90000000000000000 and 21008038bc1e70e90000000000000001 to the consistency group 21008038bc1e70e90000000100000000.

```text
admin:/>add hyper_metro_consistency_group pair consistency_group_id=21008038bc1e70e90000000100000000 pair_id_list=21008038bc1e70e90000000000000000,21008038bc1e70e90000000000000001
CAUTION: You are about to add a pair to the HyperMetro consistency group.
After the pair is added to the consistency group, the pair will use the consistency group's control policies. You cannot operate the pair in this consistency group.
Suggestion: Before performing this operation, ensure that the parameters are correct to prevent service exceptions.
Do you wish to continue?(y/n)y
Add pair 21008038bc1e70e90000000000000000 to hyper metro consistency group successfully.
Add pair 21008038bc1e70e90000000000000001 to hyper metro consistency group successfully.
```

##### System Response

None
