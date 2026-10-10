# change lun_takeover finish_switch_path


##### Function

The **change lun_takeover finish_switch_path** command is used to confirm that the host paths of the specified LUN have been switched to the paths between the host and the target disk array.

##### Format

**change lun_takeover finish_switch_path** lun_id=?

##### Parameters

| Parameter | Description | Value                                                 |
|-----------|-------------|-------------------------------------------------------|
| lun_id=?  | LUN ID.     | To obtain the value, run "show lun_takeover general". |

##### Usage Guidelines

None

##### Example

Confirm that the host paths of the specified LUN have been switched to the paths between the host and the target storage array.

```text
admin:/>change lun_takeover finish_switch_path lun_id=0
DANGER: You are about to switch over the LUN paths. This operation may cause data loss.
Suggestion: Before performing this operation, confirm that the host path of the LUN has been switched to the target array.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
