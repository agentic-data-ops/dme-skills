# delete fs_hyper_metro_domain general


##### Function

The **delete fs_hyper_metro_domain general** command is used to delete a HyperMetro domain.

##### Format

**delete fs_hyper_metro_domain general** domain_id=? \[ is_local_delete=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| domain_id=? | HyperMetro domain ID. | To obtain the value, run the "show fs_hyper_metro_domain general" command. |
| is_local_delete=? | Whether to delete a HyperMetro domain from only the local storage system or from both local and remote storage systems. | The value can be "yes" or "no", where: <br>"no": deletes the HyperMetro domain from both local and remote storage systems.<br>"yes": deletes the HyperMetro domain from only the local storage system.<br> The default value is "no". |

##### Usage Guidelines

None

##### Example

Delete the HyperMetro domain whose ID is "1".

```text
admin:/>delete fs_hyper_metro_domain general domain_id=1
Command executed successfully.
```

##### System Response

None
