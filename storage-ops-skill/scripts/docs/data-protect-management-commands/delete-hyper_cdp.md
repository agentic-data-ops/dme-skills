# delete hyper_cdp


##### Function

The **delete hyper_cdp** command is used to delete HyperCDP objects.

##### Format

**delete hyper_cdp** cdp_id_list=? \[ lun_id=? \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_id_list=? | ID of a HyperCDP object. | The value is an integer ranging from 0 to 1999999.<br>To obtain the value, run "show hyper_cdp general".<br>You can delete multiple HyperCDP objects at the same time. Multiple HyperCDP object IDs are separated by commas (,), or the ID range is separated by hyphens (-), such as: "0,5-8". |
| lun_id=? | Source LUN ID. | The value is an integer ranging from 0 to 65535.<br>To obtain the value, run the "show lun general" command. |

##### Usage Guidelines

-   Multiple HyperCDP objects can be deleted at the same time.
-   Before running this command, ensure that the selected HyperCDP objects are exactly the ones you want to delete and are no longer needed.

##### Example

Delete HyperCDP object "1".

```text
admin:/>delete hyper_cdp cdp_id_list=1
WARNING: You are about to delete the HyperCDP object, which is an irreversible operation.
This operation will delete the information about the HyperCDP object from the system.
Suggestion: Before performing this operation, ensure that the selected HyperCDP object is correct and it is not required.
Have you read warning message carefully?(y/n)y

Are you sure you really want to perform the operation?(y/n)y
Delete HyperCDP object 1 successfully.
```

##### System Response

None
