# change fs_hyper_metro_domain recover_policy


##### Function

The **change fs_hyper_metro_domain recover_policy** command is used to modify the recovery policy of a HyperMetro domain cluster.

##### Format

**change fs_hyper_metro_domain recover_policy** domain_id=? recover_policy=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id | HyperMetro domain ID of the file system. | You can run the "show fs_hyper_metro_domain general" command to obtain the value. |
| recover_policy | Restoration policy. | The value can be "automatic recover" or "manual recover", where: <br>"automatic recover": automatic recovery.<br>"manual recover": manual recovery. |

##### Usage Guidelines

OceanStor Dorado 3000 V6, Dorado 5000 V6, Dorado 6000 V6 and Dorado 8000 V6 storage systems support this command.

##### Example

Modify the recovery policy of a domain. The domain ID is "1" and the recovery policy is "manual_recover".

```text
admin:/>change fs_hyper_metro_domain recover_policy domain_id=1 recover_policy=manual_recover
Command executed successfully.
```

##### System Response

None
