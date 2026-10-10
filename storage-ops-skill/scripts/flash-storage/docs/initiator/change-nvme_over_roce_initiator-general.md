# change nvme_over_roce_initiator general


##### Function

The **change nvme_over_roce_initiator general** command is used to modify the attributes of an initiator, including its alias and NVMe qualified name (NQN), as well as replace an initiator.

##### Format

**change nvme_over_roce_initiator general** nvme_over_roce_nqn=? \[ new_nqn=? \] \[ alias=? \]

##### Parameters

| Parameter            | Description                              | Value                                                                                                           |
|----------------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| nvme_over_roce_nqn=? | NQN of an NVMe over RoCE initiator.      | To obtain the value, run "show nvme_over_roce_initiator general".                                               |
| alias=?              | Alias of an initiator.                   | The value contains 1 to 31 characters including digits, letters, underscores (\_), periods (.) and hyphens (-). |
| new_nqn=?            | NQN of the new NVMe over RoCE initiator. | The value contains 1 to 223 characters (32 \< ASCII codes \< 127) and must start with a letter or digit.        |

##### Usage Guidelines

After an initiator is replaced, the new initiator inherits all the features and mappings of the old one. For example, if the old initiator existed in a mapping view and was added to a host, the new initiator will exist in the same mapping view and will be added to the same host.

##### Example

Change the alias of the NVMe over RoCE initiator whose NQN is "455856585f654578" to "newroce".

```text
admin:/>change nvme_over_roce_initiator general nvme_over_roce_nqn=455856585f654578 alias=newroce
Command executed successfully.
```

Replace the NVMe over RoCE initiator whose NQN is "10000000c9b7bc72" with another NVMe over RoCE initiator whose NQN is "1234567890123456".

```text
admin:/>change nvme_over_roce_initiator general nvme_over_roce_nqn=10000000c9b7bc72 new_nqn=1234567890123456
DANGER: You are about to modify the initiator identifier. This operation will remove and delete the specified offline initiator from the host.
Suggestion: Before performing this operation, ensure that you choose the offline initiator that has been added to the host.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Query old initiator.
Remove old initiator from host.
Delete old initiator.
Create or change new initiator.
Command executed successfully.
```

##### System Response

None
