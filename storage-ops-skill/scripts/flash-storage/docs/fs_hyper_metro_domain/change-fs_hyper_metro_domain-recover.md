# change fs_hyper_metro_domain recover


##### Function

The **change fs_hyper_metro_domain recover** command is used to recover a file system HyperMetro domain.

##### Format

**change fs_hyper_metro_domain recover** domain_id=?

##### Parameters

| Parameter   | Description                       | Value                                                                             |
|-------------|-----------------------------------|-----------------------------------------------------------------------------------|
| domain_id=? | File system HyperMetro domain ID. | You can run the "show fs_hyper_metro_domain general" command to obtain the value. |

##### Usage Guidelines

OceanStor Dorado 3000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Restore the file system HyperMetro domain. The domain ID is "10100".

```text
admin:/>change fs_hyper_metro_domain recover domain_id=10100
DANGER: You are about to recover the file system HyperMetro domain. Once the recovery is started, the system synchronizes data based on the default synchronization direction of the HyperMetro domain. Once data synchronization starts, the data at the synchronized end cannot be recovered.
Suggestion: Before performing this operation, ensure that the operation and parameters are correct to prevent data loss.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
