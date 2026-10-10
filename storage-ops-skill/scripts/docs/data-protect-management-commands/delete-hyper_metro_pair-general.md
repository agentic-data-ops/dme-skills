# delete hyper_metro_pair general


##### Function

The **delete hyper_metro_pair general** command is used to delete a HyperMetro pair.

##### Format

**delete hyper_metro_pair general** pair_id=? \[ is_local_delete=? \| is_refresh_wwn=? \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| pair_id=? | ID of a HyperMetro pair. | Run the "show hyper_metro_pair general" command to obtain the value. |
| is_local_delete=? | Whether the pair will be deleted from local devices. Only if "is_local_delete" is set to "yes", parameter "is_refresh_wwn" is displayed. | The value is "yes" or "no", where: <br>"yes": The pair will be deleted from local devices.<br>"no": The pair will not be deleted from local devices.<br> The default value is "no". |
| is_refresh_wwn=? | Whether to refresh the LUN WWN (valid for SAN HyperMetro pair local delete only). | The value is "yes" or "no", where: <br>"yes": to refresh the WWN.<br>"no": not to refresh the WWN.<br> The default value is "yes". |

##### Usage Guidelines

None

##### Example

Locally delete the HyperMetro pair whose ID is "1".

```text
admin:/>delete hyper_metro_pair general pair_id=1 is_local_delete=yes
WARNING: You are about to delete a HyperMetro pair, which cannot be undone. If you need the configuration later, you must create it again.
To prevent LUN WWN conflicts, refresh LUN WWNs when you delete a HyperMetro pair from the storage array that is inaccessible to hosts.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the HyperMetro pair whose ID is "1".

```text
admin:/>delete hyper_metro_pair general pair_id=1
WARNING: You are about to delete a HyperMetro pair, which cannot be undone. If you need the configuration later, you must create it again.
To prevent LUN WWN conflicts, refresh LUN WWNs when you delete a HyperMetro pair from the storage array that is inaccessible to hosts.
Suggestion: Before performing this operation, ensure that the parameters are configured correctly to prevent service exceptions.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Delete the file system HyperMetro pair whose pair ID is "1".

```text
admin:/>delete hyper_metro_pair general pair_id=1
WARNING: You are about to delete the HyperMetro pair. You are advised to perform this operation after stopping the services of the file system. Otherwise, host services may be interrupted or access exceptions may occur. After the HyperMetro relationship is deleted, if the corresponding vStore pair is not deleted, the file system cannot be accessed. If the file system continues providing access services, the access will be abnormal. After this operation, the primary site retains the latest data and the file system at the secondary site cannot be accessed.
After this operation, the configuration cannot be restored. You must re-create the configuration if needed.
Suggestion:
1. Before performing this operation, ensure that the operation and parameters are correct to prevent service exceptions.
2. After the HyperMetro relationship is deleted, delete the corresponding vStore pair or file system to prevent service exceptions of the local file system caused by HyperMetro vStore service switchover.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
