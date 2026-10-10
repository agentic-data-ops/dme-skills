# change disk_domain rekey


##### Function

The **change disk_domain rekey** command is used to manually update the AK according to the disk domain.

##### Format

**change disk_domain rekey** disk_domain_id=?

##### Parameters

| Parameter        | Description     | Value                          |
|------------------|-----------------|--------------------------------|
| disk_domain_id=? | Disk domain ID. | The value ranges from 0 to 63. |

##### Usage Guidelines

None.

##### Example

Manually update the AK of the disk domain whose ID is "0".

```text
admin:/>change disk_domain rekey disk_domain_id=0
DANGER: You are about to update the Authentication Keys (AKs) of the encrypted disks in the disk domain. This operation will cause a temporary decrease in system performance.
Suggestion: Before running the command, confirm that you need to update the AKs of the encrypted disks in the disk domain.
Have you read the danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
