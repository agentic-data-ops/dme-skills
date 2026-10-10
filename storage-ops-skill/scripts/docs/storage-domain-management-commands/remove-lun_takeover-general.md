# remove lun_takeover general


##### Function

The **remove lun_takeover general** command is used to delete the information about a takeover LUN.

##### Format

**remove lun_takeover general** lun_id=?

##### Parameters

| Parameter | Description | Value                                                 |
|-----------|-------------|-------------------------------------------------------|
| lun_id=?  | LUN ID.     | To obtain the value, run "show lun_takeover general". |

##### Usage Guidelines

None

##### Example

To delete information about takeover LUN 0, run the following command:

```text
admin:/>remove lun_takeover general lun_id=0
WARNING: You are about to remove LUN_TAKEOVER. This operation will change the disk information recognized by the hosts and then interrupt services.
Suggestion: Before performing this operation, ensure that the TAKEOVER LUN is no longer necessary.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
