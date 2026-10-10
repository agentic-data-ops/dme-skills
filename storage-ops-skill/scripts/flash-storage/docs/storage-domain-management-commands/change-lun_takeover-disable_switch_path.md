# change lun_takeover disable_switch_path


##### Function

The **change lun_takeover disable_switch_path** command is used to forbid the specified LUN's paths to be switched back to the source array and to allow the LUN to be used as the source LUN for online takeover.

##### Format

**change lun_takeover disable_switch_path** lun_id=?

##### Parameters

| Parameter | Description      | Value                                                 |
|-----------|------------------|-------------------------------------------------------|
| lun_id=?  | Takeover LUN ID. | To obtain the value, run "show lun_takeover general". |

##### Usage Guidelines

None

##### Example

Forbid the specified LUN's paths to be switched back to the source array and to allow the LUN to be used as the source LUN for online takeover.

```text
admin:/>change lun_takeover disable_switch_path lun_id=0
WARNING: You are about to prevent switching over the takeover LUN path back to the source disk array. This operation may cause the link between the storage array and the host to fail to deliver services.
Suggestion: Before performing this operation, ensure that the link between the disk array and the host is no longer used.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
