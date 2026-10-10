# change fs_hyper_metro_domain start


##### Function

The **change fs_hyper_metro_domain start** command is used to forcibly start a HyperMetro domain.

##### Format

**change fs_hyper_metro_domain start** domain_id=?

##### Parameters

| Parameter   | Description           | Value                                                                      |
|-------------|-----------------------|----------------------------------------------------------------------------|
| domain_id=? | HyperMetro domain ID. | To obtain the value, run the "show fs_hyper_metro_domain general" command. |

##### Usage Guidelines

None

##### Example

Forcibly start HyperMetro domain "1".

```text

admin:/>change fs_hyper_metro_domain start domain_id=1
DANGER: You are about to forcibly enable the host access permission of the HyperMetro domain of the local file system. Ensure that the remote site does not accept host access requests. Otherwise, data may be lost.
Suggestion: Before performing this operation, disconnect the remote site from the host.
Have you read danger alert message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.

```

##### System Response

None
